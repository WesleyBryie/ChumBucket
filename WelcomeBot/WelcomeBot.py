import datetime
import json
import pickle
import praw
import re
import time
from fuzzywuzzy import fuzz

JSON_LOG_PATH = './log.json'
LOG_LIST = []

CREDENTIALS_PATH = './PiracyBot_AccountCredentials.json'
USERS_JSON_PATH = 'Users.json'
SUBREDDIT_NAME = 'Piracy'
BOT_USERNAME = 'PiracyBot'

POSSIBLE_RULE3_RE = [r'trying to \w+ a ((tv )?show|movie|series)', r'can \w+ help me (find|torrent|stream)', r'looking for a ((tv )?show|movie|series)', r'where (i can|can i|to) (download|get|stream|watch|torrent|find)', r'anyone know (of )?a \w* ?(to )?(place|link|torrent)', r'best \w+ to (download|get|stream|watch|torrent)', r'free ([^\.,?!\n]+ ){1, 6} site', r'any good (link|place|\w*site)', r'\b(download|get|stream|watch|torrent|find)\b[^\.,?!\n]+(show|movie|series)[^\.,?!]+\?\n', r'free download(?! manager)', r'safe link', r'looking for [^\.,?!\n]+(book|movie|show|link|site|place|download|free)', r'(any|where|site|link)[\w ]+book[\w ]+free\?', r'\bwhere (do|can)[^\.,?!\n]{2,15}(get[^\n\.,?!]+\?|find)', r'where (can i|do i|to) [^\.,?!\n]+free', r'^looking for', r'\ba [pd]m\br']
HOURS_DATETIME_RE = r'(\d+)(:.+)\.'

# Post will not be approved by bot if OP does not answer within 12 hours.
MAX_TIME_ALLOWANCE = 3600 * 10
# how frequent to save to Users.json
SAVE_FREQUENCY = 60 * 5

RULES_URL = 'https://www.reddit.com/r/Piracy/wiki/piracy_rules'
WELCOME_MESSAGE_SUBJECT_TITLE = 'Message from /r/Piracy'
REMOVAL_MESSAGE_SUBJECT_TITLE = 'Concerning your /r/Piracy submission'

WELCOME_MESSAGE = '''Welcome to /r/Piracy! You are receiving this message because you are new to the subreddit. If you are not new, then don't worry, you will not be messaged a second time!

---
        
[Please make sure to read our rules](https://www.reddit.com/r/Piracy/wiki/piracy_rules), as it will help to save the subreddit and yourself from being banned in the possible future.

**[Also see our Wiki](/r/Piracy/wiki/index)**, which contains a list of sites, tools, FAQ, and other useful resources.

Your question also may have been asked previously - you can search the subreddit via google - example: https://i.imgur.com/1jA767u.jpg
'''

REQUIRED_REPLY = 'I have read the rules and the wiki'
REQUIRED_REPLY_RE = r'i (\w+ )?read (\w+ )?rules \w+ (\w+ )?wiki'

REMOVAL_MESSAGE_FIRST_HALF = 'Thank you for [your submission.]('
REMOVAL_MESSAGE_SECOND_HALF = f''') I am a bot. Since you are new to the subreddit, your submission is not yet visible to everyone. 

---

**Please read** [**the rules.**](https://www.reddit.com/r/Piracy/wiki/piracy_rules)

**(Also see our Wiki)[/r/Piracy/wiki/index]**, which contains a list of sites, tools, FAQ, and other useful resources.

Your question also may have been asked previously - you can search the subreddit via google - example: https://i.imgur.com/1jA767u.jpg

---

If your submission abides by the rules and is not covered by the wiki, please reply to this message with "{REQUIRED_REPLY}" to have your submission approved.

'''

SORRY_REPLY = f'You are past the {int(MAX_TIME_ALLOWANCE/3600)}-hour time window. Your submission would be buried if it were approved now. Please re-submit.'

OVERRIDE_UNAVAILABLE_REPLY  = '''Your submission has been removed by another moderator. This bot is unable to override this action.

---

[Contact the moderators of this subreddit if you have any concerns](https://www.reddit.com/message/compose/?to=/r/Piracy)'''

# Capture group for the permalink that was removed, appearing in the bot welcome message
PERMALINK_FIRST_MESSAGE = r'\((.+?)\)'

def main():
    with open(CREDENTIALS_PATH, 'r', encoding='utf8') as f:
        credentials = json.load(f)

    CLIENT_ID = credentials['client_id']
    CLIENT_SECRET = credentials['client_secret']
    USERNAME = credentials['username']
    PASSWORD = credentials['password']
    USER_AGENT = credentials['user_agent']

    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, username=USERNAME, password=PASSWORD, user_agent=USER_AGENT)

    Users = getUsers()
    startTime = time.time()
    timeLastSavedUsers = startTime
    print(f'Started at {getProperDatetime(datetime.datetime.now().time())}')

    monitorStream(startTime, timeLastSavedUsers, Users, reddit)
    

def monitorStream(startTime, timeLastSavedUsers, Users, reddit):
    subreddit = reddit.subreddit(SUBREDDIT_NAME)
    submission_stream = subreddit.stream.submissions(pause_after=-1)
    comment_stream = subreddit.stream.comments(pause_after=-1)
    inbox_stream = reddit.inbox.stream(pause_after=-1)

    try:
        while True:
            for submission in submission_stream:
                if submission is None or submission.author is None:
                    break
                if isUserNew(submission.author.name, Users):
                    processSubmission(startTime, reddit, submission)
            for comment in comment_stream:
                if comment is None or comment.author is None:
                    break
                if isUserNew(comment.author.name, Users) and not REQUIRED_REPLY.lower() in comment.body.lower():
                    processComment(startTime, Users, reddit, comment)
            for message in inbox_stream:
                # log_json('Checking messages', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                if message is None or message.author is None:
                    # log_json('Message is None', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    break
                if isinstance(message, praw.models.Message) and (fuzz.token_set_ratio(REQUIRED_REPLY, message.body) > 90 or re.search(REQUIRED_REPLY_RE, message.body, re.IGNORECASE)):
                    # log_json('Processing message', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    processMessage(Users, reddit, message)
                message.mark_read()

            # Save Users to json every 5 minutes
            currTime = time.time()
            if currTime - timeLastSavedUsers > SAVE_FREQUENCY:
                timeLastSavedUsers = currTime
                with open(USERS_JSON_PATH, 'w', encoding='utf8') as f:
                    json.dump(Users, f, indent=4)
                print(f'Saved at {getProperDatetime(datetime.datetime.now().time())}')
    except Exception as e:
        print(f' >>>>> There was an error: {str(e)}')
        time.sleep(60)  # wait for 60 seconds before restarting
        monitorStream(startTime, timeLastSavedUsers, Users, reddit)

def log_json(logStr, now):
    if int(time.time()) % 120 > 10:
        return
    logList = []
    with open(JSON_LOG_PATH, 'r', encoding='utf8') as f:
        logList = json.load(f)

    logList.append(logStr + ' ' + str(now))

    with open(JSON_LOG_PATH, 'w', encoding='utf8') as f:
        json.dump(logList, f, indent=4)


def processSubmission(startTime, reddit, submission_temp):
    subID = submission_temp.id
    time.sleep(2)
    # reload submission to get fresh data
    submission = reddit.submission(id=subID)

    if submission.banned_by is None and not submission.approved and submission.created_utc > startTime:
        permalink = submission.permalink
        submissionID = submission.id
        authorName = submission.author.name
        submissionTitle = submission.title

        submission.mod.remove()
        print(f' > Removed submission by {authorName} : {submissionID} : {submissionTitle}')
        recipient = reddit.redditor(authorName)
        recipient.message(subject=REMOVAL_MESSAGE_SUBJECT_TITLE, message=f'{REMOVAL_MESSAGE_FIRST_HALF}https://reddit.com{permalink}{REMOVAL_MESSAGE_SECOND_HALF}')


def processComment(startTime, Users, reddit, comment):
    if comment.created_utc > startTime:
        authorName = comment.author.name

        print(f' > Welcoming {authorName}')
        # comment.mod.remove()
        recipient = reddit.redditor(authorName)
        recipient.message(subject=WELCOME_MESSAGE_SUBJECT_TITLE, message=f'{WELCOME_MESSAGE}')
        if not authorName in Users:
            Users[authorName] = 'Comment: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def processMessage(Users, reddit, message):
    try:
        firstMessage = reddit.inbox.message(message.first_message_name[3:])
    except:
        message.mark_read()
        message.reply('There was an issue. You must reply to the original PM instead of creating a new message.')
        return

    firstMessageText = firstMessage.body
    if not RULES_URL in firstMessageText:
        message.mark_read()
        return

    fullPermalink = re.search(PERMALINK_FIRST_MESSAGE, firstMessageText).groups()[0]
    authorName = message.author.name
    currTime = time.time()

    # if url is a a submission permalink
    if fullPermalink.count('/') == 8:
        submission = reddit.submission(url=fullPermalink)
        submissionTitle = submission.title
        submissionID = submission.id
        SubmissionBannedBy = submission.banned_by

        # if submission is not removed
        if SubmissionBannedBy is None:
            message.reply(f'[Your submission]({fullPermalink}) has already been approved is visible to everyone.')
        # if reply is past the MAX_TIME_ALLOWANCE (seconds)
        elif currTime - submission.created_utc > MAX_TIME_ALLOWANCE:
            message.reply(SORRY_REPLY)
        elif SubmissionBannedBy != BOT_USERNAME:
            message.reply(OVERRIDE_UNAVAILABLE_REPLY)
        elif SubmissionBannedBy == BOT_USERNAME:
            print(f' >>> Approving submission by {authorName} : {submissionID} : {submissionTitle}')
            submission.mod.approve()
            if submission.is_self:
                processApprovedSubmission(submission)
            message.reply(f'Thank you. [Your submission]({fullPermalink}) is now visible to everyone.')
        if not authorName in Users:
            Users[authorName] = 'Submission: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # if url is a comment fullPermalink
    # elif fullPermalink.count('/') == 9:
    #     comment = reddit.comment(url=fullPermalink)

    #     if comment.banned_by is None:
    #         message.reply('[Your comment](fullPermalink) has already been approved and is visible to everyone.')
    #         userSet.add(authorName)
    #     elif currTime - comment.created_utc > MAX_TIME_ALLOWANCE:
    #         message.reply(SORRY_REPLY)
    #     elif comment.banned_by != BOT_USERNAME:
    #         message.reply(OVERRIDE_UNAVAILABLE_REPLY)
    #         userSet.add(authorName)
    #     elif comment.banned_by == BOT_USERNAME:
    #         print(f'Approving comment {fullPermalink}')
    #         comment.mod.approve()
    #         message.reply('[Your comment](fullPermalink) has been approved. It is now visible to everyone.')
    #         userSet.add(authorName)


# def processReply(userSet, reddit, comment):
#     submission = comment.submission
#     submitterName = submission.author.name

#     if comment.author.name != submitterName:
#         return

#     currTime = time.time()
#     parentComment = comment.parent()
#     SubmissionBannedBy = submission.banned_by
#     permalink = submission.permalink
#     submissionID = submission.id
#     submissionTitle = submission.title

#     recipient = reddit.redditor(submitterName)

#     # if submission is not removed
#     if SubmissionBannedBy is None:
#         recipient.message(subject='Your submission is already approved', message=f'[Your submission](https://reddit.com{permalink}) has already been approved and is visible to everyone.')
#     # if reply is past the MAX_TIME_ALLOWANCE (seconds)
#     elif currTime - submission.created_utc > MAX_TIME_ALLOWANCE + 60:
#         botComment = comment.reply(SORRY_REPLY)
#         botComment.mod.distinguish()
#     elif SubmissionBannedBy != BOT_USERNAME:
#         botComment = comment.reply(OVERRIDE_UNAVAILABLE_REPLY)
#         botComment.mod.distinguish()
#     elif 'has been removed' in parentComment.body and SubmissionBannedBy == BOT_USERNAME:
#         print(f' >>> Approving submission by {submitterName}: {submissionID}: {submissionTitle}')

#         recipient.message(subject='Your /r/Piracy submission has been approved', message=f'Thank you. Your [submission](https://reddit.com{permalink}) is now visible to everyone.')
#         # botComment = comment.reply(f'>{comment.body}\n\nThank you /u/{comment.author.name}. Your submission is now visible to everyone.')
#         # botComment.mod.distinguish()
#         parentComment.edit(f'{REMOVAL_COMMENT}\n\n&nbsp;\n\nEDIT: /u/{submitterName} has replied. This submission is now approved')
#         submission.mod.approve()

#     userSet.add(submitterName)

def processApprovedSubmission(submission):
    maxLength = 65
    title = submission.title
    selftext = submission.selftext
    for str_re in POSSIBLE_RULE3_RE:
        m = re.search(str_re, title, re.IGNORECASE | re.DOTALL)
        if m:
            mGroup = m.group()
            mGroup = mGroup[:maxLength] if len(mGroup) > maxLength else mGroup
            submission.report(f'Possible rule 3? - in_title: [{mGroup}]')
            return
        m = re.search(str_re, selftext, re.IGNORECASE | re.DOTALL)
        if m:
            mGroup = m.group()
            mGroup = mGroup[:maxLength] if len(mGroup) > maxLength else mGroup
            submission.report(f'Possible rule 3? - in_body: [{mGroup}]')


def isUserNew(username, Users):
    if username in Users:
        return False
    return True


# def getUserSet():
#     try:
#         with open(USER_SET_PICKLE_PATH, 'rb') as f:
#             return pickle.load(f)
#     except:
#         userSet = set()
#         with open(USER_SET_PICKLE_PATH, 'wb') as f:
#             pickle.dump(userSet, f)
#         return userSet

def getUsers():
    try:
        with open(USERS_JSON_PATH, 'r', encoding='utf8') as f:
            Users = json.load(f)
        return Users
    except:
        with open(USERS_JSON_PATH, 'w', encoding='utf8') as f:
            json.dump({}, f, indent=4)
        return {}


def getProperDatetime(date_time):
    str_date_time = str(date_time)
    str_hours = re.search(HOURS_DATETIME_RE, str_date_time).groups()[0]
    str_min_sec = re.search(HOURS_DATETIME_RE, str_date_time).groups()[1]

    int_hours = int(str_hours)
    if int_hours > 12:
        int_hours -= 12

    return f'{int_hours}{str_min_sec}'


if __name__ == '__main__':
    print('Welcome Bot has started')
    main()
