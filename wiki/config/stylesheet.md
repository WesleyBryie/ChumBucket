.sidebox.submit:hover:before{position:fixed;display:block;top:0;text-align:center;background-color:#7da5ce;color:white;z-index:1000;padding:5px 0;width:100%;left:0;font-size:32px;font-weight:normal;content:"Before making a post, check the Megathread and wiki listed on the sidebar and use the search bar."}




/* ---------- Wiki button on header ---------- */

#header-bottom-left .tabmenu li a[href$="http://bit.ly/piracywiki"] {
  background: #3498DB;
  border-color: #2980B9;
  font-weight: bold;
  color: #FFF;
}
#header-bottom-left .tabmenu li a[href$="http://bit.ly/piracywiki"]:hover {
  border-color: #0E68A3;
}
#header-bottom-left .tabmenu li a[href$="http://bit.ly/piracywiki"]:before {
  content: " ";
}

/* ---------- Index page new icons ---------- */

.wiki-page.wiki-page-index .wiki-page-content .md.wiki > .toc {
  display: none;
}
.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type {
  list-style: none;
  margin: 0;
  padding: 0;
  max-width: 850px;
}
.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type li {
  display: inline-block;
  height: 120px;
  width: 200px;
  margin-bottom: 14px;
  margin-right: 6px;
}
.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type li a {
  display: block;
  height: 120px;
  width: 200px;
  text-indent: -9999px;
  background-size: 200px 120px!important;
  position: relative;
}
.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type li a:hover:after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255,255,255,0.2);
}

.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type li a[href$="/r/Piracy/wiki/megathread"] {
  background: url(%%megathread%%) no-repeat;
/*  border-bottom: 4px solid #685ac0; */
}
.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type li a[href$="/r/piracy/wiki/megathread_changelog"] {
  background: url(%%changelog%%) no-repeat;
/*  border-bottom: 4px solid #52bda7; */
}
.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type li a[href$="/r/piracy/wiki/faq"] {
  background: url(%%faq%%) no-repeat;
/*  border-bottom: 4px solid #5bc387; */
}
.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type li a[href$="/r/piracy/wiki/guides"] {
  background: url(%%guides%%) no-repeat;
/*  border-bottom: 4px solid #5aa3bb; */
}
.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type li a[href$="/r/piracy/wiki/tools"] {
  background: url(%%tools%%) no-repeat;
/*  border-bottom: 4px solid #c25b5f; */
}
.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type li a[href$="https://discord.gg/GDr46dF"] {
  background: url(%%discord%%) no-repeat;
/*  border-bottom: 4px solid #5985be; */
}

/* ------- Placeholder for r/Piracyfuture categories ------- */

/*.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type li a[href$="/resources"] {
  background: url(%%wiki-res%%) no-repeat;
  border-bottom: 4px solid #d17d54; 
} */
/*.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type li a[href$="/rules"] {
  background: url(%%wiki-use%%) no-repeat;
  border-bottom: 4px solid #5268c6; 
} */
/*.wiki-page.wiki-page-index .wiki-page-content .md.wiki > ul:first-of-type li a[href$="/glossary"] {
  background: url(%%wiki-glo2%%) no-repeat;
  border-bottom: 4px solid #57c0bd; 
} */

/*----------- Flair sidebar table --------------------------- */

.side table {
    width: 260px;
    border: none !important;
    margin-left: 0px;
}

.side table th {
        display: none;
}

.side table tr {
    /*text-align: center;*/
    /*border: none !important;*/
}

.side table td {
    /*text-align: center;*/
    border: none !important;
    padding: 4px 0;
}

.side table td a {
    background: #aaa;
    width: 100px;
    color: #fff;
    display: inline-block;
    margin-left: 14px;
    padding: 4px 0;
    padding-left: 23px;
    position: relative;
    left: 0;
    top: 0;
    transition: background 2s;
    -webkit-transition: background 2s;
    -moz-transition: background 2s;
    -o-transition: background 2s;
}

.side table td a:hover {
    text-decoration: none;
    /*padding-left: 25px;*/
    /*width: 78px;*/
    /*background: #ccc !important;*/
}

/* PSA flair */
.side table td a[href$="http://bit.ly/PSA_flair"] {
    background-color: #f8a5a5;
    color:#000000!important;
}
.side table td a[href$="http://bit.ly/PSA_flair"]:before {
    background-position: 3px 4px;
}
/* Humor flair */
.side table td a[href$="http://bit.ly/Humor_flair"] {
    background-color: #f2cea3;
    color:#000000!important;
}
.side table td a[href$="http://bit.ly/Humor_flair"]:before {
}
/* News flair */
.side table td a[href$="http://bit.ly/News_flair"] {
    background-color: #EFE096;
    color:#000000!important;
}
.side table td a[href$="http://bit.ly/News_flair"]:before {
}

/* Meta flair */
.side table td a[href$="http://bit.ly/meta_flair"] {
    background-color: #8dda8a;
    color:#000000!important;
}
.side table td a[href$="http://bit.ly/meta_flair"]:before {
}
/* weekly thread flair */
.side table td a[href$="http://bit.ly/weekly_new"] {
    background-color: #0ad76c;
        color:#000000!important;
}
.side table td a[href$="http://bit.ly/weekly_new"]:before {

    background-position: 4px 6px;
    background-size: 12px;
}

/*
.side table td a[href$="Energy"] {
    background-color: #BBDF98;
}

.side table td a[href$="Energy"]:before {
;
}

.side table td a[href$="Nanotech"] {
    background-color: #b3e6b1;
}

.side table td a[href$="Nanotech"]:before {

}
*/

/* Guide flair */
.side table td a[href$="http://bit.ly/Guide_flair"] {
    background-color: #A4DFD0;
    color:#000000!important;
}

.side table td a[href$="http://bit.ly/Guide_flair"]:before {
}

/* Question flair */
.side table td a[href$="http://bit.ly/Question_flair"] {
    background-color: #71a9f7;
    color:#000000!important;
}

.side table td a[href$="http://bit.ly/Question_flair"]:before {

}
/* Release flair */
.side table td a[href$="http://bit.ly/release_flair"] {
    background-color: #ffacec;
    color:#000000!important;
}

.side table td a[href$="http://bit.ly/release_flair"]:before {

}
/* Discussion flair */
.side table td a[href$="http://bit.ly/discussion_flair"] {
    background-color: #c9b5f0;
    color:#000000!important;
}

.side table td a[href$="http://bit.ly/discussion_flair"]:before {

}

/*.side table td a[href$="Space"] {
    background-color: #babcef;
}

.side table td a[href$="Space"]:before {

}

.side table td a[href$="Wireless"] {
    background-color: #c9b5f0;
}

.side table td a[href$="Wireless"]:before {

    background-position: 3px 6px;
}

.side table td a[href$="AI"] {
    background-color: #d8b1ea;
}

.side table td a[href$="AI"]:before {

}

*/


#header{height:165px;background:#4a5f7b;border-bottom:none}#header #header-bottom-right #mail.havemail,#header #modmail.havemail,.comments-page.linkflair-bug .flat-list a.flairselectbtn:after,.comments-page.linkflair-help .flat-list a.flairselectbtn:after{animation:1s ease-out 0s normal none infinite running pulsate;animation-duration:2s;animation-timing-function:ease-out;animation-delay:0s;animation-direction:normal;animation-fill-mode:none;animation-iteration-count:infinite;animation-play-state:running;animation-name:pulsate}#header-bottom-left{height:140px}#header-bottom-left .tabmenu{background:rgba(0,0,0,.2);width:calc(100% - 50px);padding-left:50px;position:absolute;bottom:0;left:0;font-family:"Segoe UI",Helvetica,sans-serif;transition:.5s}#header-bottom-left .tabmenu li{font-weight:400;margin:0}#header-bottom-left .tabmenu li a{background:0;color:#ddd;border-bottom:2px solid transparent;font-size:11.4px;font-family:"Segoe UI",Helvetica,sans-serif;line-height:30px;padding:8px 9px 6px;letter-spacing:.1em;text-transform:uppercase;transition:.15s ease-in-out}#header-bottom-left .tabmenu li a:hover{color:#fff;background:#259eff;border-bottom:2px solid #fff!important}#header-bottom-left .tabmenu li.selected a{background-color:#259eff;border:0;color:#fff;font-weight:700;border-bottom:2px solid currentColor!important}#header-img{text-indent:-9999px;display:inline-block;margin-top:110px;position:absolute;z-index:99;height:27px;width:27px;margin-left:4px;padding:2px 11px 0 8px;opacity:.8;background-repeat:no-repeat!important;transition:.15s ease-in-out;border-bottom:2px solid transparent!important}#header-img:hover{opacity:1;background:#259eff;font-weight:500;border-bottom:2px solid #fff!important}#header .hover a:hover,.redditname a:hover:after{color:#fff!important}#header-bottom-right #modmail,#header-bottom-right .user{height:37px;white-space:nowrap;border-radius:1px;overflow:hidden;transition:.5s}#sr-header-area{transition:opacity .3s;opacity:.4;height:24px;background-color:#0c1722;border-bottom:0;letter-spacing:1px;line-height:22px}#sr-header-area .srdrop.dropdown .selected:hover,#sr-header-area:hover{opacity:1}#sr-header-area a{color:#c4c4c4;font-family:"Segoe UI",Helvetica,sans-serif}#sr-header-area .srdrop.dropdown{width:35px;padding:0}#sr-header-area .srdrop.dropdown .selected{width:35px;height:23px;padding:0;margin:0;display:block;background:url(%%spritesheet%%) -225px -252px no-repeat;line-height:35px;text-indent:-999em}#sr-header-area .sr-list{padding-left:8px;border-left:2px solid rgba(196,196,196,.9);height:24px;line-height:25px}#sr-header-area .drop-choices.srdrop{padding:5px;margin:1px 0 0;background:#222;border:none}#sr-header-area .drop-choices a.choice{color:#aeaeae}#sr-header-area .drop-choices a.choice:hover{background-color:#333;color:#eee}#sr-header-area .drop-choices .choice.bottom-option{border-color:#aeaeae}#header [href$="/ads/"],#header [href$="/controversial/"],#header [href$="/rising/"],#sr-more-link,#suggested-reddits,.rank,.submit-page .content h1,.titlebox .bottom,.voteWeight,a[href*='#/RES_SR_Config/NightModeCompatible'],a[href*='#icon']+.keyNavAnnotation{display:none!important}#url-field button,.submit-page .content button[name=submit]{background:0 0;transition:all .5s;border:1px solid #5cb85c;color:#5cb85c}#url-field button:hover,.submit-page .content button[name=submit]:hover,button.save:hover,button.submit-action-thing:hover,button.submit-report:hover{background:#5cb85c;color:#fff}.submit-page .tabmenu.formtab{margin-bottom:74px}.submit_text p{color:#eee}.commentarea .infobar p:hover,.submit_text.roundfield.enabled{background:#529dff}button.cancel,button.cancel-action-thing,button.cancel-report-thing,button.save,button.submit-action-thing,button.submit-report{background:0 0;transition:.5s;text-transform:capitalize;font-family:"Segoe UI",Helvetica,sans-serif;border:1px solid #5cb85c;color:#5cb85c;padding:.25rem .75rem}button.cancel,button.cancel-action-thing,button.cancel-report-thing{border:1px solid #d9534f;color:#d9534f}button.cancel-action-thing:hover,button.cancel-report-thing:hover,button.cancel:hover{background:#d9534f;color:#fff}.next-suggestions a{padding:0 4px;color:#259eff}.next-suggestions a,.nextprev a{background:0 0;border:none;text-align:center}.next-suggestions a:hover,.nextprev a:hover{background:#259eff;border:none;color:#fff;outline:0}#header #header-bottom-right #mail.havemail:active,#header #header-bottom-right #mail.nohavemail:active,#header #header-bottom-right .choice:active,#header #header-bottom-right .logout a:active,#header-bottom-left .tabmenu li a:active,#header-bottom-right #modmail:active,#header-bottom-right .user:active,.btn:active,.gadget .right a:active,.morelink a:active,.sidecontentbox a.helplink:active,button:active{background-color:#1686f0!important}.comment{position:relative;padding:4px 0 0 30px;z-index:1;border:2px solid #e6e6e6;overflow:hidden;margin:0 18px 8px 0}.comment .expand{transition:all .5s;position:absolute;top:0;left:0;bottom:0;padding:4px}.comment .expand:hover{background:#259eff;color:#fff!important;text-decoration:none}.comment.collapsed .tagline{height:21px;line-height:21px}.comment.collapsed .tagline a{line-height:13px}.comment .child,.comment .showreplies{border-left:none}.new-comment{border-color:#ffab91!important}.new-comment .expand:hover{background:#ffab91}.new-comment .usertext-body{background-color:transparent;border:none}.comment.gilded,.res-commentBoxes .commentarea .comment.gilded{border-color:#e2c737}.comment.gilded>.entry .expand:hover{background-color:#e2c737}.gilded.link{border-left-color:gold!important;background:#fffdf3}.tagline .score{font-weight:700}.entry .flat-list .reply-button a,.tagline .likes{color:#3b4c62}.tagline .submitter{color:#529dff}.tagline .stickied-tagline{color:#00a64f}.tagline a:hover{color:#259eff}.link .domain{visibility:hidden}.link .domain a{visibility:visible;position:relative;top:-1px;color:#b1b1b1}.domain{display:inline-block!important}#siteTable_organic{background:rgba(6,102,178,.1);margin-right:325px;margin-top:-7px;left:-5px;border-left:3px solid #ff4500;border-right:1px solid #e5e5e5;border-bottom:none;border-top:none}#ad_sponsorship{max-width:295px}.organic-listing .link.promotedlink{margin-left:-1px;border-bottom:1px solid #e5e5e5}.flairselector{border:1px solid #3b4c62!important}.flairselector .title{font-size:0!important}.flairselector .linkflair{border-left:none!important;background:0 0;width:110px}.flairselector h2{color:#fff;font-size:13px;background:#3b4c62!important;padding-top:6px;font-weight:lighter!important;text-transform:capitalize;padding-bottom:6px}.flairselector li:hover{background-color:transparent}.flairselector form{border-top:solid 1px #3b4c62;margin-bottom:10px}.flairselector.drop-choices.active{left:45%!important;margin-top:-172px;position:absolute;padding:0!important;box-shadow:none}.comments-page .flairselector.drop-choices.active{top:50%!important;left:50%!important;transform:translate(-50%,-50%)}.flairoptionpane{max-height:600px}.flairoptionpane li,.flairoptionpane ul{min-width:120px;padding:3px}.nextprev a,.side .usertext-body .md ol a{transition:background-color .5s}.submit-page .roundfield{padding:16px;width:525px;background-color:#fff;border:1px solid #e5e5e5;border-radius:0}.submit-page .roundfield span.title{color:#4d5763;text-transform:capitalize}.submit-page .submit.content#newlink .tabmenu.formtab a{padding:16px;display:inline-block;text-align:center;background-color:#fff;color:#4d5763;text-transform:uppercase;font-weight:700;transition:all .25s ease;font-size:16px;border:none;width:247.5px}.submit-page .submit.content#newlink .tabmenu.formtab a:hover{background-color:#e7e9f6}.submit-page .submit.content#newlink .tabmenu.formtab .selected a{font-size:16px;background-color:#3b4c62;color:#fff}#header #header-bottom-right #modmail:hover,.submit-page .submit.content#newlink .tabmenu.formtab .selected a:hover{background-color:#259eff}.submit-page #newlink.submit.content .btn{width:558px;height:auto;text-transform:capitalize;font-size:17px;padding:16px;text-align:center}.submit-page #newlink.submit.content .btn:after{content:" your thread";text-transform:none}.formtabs-content{width:520px;border-top:none;margin-top:-15px}.formtabs-content .infobar{background-color:#529dff;color:#fff;padding:15px;border:none;margin:-69px 0 -5px;font-size:14px;width:529px}form .spacer+.spacer{margin:0}.content.submit .info-notice{background-color:#fff;border-radius:2px;padding:16px;margin-bottom:0;border:1px solid #e5e5e5!important}.self .expanded~.expando .usertext-body{-webkit-animation:700ms expandy ease-in-out forwards;animation:700ms expandy ease-in-out forwards}@-webkit-keyframes expandy{0%{-webkit-transform:translateY(-100px);opacity:0}50%{-webkit-transform:translateY(0)}to{-webkit-transform:translateY(0);opacity:1}}@keyframes expandy{0%{transform:translateY(-100px);opacity:0}50%{transform:translateY(0)}to{transform:translateY(0);opacity:1}}.expando-button{cursor:pointer;float:left;height:28px;width:30px}.expando-button.selftext.collapsed,.expando-button.selftext.collapsed:hover,.expando-button.selftext.expanded,.expando-button.selftext.expanded:hover{background-image:url(%%spritesheet%%);background-repeat:no-repeat}.expando-button.selftext.collapsed{background-position:-195px -256px}.expando-button.selftext.collapsed:hover{background-position:-155px -256px}.expando-button.selftext.expanded{background-position:-265px -218px}.expando-button.selftext.expanded:hover{background-position:-305px -218px}.expando-button.video.collapsed,.expando-button.video.collapsed:hover,.expando-button.video.expanded{background-image:url(%%spritesheet%%)!important}.expando-button.video.collapsed{background-position:-301px -256px}.expando-button.video.collapsed:hover{background-position:-261px -256px}.expando-button.video.expanded{background-position:-265px -218px}.expando-button.video.expanded:hover{background-image:url(%%spritesheet%%);background-repeat:no-repeat;background-position:-305px -218px}.expando-button.image{cursor:pointer;display:inline-block;height:28px!important;margin-right:11px;padding:0;vertical-align:top!important;width:30px!important}@media only screen and (min-resolution:2dppx),only screen and (-webkit-min-device-pixel-ratio:2){.expando-button{cursor:pointer;float:left;height:28px;width:30px;background:center center no-repeat #fff;background-size:341px 331px!important}.expando-button.selftext.collapsed,.expando-button.selftext.collapsed:hover,.expando-button.selftext.expanded,.expando-button.selftext.expanded:hover{background-image:url(%%spritesheet%%);background-repeat:no-repeat}.expando-button.selftext.collapsed{background-position:-195px -256px}.expando-button.selftext.collapsed:hover{background-position:-155px -256px}.expando-button.selftext.expanded{background-position:-265px -218px}.expando-button.selftext.expanded:hover{background-position:-305px -218px}.expando-button.video.collapsed,.expando-button.video.collapsed:hover,.expando-button.video.expanded{background-image:url(%%spritesheet%%)!important}.expando-button.video.collapsed{background-position:-301px -256px}.expando-button.video.collapsed:hover{background-position:-261px -256px}.expando-button.video.expanded{background-position:-265px -218px}.expando-button.video.expanded:hover{background-image:url(%%spritesheet%%);background-repeat:no-repeat;background-position:-305px -218px}.expando-button.image{cursor:pointer;display:inline-block;height:28px!important;margin-right:11px;padding:0;vertical-align:top!important;width:30px!important}body>.content #siteTable .thing.self .thumbnail{background-image:url(%%spritesheet%%);background-position:-289px -139px;background-size:341px 331px}}.link .usertext-body .md{border-radius:0!important;border:1px solid #ccd4e8;background-color:#fff}body>.content #siteTable .thing.self .thumbnail{background-image:url(%%spritesheet%%);width:45px;height:45px;margin:10px 15px 10px 10px;background-repeat:no-repeat!important;background-position:-289px -139px}body>.content #siteTable .thing.stickied .thumbnail{background-image:url(%%spritesheet%%);background-repeat:no-repeat!important;background-position:-289px -84px;margin-right:15px}body>.content #siteTable .thing .thumbnail.default,body>.content #siteTable .thing.over18 .thumbnail{background-image:url(%%spritesheet%%)!important;background-repeat:no-repeat!important;margin:10px 15px 10px 10px;width:45px;height:45px}body>.content #siteTable .thing.stickied .entry>.title .title{color:#00a64f;font-weight:400}body>.content #siteTable .thing.over18 .thumbnail{background-position:-286px -5px!important}body>.content #siteTable .thing .thumbnail.default{background-position:-47px -77px;background-size:341px 331px}.link .title,.submit-page #newlink.submit.content .btn,a[href*="#icon-more"]{font-family:"Segoe UI",Helvetica,sans-serif}.link{padding:10px 0;border-left:3px solid #cec0c0;margin-bottom:0;border-bottom:1px solid #e5e5e5}.link .title,.newComments{color:#3b4c62}.link .title:visited{color:#b1b1b1}.link.thing.visited .title{color:#b1b1b1;padding:0!important}.link.last-clicked{border:0;border-left:3px solid #259eff;background:#f8fcff}.link .score.likes{color:#259eff}.link .score.dislikes{color:#7f7f7f}.link .flair{font-size:1em}.link .midcol{margin:5px 7px}.nextprev a{padding:5px 0 5px 15px;color:#fff;width:auto;display:block;background:#3b4c62;border-radius:0;font-size:small;margin-top:-12px;margin-right:-1px;margin-left:-5px;text-transform:capitalize}.report-reasons.rounded{display:block!important}.newComments{display:inline}.linkinfo .totalvotes{color:#494949!important}.arrow{background-image:url(%%spritesheet%%)!important;background-position:center center;outline:0!important;border:none!important}.arrow.up{background-position:-289px -194px}.arrow.upmod{background-position:-296px -60px}.arrow.down{background-position:-321px -60px}.arrow.downmod{background-position:-271px -60px}.arrow.down:hover,.arrow.up:hover{opacity:.6}.arrow.up:active,.arrow.upmod:active{transform:translate(0,-1px)}.arrow.down:active,.arrow.downmod:active{transform:translate(0,1px)}.linklisting{margin-right:330px;bottom:0;margin-top:-7px;padding:0;border-right:1px solid #e5e5e5}.linklisting .nextprev,.sidecontentbox .helplink+.title h1{font-size:0}.linklisting .stickied{border-left:3px solid #00a64f!important;background:#f8fffb!important}.linklisting .over18,.linklisting .reported{background:rgba(226,6,44,.1);border-left:3px solid #e2062c}.linklisting .md{margin-bottom:0}.linklisting .usertext-edit div textarea{margin-left:-10px}.entry .buttons li a{padding:0;font-size:1.145em}.search-result-meta,.tagline{font-size:1.145em}#siteTable .thing{margin-left:-5px!important;transition:all .2s}.listing-page .link:hover{border-left-color:#259eff;background:#f9fafc}.entry .flat-list .report-button a,.res-nightmode .entry .flat-list .report-button a{color:#d9534f}.reddit-infobar{background:#fff;BORDER:1px solid #e6edf6}.reddit-infobar.with-icon{margin-left:-4px}.reddit-infobar.with-icon:before{background-color:solid #3b4c62;background-repeat:no-repeat}.c-btn-primary{background-color:solid #3b4c62;border-bottom:2px solid #4270a2;color:#fff;border-radius:0}.sitetable .comment,.sitetable .comment .comment .comment,.sitetable .comment .comment .comment .comment .comment,.sitetable .comment .comment .comment .comment .comment .comment .comment,.sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment,.sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,.sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,.sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment{background-color:#fff!important}.sitetable .comment .comment,.sitetable .comment .comment .comment .comment,.sitetable .comment .comment .comment .comment .comment .comment,.sitetable .comment .comment .comment .comment .comment .comment .comment .comment,.sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,.sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,.sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,.sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment{background-color:#fff!important}a.author{margin-right:.3em}.panestack-title{margin:0 330px 0 -5px;padding:4px 0;background:#3b4c62;color:#fff}.panestack-title .title{font-size:1.3em;margin:10px 0 10px 10px}.panestack-title a.title-button,thead th a{color:#fff!important}.panestack-title a.title-button.gold{background-color:transparent;border:none}.thing.stickied a.title{font-weight:700!important;font-size:large}.green,.tagline .moderator{color:#00a64f;font-weight:700;padding-left:0;padding-right:1px}.comment .moderator~.userattrs:after{position:absolute;border:3px solid #00a64f;top:-.7px;right:-1px;bottom:-1px;left:-1px;content:'';opacity:.5;z-index:-1}.stickied.comment .moderator~.userattrs:after{border:0}.stickied.comment .expand:hover{background:#01a64f}.entry .flat-list .approve-button a{color:#00a64f}.gold-accent{background-color:#3b4c62;border:none;display:inline-block;color:#fff!important}#noresults{padding:10px;margin-right:310px!important;color:#fff;background:#3b4c62;margin-left:5px!important;display:none}.comments-page .sitetable.nestedlisting>.thing.stickied{background:#f8fffb!important;border-color:rgba(0,166,79,.1);border-bottom:solid 3px #00a64f}.comments-page .link .flat-list a.flairselectbtn{color:#3b4c62!important}.comments-page .usertext-edit div textarea{border:1px solid #000!important;opacity:.8;margin-top:5px;outline:0;display:block;clear:both;margin-bottom:10px;background:url(%%piracylogo%%) 206px -240px no-repeat #fff!important}.comments-page .usertext-edit div textarea:focus{background:#fff!important;opacity:1;border-color:#259eff!important}.comments-page .link{border-left:1px solid #c6c6c6!important}.comments-page:not(.comment-permalink-page) .sitetable .comment{-webkit-animation:fade-in-bottom .6s cubic-bezier(.39,.575,.565,1) both;-moz-animation:fade-in-bottom .6s cubic-bezier(.39,.575,.565,1) both;animation:fade-in-bottom .6s cubic-bezier(.39,.575,.565,1) both}@-webkit-keyframes fade-in-bottom{0%{-webkit-transform:translateY(50px);transform:translateY(50px);opacity:0}to{-webkit-transform:translateY(0);transform:translateY(0);opacity:1}}@keyframes fade-in-bottom{0%{-webkit-transform:translateY(50px);transform:translateY(50px);opacity:0}to{-webkit-transform:translateY(0);transform:translateY(0);opacity:1}}.commentarea .menuarea{margin:5px 310px 5px 5px}.commentarea .md{margin-bottom:0}.commentarea .infobar{display:flex;justify-content:space-between;color:#eee;background:#3b4c62;border:0}.commentarea .infobar a{color:#eee}.commentarea .infobar p{background:#259eff;padding:10px;margin:-5px -10px -5px 10px;line-height:8px;-webkit-transition:all .25s;-o-transition:all .25s;transition:all .25s}.commentarea .infobar.infobar.commentsignupbar{display:block;background:0 0}.commentarea .infobar.infobar.commentsignupbar .commentsignupbar__desc{background:0 0}.md{overflow:visible}.md a{color:#bf0426}.helplink~.content .author .helplink~.content .author:hover,.md a:hover{color:#259eff}.md code{white-space:normal}.md blockquote{border:1px solid rgba(36,156,255,.1);border-left:2px solid #259eff;background-color:#efefed}.usertext.border .usertext-body{background-color:rgba(0,120,213,.3);width:95%}.wiki-page .pageactions{border-radius:0;border:1px solid #259eff}.wiki-page .pageactions .wikiaction{margin:0!important;border-radius:0!important}.wiki-page .pageactions .wikiaction:hover{background-color:#259eff!important;color:#fff!important}.wiki-page .pageactions .wikiaction-current,div.titlebox span.fancy-toggle-button a.active.add:hover,div.titlebox span.fancy-toggle-button a.active.remove{background-color:#3b4c62}.wiki-page .pageactions .wiki-page-content .nextprev a{margin-bottom:12px}ul.tabmenu.formtab{padding-left:0}::selection{background-color:#259eff;color:#fff}.buttons .comments.empty{color:#3b4c62}.gadget .right a,a[href*="#tech"]{font-family:"Segoe UI",Helvetica,sans-serif;text-align:center}.sheets ::-webkit-scrollbar{background-color:#0f0f0f!important}.sheets ::-webkit-scrollbar-corner,.sheets ::-webkit-scrollbar-thumb{background:#313131!important}.sheets .col textarea{width:98%;background:#1d1f21;color:#ddd!important;height:712px!important;font-family:SourceCodePro-Medium,monospace}.panestack-title{border-bottom:transparent}.infobar.newsletterbar{box-sizing:border-box;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;position:relative;overflow:hidden;min-height:80px;padding:15px 20px 20px 25px;border:none;border-radius:0;background-color:#30659b;border-left:3px solid #ff4500;margin:-7px 325px 7px 0;left:-5px}#eu-cookie-policy .reddit-infobar a{color:#222!important}.gadget .midcol{margin-right:9px}.gadget .right a{background:#3b4c62;padding:5px 10px;margin-right:5px;display:block;color:#fff;font-size:16px;transition:background-color .5s;text-transform:capitalize}.gadget .right a:hover{background:#259eff}span.clear-input-button,thead th{color:#fff}#newlink-with-image-upload .clear-input-button{border-radius:0!important;width:33px!important;height:27px!important;top:0!important;line-height:26px!important;border:1px solid gray;background:#3b4c62!important;transition:background-color .5s;right:-10px!important}#newlink-with-image-upload .clear-input-button:hover{background:#259eff!important}#newlink-with-image-upload .image-upload-drop-target{padding:15px!important}#newlink-with-image-upload .file-upload-button{background:#3b4c62;border:none;padding:7px 20px!important;display:block!important;margin:6px -17px -17px!important;transition:background-color .5s}#newlink-with-image-upload .file-upload-button:hover{background:#259eff}thead th{background:#3b4c62;border:none!important}thead th:nth-child(2n){background:#259eff}tr:nth-child(even){background-color:#fff}.drop-choices{border-color:#e8e8e8}.drop-choices a.choice{border-bottom:1px solid #e8e8e8;padding:3px 6px}@media (max-width:880px){#siteTable_organic{margin-right:-5px}#header-bottom-left .tabmenu{width:calc(100% - 50px);padding-left:50px}.side{display:none}body .linklisting{margin-right:0!important}.footer::after{display:none!important}.infobar{margin-right:18px}.footer{border-right:1px solid #3b4c62}.panestack-title{margin:0 0 0 -5px}.infobar.newsletterbar{margin:-7px -5px 7px 0}}.submitter:after{content:"";position:absolute;top:-.7px;right:-1px;bottom:-1px;left:-1px;text-align:right;padding:.25em .5em;border:3px solid #8bb9e2;pointer-events:none}body:lang(np):not(.subscriber) .arrow{pointer-events:none}#header-bottom-right #modmail,a[href*="#icon-day"]{display:none}#chat,.pinnable-content .thing{border-bottom:0}.pinnable-content.pinned{background-color:rgba(248,248,248,.95)!important}.expando-button.collapsed.crosspost,.expando-button.collapsed.crosspost:hover{width:20px!important}#chat{position:absolute;margin-left:-26.65em;top:.8em;padding:1.34em;background:url(%%redditchat%%) 5px no-repeat #2d4059;border:.2em solid #fff;-webkit-transition:.5s;-o-transition:.5s;transition:.5s}#chat:hover,#header #header-bottom-right #modmail:hover{background-color:#47658c}#chat:active{background:url(%%redditchat%%) 5px no-repeat #ea5455}.side{margin:0;padding-left:30px;background:0 0}.side:after{content:" ";font-size:large;color:#2d4059;margin-left:1.5em}.sidee .md h2{margin-top:1.4em}.side .md h3{margin:2em 0 .2em}.side .md h4{margin-bottom:1.5em}.side .md p{margin:.5em 0}.side .md p a{margin:0 .2em;font-size:1.1em}.side .md p a:first-child{margin-left:0}.side .md h1{font-weight:400}.morelink a,.side .md h2,.side .md h3,.side .md h4{color:#fff;font-size:13px;font-weight:400}.side .md h1:after,.side .md h2:after,.side .md h3:after,.side .md h4:after,.sidecontentbox .title:after,.titlebox h1:after{display:block;position:absolute;z-index:-1;border-color:transparent #e6edf6 transparent transparent;border-width:10px;border-style:solid;content:"";margin-left:-24px}.side .md h1,.side .md h1 a,.side .md h2 a,.side .md h3 a,.side .md h4 a{color:#fff;font-size:13px}.side .titlebox div.subButtons,.side .titlebox h1.redditname+div,.side .titlebox>.fancy-toggle-button{padding:5px 10px;border:1px solid #e6edf6;border-left:5px solid #e6edf6;border-right:1px solid #e6edf6;border-top:none;border-bottom:none;border-radius:0;background-color:#fff;color:#000;font-size:8pt;font-weight:400;margin:0 5px 0 0}.side .titlebox>.fancy-toggle-button{display:block!important;width:269.3px}.side .titlebox div.subButtons{width:269.3px}.side div.titlebox ul{list-style-type:none;margin:0;padding:0}.side .subscribe-button .add{animation:1s ease-out 0s normal none infinite running pulsate;animation-duration:2s;animation-timing-function:ease-out;animation-delay:0s;animation-direction:normal;animation-fill-mode:none;animation-iteration-count:infinite;animation-play-state:running;animation-name:pulsate}@-webkit-keyframes pulsate{0%,to{opacity:.7}50%{opacity:1}}@-moz-keyframes pulsate{0%,to{opacity:.7}50%{opacity:1}}@keyframes pulsate{0%,to{opacity:.7}50%{opacity:1}}div.side div.tagline{display:block!important;padding:0 10px 10px;border-top:none!important}div.side div.tagline,div.side form.flairtoggle,div.side form.leavecontributor-button,div.side span.subscribers{border:1px solid #e6edf6;border-left:5px solid #e6edf6;border-right:1px solid #e6edf6;border-radius:0;background-color:#fff;color:#000;font-size:.945em;font-weight:400;margin:0 5px 0 0}div.side form.leavecontributor-button,div.side span.subscribers{padding:10px}div.side span.subscribers{padding:5px 10px 10px;border-top:none;display:block}div.side span.subscribers span{vertical-align:middle}div.side span.subscribers span.number:before{background:url(%%spritesheet%%) -192px -5px;display:block;float:left;width:20px;height:20px;content:"";margin-right:5px;margin-top:-3px}div.side form.flairtoggle{display:block;padding:5px 10px;border-top:none;border-bottom:none}div.side p.users-online{padding-top:5px;padding-bottom:5px;border-top:none;border-bottom:none}.morelink{border:1px solid #3b4c62;background:#3b4c62;width:145px;margin-right:5px;transition:all .5s;box-sizing:border-box}.morelink a{font-family:"Segoe UI",Helvetica,sans-serif;letter-spacing:0;font-size:.9em}.morelink:hover{background:#259eff;border-color:#259eff}.morelink:hover a{color:#fff;border-color:#259eff}.helplink~.content .author[href*=AutoModerator],.helplink~.content .author[href*=flair_your_post_bot],.morelink .nub{display:none}.submit .morelink{float:left}.submit-page .titlebox h1{margin-top:0!important}.redditname{margin-top:53px!important}.icon-menu li,.reddit-link{border-left:5px solid #e6edf6;background-color:#fff;border-bottom:1px solid #e6edf6;border-right:1px solid #e6edf6}.reddit-link{font-size:1em;padding:7px 10px 10px;margin-right:5px}.icon-menu li{display:block;margin:0;padding:7px 10px 10px!important;margin-right:5px!important}.search-page .side .spacer{margin:10px 0}.sidebox.create{display:none!important}.helplink~.content .author:after{content:'- Moderator';margin-left:5px}.helplink~.content .flair,.sidecontentbox .content .linkflairlabel{display:none}.linkinfo{background-color:transparent}.sidecontentbox .helplink+.title h1:before{font-size:13px!important;content:"Moderators team";text-transform:capitalize}div.titlebox .md h3:hover+ul{display:block;transition:.8s max-height ease-out}div.titlebox .md ul li strong:first-child,div.titlebox .md ul:hover{display:block}.sidecontentbox .content a.author,.sidecontentbox .more,div.titlebox .md ul li{background-color:#fff;border-left:5px solid #e6edf6;border-bottom:1px solid #e6edf6;border-right:1px solid #e6edf6;font-size:.945em}div.titlebox .md ul li{padding:7px 10px 10px;transition:.2s;margin-right:5px}.sidecontentbox .content a.author,.sidecontentbox .more{margin-right:5px!important}.sidecontentbox .more{display:block;padding:7px 10px 10px!important;margin:0}.sidecontentbox .content a.author:hover,.sidecontentbox .more:hover{background-color:#f8fcff;border-left-color:#ccd4e8}.sidecontentbox .content{border:none;padding:0}.sidecontentbox .more{text-align:center}.sidecontentbox .more a{color:#369}.sidecontentbox .title{background-color:#3b4c62;padding:10px;border-left:5px solid #529dff;margin-top:0;margin-bottom:0;margin-left:-10px;font-weight:400}.sidecontentbox a.helplink{display:block;background:#3b4c62;margin-right:5px;margin-bottom:10px;float:none;margin-top:4px;clear:both;text-align:center;box-sizing:border-box;color:#fff}.sidecontentbox a.helplink:hover{background:#259eff}.sidecontentbox .title h1{color:#fff}.icon-menu li:hover,.reddit-link:hover,div.titlebox .md ul li:hover{background-color:#f8fcff;border-left-color:#ccd4e8}div.titlebox .md h3:before{content:"+";color:#fff;padding-right:5px}div.titlebox .md h2,div.titlebox .md h3,div.titlebox .md h4{margin-bottom:0;font-weight:400;cursor:default}.date:before,div.titlebox .md h2,div.titlebox .md h3,div.titlebox .md h4,div.titlebox h1{border-left:5px solid #529dff;background-color:#3b4c62;padding:10px;margin-top:0;margin-left:-10px}div.titlebox h1{font-weight:400;font-size:13px;margin-bottom:0}div.titlebox div.styleToggle,div.titlebox span.fancy-toggle-button a.active{padding:5px 10px;color:#fff;font-size:8pt;display:block!important;background-image:none;border-radius:0;font-weight:400;margin:0;border:none}div.titlebox div.styleToggle{line-height:20px;background-color:#3b4c62}div.titlebox span.fancy-toggle-button a.active{background-color:#259eff}div.titlebox div.styleToggle input,div.titlebox div.styleToggle label{vertical-align:middle;margin:0}div.titlebox span.fancy-toggle-button a.active.remove:before{content:"";padding-right:5px}div.titlebox span.fancy-toggle-button a.active.remove:hover:after{content:"=(";font-style:italic;padding-left:5px}div.titlebox span.fancy-toggle-button a.active.add:before{content:"+";padding-right:5px;color:#fff}#RESShortcutsAdd,#RESShortcutsLeft,#RESShortcutsRight,#RESShortcutsSort,#RESShortcutsTrash{width:17px!important}#RESShortcutsAdd,#RESShortcutsEditContainer,#RESShortcutsLeft,#RESShortcutsRight,#RESShortcutsSort,#RESShortcutsTrash{background-color:transparent!important}#RESShortcutsAdd:hover,#RESShortcutsEditContainer:hover,#RESShortcutsLeft:hover,#RESShortcutsRight:hover,#RESShortcutsSort:hover,#RESShortcutsTrash:hover{color:#f0f0f0!important}.sidecontentbox .content a.author{display:block;margin:0;padding:7px 10px 10px!important}.sidecontentbox .content a.author:hover{color:#259eff}#search input[type=text]{width:295px!important;border-color:#3b4c62}#searchexpando{padding:10px;border:1px solid #e6edf6;border-right:1px solid #e6edf6;background-color:#fff;color:#000;font-size:8pt;border-radius:0;font-weight:400;margin:0 5px 0 0;width:273px!important;border-left:1px solid #e6edf6}#header-bottom-right .separator,.leavecontributor-button,.leavemoderator{display:none}.icon-menu a{background:0 0}.linkinfo,.titlebox .bottom{border:none}#header-bottom-right .user span a,.pagename a,.titlebox h1 a{color:#fff}.titlebox .md h3+ul:hover,.titlebox .md h3:hover+ul{max-height:600px;transition-delay:0s}div.titlebox .md h3+ul{display:block;transition:1.8s max-height ease-out;overflow:hidden;max-height:0;transition-delay:2s}.linkinfo{padding:0}.linkinfo .score,.linkinfo .shortlink{color:#494949;border-left:5px solid #e6edf6;background-color:#fff;border-bottom:1px solid #e6edf6;border-right:1px solid #e6edf6;font-size:8pt;margin-right:5px}.linkinfo .score{padding:7px 10px;margin-top:10px}.linkinfo .shortlink{display:block;font-weight:600;text-transform:capitalize;margin-top:0;padding:7px 10px 10px}.date{position:relative}.date:before{content:"Date ";display:block;color:#fff!important;text-transform:none;cursor:pointer;margin-bottom:6px;font:400 small verdana,arial,helvetica,sans-serif}.date:after{display:block;position:absolute;z-index:-1;border-color:transparent #e6edf6 transparent transparent;border-width:10px;border-style:solid;content:"";margin-left:-19px;margin-top:-32px}.date span,.totalvotes{display:block;background-color:#fff;border-left:5px solid #e6edf6;border-bottom:1px solid #e6edf6;border-right:1px solid #e6edf6}.date span,.date time{color:#494949;font-size:9pt}.date span{margin:-6px 5px -10px 0;padding:7px 0 10px 10px}.date time{position:absolute;top:50%;left:55%;padding:9px 0 10px}.totalvotes{color:#494949!important;font-weight:600;text-transform:capitalize;margin-top:0;padding:7px 10px 10px;font-size:8pt!important;margin-right:5px}.linkinfo .shortlink input{height:10px;border:none;width:181px;font-size:13px}.account-activity-box,.sidecontentbox a.helplink{font-size:16px;padding:10px;transition:background-color .5s;text-transform:capitalize}.account-activity-box{display:block!important;background:#3b4c62;margin-right:5px}.account-activity-box:hover{background:#259eff}.account-activity-box a{color:#fff;padding:10px 70px}.side .views{color:#494949;border-left:5px solid #e6edf6;border-bottom:1px solid #e6edf6;border-right:1px solid #e6edf6;margin-right:5px;padding:7px 10px}#header #header-bottom-right{background:0 0;bottom:-18px;top:auto;padding:3px;height:59px;font-family:"Segoe UI",Helvetica,sans-serif}#header-bottom-right .user{position:relative;top:0;width:119px;padding-left:42px;padding-top:5px;font-size:13px;color:#eaeaea;line-height:170%;background:url(%%spritesheet%%) -110px -289px no-repeat #3b4c62;float:left;border:2px solid #fff;cursor:pointer}#header-bottom-right .user>a{text-indent:4px;color:#fff;display:block;line-height:12px;white-space:nowrap}#header-bottom-right #mail{top:0!important;width:42px;height:42px;display:inline-block}#header-bottom-right #modmail{position:absolute;margin-left:-267px;top:3px;padding-left:26px;padding-top:5px;background:url(%%spritesheet%%) -224px -72px no-repeat #3b4c62;border:2px solid #fff}#beta-help,.beta-hint a{position:absolute!important}#modmail.havemail{background:url(%%spritesheet%%) -224px -72px #ff4500!important}#header #header-bottom-right .logout{display:inline-block}#header #header-bottom-right #mail,#header #header-bottom-right .choice,#header #header-bottom-right .logout a{margin-left:5px;width:42px!important;height:42px;display:inline-block;text-indent:50px;overflow:hidden;transition:background-color .5s}#header #header-bottom-right #mail.nohavemail{background:url(%%spritesheet%%) 0 -114px no-repeat #3b4c62;border-radius:1px;border:2px solid #fff}#header #header-bottom-right #mail.havemail{background:url(%%spritesheet%%) 0 -114px no-repeat #ff4500;border-radius:1px;border:2px solid #fff}.res #header #header-bottom-right #mail.havemail{background:url(%%spritesheet%%) 0 -115px no-repeat #ff4500}#header #header-bottom-right .choice{background:url(%%spritesheet%%) -127px -114px no-repeat #3b4c62;border-radius:1px;border:2px solid #fff}.beta-hint,.side .usertext-body .md ol a:hover,.side .usertext-body .md ol a[href$='#achieve']:hover,.side .usertext-body .md ol a[href$='#special']:hover,.side .usertext-body .md ol a[href$='#sticky']:hover,.side .usertext-body .md ol a[href$='#stickyg']:hover,.side .usertext-body .md ol a[href$='#update']:hover{opacity:1}.beta-hint a{top:0;left:-78px;color:transparent!important;background-color:#f85f73;background-image:url(%%spritesheet%%)!important;background-repeat:no-repeat!important;background-size:341px 331px!important;background-position:-72px -143px!important;width:42px;height:42px;border-radius:1px;border:2px solid #fff;transition:background-color .5s}.beta-hint a:hover{background-color:green!important}#beta-help{background:#ffffe1!important;color:#000!important;left:1200px!important;top:170px!important}.res .beta-hint a{display:none}#header #header-bottom-right .logout a{background:url(%%spritesheet%%) -127px -42px no-repeat #3b4c62;border-radius:1px;border:2px solid #fff}#header #header-bottom-right #mail.havemail,#header #header-bottom-right #mail.nohavemail,#header #header-bottom-right .choice,#header #header-bottom-right .logout a,#header-bottom-right #modmail,#header-bottom-right .user,.user .userkarma{border-bottom:none}#header #header-bottom-right #mail:hover,#header #header-bottom-right .choice:hover,#header #header-bottom-right .user:hover{background-color:#259eff}#header #header-bottom-right .logout a:hover{text-indent:-99999px;color:#fff;background:url(%%spritesheet%%) -127px -42px no-repeat #ce352c}#openRESPrefs{position:absolute;right:365px;top:22px}#mailCount{position:absolute;left:208px;top:-2px;color:#fff;font-size:14px;overflow:hidden}.message-count{background:#259eff;height:42px;font-size:medium;line-height:42px!important;margin-left:-4px;vertical-align:top;display:none}.user .userkarma{cursor:help}#RESAccountSwitcherIconOverlay{display:none!important}#RESAccountSwitcherIcon{float:right;margin-right:5px;margin-top:-10px;background:url(%%spritesheet%%) -264px -5px no-repeat!important}#new_modmail{position:absolute;left:-75px}.md-container-small .md .-text,.md-container-small .md li,.md-container-small .md p,.md-container-small .md pre>code,.md-container-small .md td,.md-container-small .md th,.side .md .-text,.side .md li,.side .md p,.side .md pre>code,.side .md td,.side .md th{list-style:none}.side .usertext-body .md ol{position:absolute;top:30px;right:0;margin:0 30px 0 0;padding:0;z-index:99}.side .usertext-body .md ol a{background-color:#57b5ff;display:inline-block;font-size:12px;font-weight:400;padding:5px 5px 5px 0;text-decoration:none;margin-bottom:3px;opacity:.8}.side .usertext-body .md ol a[href$="#special"]{animation:1s ease-out 0s normal none infinite running pulsate;animation-duration:3s;animation-timing-function:ease-out;animation-delay:0s;animation-direction:normal;animation-fill-mode:none;animation-iteration-count:infinite;animation-play-state:running;animation-name:pulsate}.side .md>ol li a[href$='#special']:after,.side .md>ol li a[href$='#special']:before,.side .md>ol li a[href$='#sticky']:after,.side .md>ol li a[href$='#sticky']:before{margin:0 5px 0 0;font-weight:700;padding:5px 6px}.side .usertext-body .md ol a[href$='#special']{border:2px solid #fefefe;display:inline-block;font-size:12px;font-weight:400;padding:5px 5px 5px 0;text-decoration:none;margin-bottom:3px;transition:opacity .5s;background-color:#259eff;opacity:.8}.side .usertext-body .md ol a[href$='#special']:before{margin:0 5px 0 0;font-weight:700;padding:5px 6px;background-color:#3b4c62;content:"Event";color:#fff}.side .usertext-body .md ol a[href$='#achieve']{background-color:#28bc07;opacity:.8}.side .md>ol li a[href$='#achieve']:after,.side .md>ol li a[href$='#achieve']:before,.side .md>ol li a[href$='#update']:after,.side .md>ol li a[href$='#update']:before,.side .usertext-body .md ol a[href$='#achieve']:before,.side .usertext-body .md ol a[href$='#sticky']:before{margin:0 5px 0 0;font-weight:700;padding:5px 6px}.side .usertext-body .md ol a[href$='#achieve']:before{background-color:#0d9605;content:"Achievement unlocked";color:#fff}.side .usertext-body .md ol a[href$='#achieve'],.side .usertext-body .md ol a[href$='#sticky'],.side .usertext-body .md ol a[href$='#stickyg']{font-weight:400;padding:5px 5px 5px 0;margin-bottom:3px;border:2px solid #fefefe;display:inline-block;font-size:12px;transition:opacity .5s;text-decoration:none}.side .usertext-body .md ol a[href$='#sticky']{background-color:#259eff;opacity:.8}.side .usertext-body .md ol a[href$='#sticky']:before{background-color:#2ea619;content:"Sticky";color:#fff}.side .usertext-body .md ol a[href$='#stickyg']{background-color:#28bc07;opacity:.8}.side .usertext-body .md ol a[href$='#stickyg']:before,.side .usertext-body .md ol a[href$='#update']:before{margin:0 5px 0 0;font-weight:700;padding:5px 6px}.side .usertext-body .md ol a[href$='#stickyg']:before{background-color:#0d9605;content:"Sticky";color:#fff}.side .usertext-body .md ol a[href$='#update']{border:2px solid #fefefe;background-color:#1686f0;display:inline-block;font-size:12px;font-weight:400;padding:5px 5px 5px 0;text-decoration:none;margin-bottom:3px;opacity:.8;transition:opacity .5s}.side .usertext-body .md ol a[href$='#update']:before{background-color:#3b4c62;content:"Update";color:#fff}.side .md del{color:#fff;text-decoration:none}.res-nightmode body,html[lang^=nm] body{background:#1a1a1a!important}.res-nightmode #sr-header-area,html[lang^=nm] #sr-header-area{background-color:#0c1722!important}.res-nightmode a,html[lang^=nm] a{color:#f8f8ff}.res-nightmode .morelink a,.res-nightmode a[href*="#Donsiders"],.res-nightmode a[href*="#btn"],html[lang^=nm] .morelink a,html[lang^=nm] a[href*="#Donsiders"],html[lang^=nm] a[href*="#btn"]{color:#fff!important}.res-nightmode .shortlink input,html[lang^=nm] .shortlink input{background:#393939;color:#ddd}.res-nightmode .linklisting,.res-nightmode .md td,.res-nightmode .md th,html[lang^=nm] .linklisting,html[lang^=nm] .md td,html[lang^=nm] .md th{border-color:#2d2e32!important}.res-nightmode #previoussearch #moresearchinfo,.res-nightmode .comments-page .usertext-edit div textarea,.res-nightmode .md,.res-nightmode .md del,.res-nightmode .roundfield label,.res-nightmode .search-result-body,.res-nightmode .submit-page .roundfield .title,.res-nightmode div.side #searchexpando,html[lang^=nm] #previoussearch #moresearchinfo,html[lang^=nm] .comments-page .usertext-edit div textarea,html[lang^=nm] .md,html[lang^=nm] .md del,html[lang^=nm] .roundfield label,html[lang^=nm] .search-result-body,html[lang^=nm] .submit-page .roundfield .title,html[lang^=nm] div.side #searchexpando{color:#eee!important}.res-nightmode .md blockquote,html[lang^=nm] .md blockquote{background:rgba(0,87,166,.24);border-left:2px solid #259eff!important;color:#888!important}.res-nightmode .md code,html[lang^=nm] .md code{border:none!important;background-color:#393939!important;border-radius:0!important;border-left:3px solid #259eff!important}.res-nightmode .commentingAs,.res-nightmode .date time,.res-nightmode .edit-stylesheet.choice:after,.res-nightmode .linkinfo .score,.res-nightmode .linkinfo .shortlink,.res-nightmode .side .views,.res-nightmode .wiki-page .wiki-page-content,html[lang^=nm] .commentingAs,html[lang^=nm] .date time,html[lang^=nm] .edit-stylesheet.choice:after,html[lang^=nm] .linkinfo .score,html[lang^=nm] .linkinfo .shortlink,html[lang^=nm] .side .titlebox>.fancy-toggle-button,html[lang^=nm] .side .views,html[lang^=nm] .wiki-page .wiki-page-content{color:#ddd!important}.res-nightmode .date span,.res-nightmode .date time,html[lang^=nm] .date span,html[lang^=nm] .date time{border-bottom:1px solid #393939!important;background:#222!important;border-top:1px solid #393939!important}.res-nightmode #header,.res-nightmode #newlink-with-image-upload #new-link-preview,.res-nightmode .account-activity-box,.res-nightmode .date:before,.res-nightmode .morelink,.res-nightmode .nextprev a,.res-nightmode .res .RESDashboardToggle,.res-nightmode .res .RESshortcutside,.res-nightmode .titlebox h1,.res-nightmode div.titlebox .md h1,.res-nightmode div.titlebox .md h2,.res-nightmode div.titlebox .md h3,.res-nightmode div.titlebox .md h4,html[lang^=nm] #header,html[lang^=nm] #newlink-with-image-upload #new-link-preview,html[lang^=nm] .account-activity-box,html[lang^=nm] .date:before,html[lang^=nm] .morelink,html[lang^=nm] .nextprev a,html[lang^=nm] .res .RESDashboardToggle,html[lang^=nm] .res .RESshortcutside,html[lang^=nm] .titlebox h1,html[lang^=nm] div.titlebox .md h1,html[lang^=nm] div.titlebox .md h2,html[lang^=nm] div.titlebox .md h3,html[lang^=nm] div.titlebox .md h4{background:#222!important}.res-nightmode .res .RESDashboardToggle,.res-nightmode .res .RESshortcutside,html[lang^=nm] .res .RESDashboardToggle,html[lang^=nm] .res .RESshortcutside{color:#eee}.res-nightmode #header #header-bottom-right #mail:hover,.res-nightmode #header #header-bottom-right #modmail:hover,.res-nightmode #header #header-bottom-right .choice:hover,.res-nightmode #header #header-bottom-right .logout:hover,.res-nightmode #header #header-bottom-right .user:hover,html[lang^=nm] #header #header-bottom-right #mail:hover,html[lang^=nm] #header #header-bottom-right #modmail:hover,html[lang^=nm] #header #header-bottom-right .choice:hover,html[lang^=nm] #header #header-bottom-right .logout:hover,html[lang^=nm] #header #header-bottom-right .user:hover{background-color:#393939!important}.res-nightmode #header #header-bottom-right .logout a,.res-nightmode #header #header-bottom-right .nohavemail#mail,.res-nightmode #header-bottom-right #modmail,.res-nightmode #header-bottom-right .choice,.res-nightmode #header-bottom-right .user,html[lang^=nm] #header #header-bottom-right .logout a,html[lang^=nm] #header #header-bottom-right .nohavemail#mail,html[lang^=nm] #header-bottom-right #modmail,html[lang^=nm] #header-bottom-right .choice,html[lang^=nm] #header-bottom-right .user{background-color:transparent!important;outline:0!important}.res-nightmode #header-bottom-left .tabmenu,.res-nightmode #header-img,.res-nightmode #header-img.default-header,html[lang^=nm] #header-bottom-left .tabmenu,html[lang^=nm] #header-img,html[lang^=nm] #header-img.default-header{background:0 0!important}.res-nightmode #header-bottom-left .tabmenu,.res-nightmode .new-comment .usertext-body,html[lang^=nm] #header-bottom-left .tabmenu,html[lang^=nm] .new-comment .usertext-body{background-color:transparent;border:none}.res-nightmode .date,.res-nightmode .date::before,.res-nightmode .flair,html[lang^=nm] .date,html[lang^=nm] .date::before,html[lang^=nm] .flair{color:#ddd!important}.res-nightmode .footer,html[lang^=nm] .footer{border-right:none!important;border-top:none}.res-nightmode .footer div.col a,.res-nightmode .footer::after,.res-nightmode div.side div.tagline,.res-nightmode div.side form.flairtoggle,.res-nightmode div.side span.subscribers,.res-nightmode div.titlebox .md ul li,html[lang^=nm] .footer div.col a,html[lang^=nm] .footer::after,html[lang^=nm] div.side div.tagline,html[lang^=nm] div.side form.flairtoggle,html[lang^=nm] div.side span.subscribers,html[lang^=nm] div.titlebox .md ul li{color:#ddd!important}.res-nightmode .sidecontentbox .title,.res-nightmode .sidecontentbox a.helplink,html[lang^=nm] .sidecontentbox .title,html[lang^=nm] .sidecontentbox a.helplink{background:#222!important}.res-nightmode .icon-menu li,.res-nightmode .linkinfo .score,.res-nightmode .linkinfo .shortlink,.res-nightmode .reddit-link,.res-nightmode .side .views,.res-nightmode .sidecontentbox .content a.author,.res-nightmode .sidecontentbox .more,.res-nightmode .totalvotes,.res-nightmode div #searchexpando,.res-nightmode div.titlebox .md ul li,html[lang^=nm] .icon-menu li,html[lang^=nm] .linkinfo .score,html[lang^=nm] .linkinfo .shortlink,html[lang^=nm] .reddit-link,html[lang^=nm] .side .views,html[lang^=nm] .sidecontentbox .content a.author,html[lang^=nm] .sidecontentbox .more,html[lang^=nm] .totalvotes,html[lang^=nm] div #searchexpando,html[lang^=nm] div.titlebox .md ul li{border-bottom:1px solid #393939!important;border-left:5px solid #393939!important;border-right:1px solid #393939!important;background:#222!important;border-top:1px solid #393939!important}.res-nightmode .icon-menu li:hover,.res-nightmode .linkinfo .score:hover,.res-nightmode .linkinfo .shortlink:hover,.res-nightmode .reddit-link:hover,.res-nightmode .side .views:hover,.res-nightmode .sidecontentbox .content a.author:hover,.res-nightmode .sidecontentbox .more:hover,.res-nightmode .totalvotes:hover,.res-nightmode div #searchexpando:hover,.res-nightmode div.titlebox .md ul li:hover,html[lang^=nm] .icon-menu li:hover,html[lang^=nm] .linkinfo .score:hover,html[lang^=nm] .linkinfo .shortlink:hover,html[lang^=nm] .reddit-link:hover,html[lang^=nm] .side .views:hover,html[lang^=nm] .sidecontentbox .content a.author:hover,html[lang^=nm] .sidecontentbox .more:hover,html[lang^=nm] .totalvotes:hover,html[lang^=nm] div #searchexpando:hover,html[lang^=nm] div.titlebox .md ul li:hover{background-color:#393939!important;border-left-color:#ccd4e8!important}.res-nightmode div.side .titlebox div.subButtons,.res-nightmode div.side .titlebox h1.redditname+div,.res-nightmode div.side .titlebox>.fancy-toggle-button,.res-nightmode div.side div.leavemoderator,.res-nightmode div.side form.leavecontributor-button,.res-nightmode div.side p.users-online,.res-nightmode div.side span.subscribers,html[lang^=nm] div.side .titlebox div.subButtons,html[lang^=nm] div.side .titlebox h1.redditname+div,html[lang^=nm] div.side .titlebox>.fancy-toggle-button,html[lang^=nm] div.side div.leavemoderator,html[lang^=nm] div.side form.leavecontributor-button,html[lang^=nm] div.side p.users-online,html[lang^=nm] div.side span.subscribers{border-bottom:1px solid #393939!important;border-left:5px solid #393939!important;border-right:1px solid #393939!important;background:#222!important;border-top:1px solid #393939!important}.res-nightmode div.side div.tagline,.res-nightmode div.side form.flairtoggle,html[lang^=nm] div.side div.tagline,html[lang^=nm] div.side form.flairtoggle{border-left:5px solid #393939!important;border-right:1px solid #393939!important;border-bottom:none!important;background:#222!important}.res-nightmode .titlebox form.toggle,html[lang^=nm] .titlebox form.toggle{background:#222;border-bottom:1px solid #393939!important;border-left:5px solid #393939!important;border-right:1px solid #393939!important;color:#eee}.res-nightmode .sitetable .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment .comment .comment .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment .comment .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment{background-color:#393939!important}.res-nightmode .sitetable .comment,.res-nightmode .sitetable .comment .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment .comment .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,.res-nightmode .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,.res-nightmode button,html[lang^=nm] .sitetable .comment,html[lang^=nm] .sitetable .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,html[lang^=nm] .sitetable .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment .comment,html[lang^=nm] button{background-color:#222!important}.res-nightmode button.save:hover,html[lang^=nm] button.save:hover{border-color:#7cd87c}.res-nightmode button.cancel:hover,html[lang^=nm] button.cancel:hover{border-color:#f9736f}.res-nightmode a[href*="#square"]::before,html[lang^=nm] a[href*="#square"]::before{border:3px solid #393939}.res-nightmode .link,html[lang^=nm] .link{border-bottom:1px solid #2d2e32!important}.res-nightmode .listing-page .link:hover,html[lang^=nm] .listing-page .link:hover{background:#393939!important;border-left-color:#a9a9a9!important}.res-nightmode tr:nth-child(even),html[lang^=nm] tr:nth-child(even){background-color:#050505}.res-nightmode .titlebox h1:after,.res-nightmode div.titlebox .md h1:after,.res-nightmode div.titlebox .md h2:after,.res-nightmode div.titlebox .md h3:after,.res-nightmode div.titlebox .md h4:after,.res-nightmode div.titlebox .sidecontentbox .title:after,.res-nightmode div.titlebox h1:after,html[lang^=nm] .titlebox h1:after,html[lang^=nm] div.titlebox .md h1:after,html[lang^=nm] div.titlebox .md h2:after,html[lang^=nm] div.titlebox .md h3:after,html[lang^=nm] div.titlebox .md h4:after,html[lang^=nm] div.titlebox .sidecontentbox .title:after,html[lang^=nm] div.titlebox h1:after{display:block;position:absolute;z-index:-1;border-color:transparent #393939 transparent transparent!important}.res-nightmode #eu-cookie-policy .reddit-infobar,.res-nightmode #search input[type=text],.res-nightmode .flairselector,html[lang^=nm] #eu-cookie-policy .reddit-infobar,html[lang^=nm] #search input[type=text],html[lang^=nm] .flairselector{background-color:#222!important;color:#ddd}.res-nightmode .comments-page .usertext-edit div textarea,html[lang^=nm] .comments-page .usertext-edit div textarea{background-color:#222!important}.res-nightmode .reddit-infobar,html[lang^=nm] .reddit-infobar{background:#202020;BORDER:1px solid #2d2e32}.res-nightmode .reddit-infobar.with-icon:before,html[lang^=nm] .reddit-infobar.with-icon:before{background-color:solid #202020}.res-nightmode #header-bottom-left .tabmenu li.selected a,.res-nightmode .account-activity-box:hover,.res-nightmode .cookie-infobar.with-icon:before,.res-nightmode .debuginfo,.res-nightmode .link .score .likes,.res-nightmode .link .usertext-body .md,.res-nightmode .nextprev a:hover,.res-nightmode .side .morelink a:hover,.res-nightmode .sidecontentbox a.helplink:hover,.res-nightmode ::-webkit-scrollbar,.res-nightmode button:hover,.res-nightmode div.titlebox span.fancy-toggle-button a.active.remove,html[lang^=nm] #header-bottom-left .tabmenu li.selected a,html[lang^=nm] .account-activity-box:hover,html[lang^=nm] .cookie-infobar.with-icon:before,html[lang^=nm] .debuginfo,html[lang^=nm] .link .score .likes,html[lang^=nm] .link .usertext-body .md,html[lang^=nm] .nextprev a:hover,html[lang^=nm] .side .morelink a:hover,html[lang^=nm] .sidecontentbox a.helplink:hover,html[lang^=nm] ::-webkit-scrollbar,html[lang^=nm] button:hover,html[lang^=nm] div.titlebox span.fancy-toggle-button a.active.remove{background-color:#393939!important}.res-nightmode .comment .usertext .md p>a:visited,.res-nightmode .md a,.res-nightmode h2 a:visited,html[lang^=nm] .comment .usertext .md p>a:visited,html[lang^=nm] .md a,html[lang^=nm] h2 a:visited{color:#3498db}.res-nightmode ::-webkit-scrollbar-thumb,html[lang^=nm] ::-webkit-scrollbar-thumb{background-color:#666;border:2px solid #333;transition:background-color .5s}.res-nightmode ::-webkit-scrollbar-thumb:hover,html[lang^=nm] ::-webkit-scrollbar-thumb:hover{background-color:#555;transition:background-color .5s}.res-nightmode ::-webkit-scrollbar-thumb:active,html[lang^=nm] ::-webkit-scrollbar-thumb:active{background-color:#bbb}.res-nightmode ::-webkit-scrollbar-corner,html[lang^=nm] ::-webkit-scrollbar-corner{color:#555}.res-nightmode textarea,html[lang^=nm] textarea{color:#000!important}.res-nightmode .content,html[lang^=nm] .content{margin-bottom:0;margin-top:0}.res-nightmode input[type=button],.res-nightmode input[type=reset],.res-nightmode input[type=submit],html[lang^=nm] input[type=button],html[lang^=nm] input[type=reset],html[lang^=nm] input[type=submit]{border:none}.res-nightmode .side .spacer .titlebox .redditname,html[lang^=nm] .side .spacer .titlebox .redditname{border-left-color:#259eff}.res-nightmode .gold-accent,html[lang^=nm] .gold-accent{background:#3b4c62}.res-nightmode .thing .title:visited,.res-nightmode .thing.visited .title,html[lang^=nm] .thing .title:visited,html[lang^=nm] .thing.visited .title{color:#808c94}.res-nightmode .thing .title,html[lang^=nm] .thing .title{color:#b5c4d0}.res-nightmode .content.submit .info-notice,.res-nightmode .submit-page .roundfield,html[lang^=nm] .content.submit .info-notice,html[lang^=nm] .submit-page .roundfield{background-color:#222;color:#eee}.res-nightmode #header #header-bottom-right #mail.havemail,html[lang^=nm] #header #header-bottom-right #mail.havemail{outline:0}.res-nightmode .formtabs-content .infobar,html[lang^=nm] .formtabs-content .infobar{border-color:transparent!important}.res-nightmode .infobar,html[lang^=nm] .infobar{border-color:#ff4500!important}.res-nightmode span.score,html[lang^=nm] span.score{color:#888!important}.res-nightmode .comment.spam>.child,.res-nightmode .message.spam>.child,.res-nightmode .usertext.grayed .usertext-body,html[lang^=nm] .comment.spam>.child,html[lang^=nm] .message.spam>.child,html[lang^=nm] .usertext.grayed .usertext-body{background-color:transparent}.res-nightmode div.commentarea .infobar,html[lang^=nm] div.commentarea .infobar{color:#eee;border:none}.res-nightmode .comment,html[lang^=nm] .comment{border:1px solid #43474f}.res-nightmode a[href*='#icon-day'],html[lang^=nm] a[href*='#icon-day']{display:inline-block!important}.res-nightmode a[href*='#icon-day']::before,html[lang^=nm] a[href*='#icon-day']::before{display:inline-block!important;height:20px;width:20px;content:'';margin:0 7px -4px 0;background:url(%%spritesheet%%) -85px -294px}.res-nightmode a[href*='#icon-night'],html[lang^=nm] a[href*='#icon-night']{display:none}.res-nightmode a[href*="#icon-feedback"]::before,html[lang^=nm] a[href*="#icon-feedback"]::before{background-position:-47px -149px}.res-nightmode a[href*="#icon-feedback2"]::before,html[lang^=nm] a[href*="#icon-feedback2"]::before{background-position:-5px -375px}.res-nightmode a[href*="#iconz-tips"]::before,html[lang^=nm] a[href*="#iconz-tips"]::before{background-position:-234px -47px}.res-nightmode a[href*="#iconz-updates"]::before,html[lang^=nm] a[href*="#iconz-updates"]::before{background-position:-259px -119px}.res-nightmode a[href*="#iconz-faq"]::before,html[lang^=nm] a[href*="#iconz-faq"]::before{background-position:-174px -47px}.res-nightmode a[href*="#iconz-install"]::before,html[lang^=nm] a[href*="#iconz-install"]::before{background-position:-259px -119px}.res-nightmode a[href*="#iconz-wiki"]::before,html[lang^=nm] a[href*="#iconz-wiki"]::before{background-position:-204px -149px}.res-nightmode #siteTable .thing,.res-nightmode .link.promotedlink,html[lang^=nm] #siteTable .thing,html[lang^=nm] .link.promotedlink{background:#202020!important}.res-nightmode .organic-listing,html[lang^=nm] .organic-listing{background:0 0!important}.res-nightmode body>.content #siteTable .thing.self .thumbnail,html[lang^=nm] body>.content #siteTable .thing.self .thumbnail{background-position:-77px -5px}.res-nightmode body>.content #siteTable .thing .thumbnail.default,html[lang^=nm] body>.content #siteTable .thing .thumbnail.default{background-position:-174px -77px}.res-nightmode div.side span.subscribers span.number:before,html[lang^=nm] div.side span.subscribers span.number:before{background-position:-162px -5px}.res-nightmode .expando-button.selftext.collapsed,html[lang^=nm] .expando-button.selftext.collapsed{background-position:-5px -242px}.res-nightmode .expando-button.selftext.collapsed:hover,html[lang^=nm] .expando-button.selftext.collapsed:hover{background-position:-225px -204px}.res-nightmode .expando-button.selftext.expanded,html[lang^=nm] .expando-button.selftext.expanded{background-position:-65px -204px}.res-nightmode .expando-button.selftext.expanded:hover,html[lang^=nm] .expando-button.selftext.expanded:hover{background-position:-105px -204px}.res-nightmode .expando-button.video.collapsed,html[lang^=nm] .expando-button.video.collapsed{background-position:-85px -242px}.res-nightmode .expando-button.video.collapsed:hover,html[lang^=nm] .expando-button.video.collapsed:hover{background-position:-45px -242px}.res-nightmode .expando-button.video.expanded,html[lang^=nm] .expando-button.video.expanded{background-position:-65px -204px}.res-nightmode .expando-button.video.expanded:hover,html[lang^=nm] .expando-button.video.expanded:hover{background-position:-105px -204px}.res-nightmode .date:after,html[lang^=nm] .date:after{border-color:transparent #393939 transparent transparent!important}.res-nightmode .date span,html[lang^=nm] .date span{border-left:5px solid #393939!important;color:#ddd;border-right-color:#393939}.res-nightmode .date time,html[lang^=nm] .date time{border-right:1px solid #393939!important}.res-nightmode .link.last-clicked,html[lang^=nm] .link.last-clicked{background:#393939!important}.res-nightmode .comments-page .link,html[lang^=nm] .comments-page .link{border-left:3px solid transparent}.res-nightmode .sitetable.nestedlisting>.thing.stickied,html[lang^=nm] .sitetable.nestedlisting>.thing.stickied{background:#202020!important;border-bottom:none}.res-nightmode .RES-keyNav-activeElement,.res-nightmode .RES-keyNav-activeElement .md-container,.res-nightmode .res .RES-keyNav-activeElement,.res-nightmode .res .commentarea .RES-keyNav-activeElement .md,.res-nightmode .res .commentarea .RES-keyNav-activeElement.entry .noncollapsed{background-color:#292929!important}.res-nightmode .arrow.upmod{background-position:-296px -60px!important}.res-nightmode .arrow.down{background-position:-321px -60px!important}.res-nightmode .arrow.up{background-position:-289px -194px!important}.res-nightmode .arrow.downmod{background-position:-271px -60px!important}.res-nightmode .side .titlebox>.fancy-toggle-button{background:#222!important;color:#ddd!important}.RESSubscriptionButton,.res .commentarea .RES-keyNav-activeElement.entry .noncollapsed html[lang^=nm] .RES-keyNav-activeElement .md-container{background-color:transparent!important}.res #sr-header-area #srDropdownContainer a:hover,.side .md a[href="http://bit.ly/piracywiki"]:hover::after{opacity:1}.res .comment .midcol{margin-left:20px}.res .comment .new-comment{border:2px solid #ffab91!important;border-radius:0!important}.res #sr-header-area #srDropdownContainer a{width:35px;height:23px;padding:0;margin:0;display:block;background:url(%%spritesheet%%) -225px -252px no-repeat;line-height:35px;text-indent:-999em}.res .RES-keyNav-activeElement,.res .commentarea .RES-keyNav-activeElement .md,.res .commentarea .noncollapsed .RES-keyNav-activeElement.entry{background-color:0 0!important}.res .RESDashboardToggle,.res .RESshortcutside{background:0 0;border:none;font-weight:400;text-transform:uppercase;color:#222}.res .sitetable .sitetable{margin-right:0}.RESSubscriptionButton{color:#fff!important;border-radius:1px!important;border:none!important}#RESAnnouncementAlert,#userbarToggle,.multi-count,.res .message-count,.res .side .userTagLink,.res .sidebox.create,.sidecontentbox .content .RESUserTagImage::after{display:none!important}#RESSettingsButton{right:20px;top:3px}#RESStaticShortcuts{line-height:25px}.footer,.footer::after{border-bottom:1px solid #3b4c62}.footer{border-left:1px solid #3b4c62;padding:0}.footer div.col,.footer::after{font-family:"Segoe UI",Helvetica,sans-serif}.footer::after{display:block;margin-top:0;padding-top:8px!important;color:#000;content:"Designed by /u/Jaskys";font-size:16px;border-top:34px solid #3b4c62;border-right:1px solid #3b4c62;margin-bottom:-1.1px;padding:10px;width:90px}.footer div.col{position:relative;margin:0;padding:0;width:176px;height:auto}.footer div.col .title{font-size:16px;text-transform:capitalize;padding:8px;color:#fff;background:#3b4c62;max-height:18px}.footer div.col a{display:block;margin:5px;padding:3px 4px 3px 7px;color:#000}.footer div.col a:hover{color:#000;text-decoration:none;background:#fff}.footer p.bottommenu{clear:left;padding:6px}.footer p.bottommenu,.footer p.bottommenu a{font-weight:700;color:#fff}.footer .col{border-left:none!important}.debuginfo{background:#f6f6f6}.rounded{border-radius:0}.flat-vert{text-align:center}.titlebox h1.redditname a{font-size:0}.titlebox h1.redditname a:after{content:"r/Piracy";color:#fff;font:400 small verdana,arial,helvetica,sans-serif}#header .redditname a{font-size:0;background:url(%%piracylogo%%) -5px -5px no-repeat;margin-left:10px;height:100px;display:block;position:absolute;top:30px}#header .redditname a:hover{background:url(%%piracylogo%%) -5px -115px no-repeat!important;text-decoration:none}#header .redditname a:after{content:"r/Piracy";font-size:70px;font-weight:lighter;color:#ecf0f1;font-family:"Segoe UI Light",Helvetica,sans-serif;letter-spacing:.05em;margin-left:100px;line-height:100px;font-variant:normal;transition:background-color .5s}.flair-wiki{color:#e67e22;font-weight:700}.flair-wiki{height:16px;line-height:16px;border:none;background:0 0;padding:0}.flair-wiki:before{content:"- "}.flairselector{background-color:#fff}.linkflair-discussion .linkflairlabel,.side a[href*='#square-discussion']:before{background:#ff9e00}.linkflair-tip .linkflairlabel,.side a[href*='#square-tip']:before{background:#468966}.linkflair-news .linkflairlabel,.side a[href*='#square-news']:before{background:#f2385a}.linkflair-official .linkflairlabel,.side a[href*='#square-official']:before{background:#2086bf}.linkflair-help .linkflairlabel,.side a[href*='#square-help']:before{background:#ff6138}.linkflair-solved .linkflairlabel,.side a[href*='#square-solved']:before{background:#008a00}.linkflair-bug .linkflairlabel,.side a[href*='#square-bug']:before{background:#ce352c}.linkflair-update .linkflairlabel,.side a[href*='#square-update']:before{background:#3b4c62}.linkflair-feature .linkflairlabel,.side a[href*='#square-feature']:before{background:#00aba9}.linkflair-meta .linkflairlabel,.side a[href*='#square-meta']:before{background:#4390df}.linkflair-app .linkflairlabel,.side a[href*='#square-app']:before{background:#bf5a15}.linkflair-concept .linkflairlabel,.side a[href*='#square-concept']:before{background:#14b6f5}.linkflair-request .linkflairlabel,.side a[href*='#square-request']:before{background:#00aba9}.linkflair-hflairs .linkflairlabel,.linkflair-hhelp .linkflairlabel,.side a[href*='#square-hflairs']:before,.side a[href*='#square-hhelp']:before{background:#e42608}.linkflair-gaming .linkflairlabel,.side a[href*='#square-gaming']:before{background:#107c10}.linkflair-development .linkflairlabel,.side a[href*='#square-development']:before{background:#3b4c62}.linkflair-insider-bug .linkflairlabel,.side a[href*='#square-insider-bug']:before{background:#ce352c}a[href*='#square-']:hover::before{text-decoration:none;background:#259eff;border-color:#80c2ff;left:4px;top:8px;transition:all .15s ease}a[href*='#square-']:before{display:inline-block;height:10px;width:10px;content:'';margin:0 5px -4px 0;border:3px solid #e8e8e8}.linkflairlabel{margin:0 4px -4px 0;padding:3px 7px;color:#fff;font-weight:400;font-size:10px;font-family:"Segoe UI",Helvetica,sans-serif;pointer-events:none;border-radius:0;border:0}.linkflairlabel:lang(nf){display:none}html:lang(nh) .linkflair-bug,html:lang(nh) .linkflair-help{display:none!important}.listing-page .linkflair-discussion{border-left:3px solid #ff9e00;background:rgba(255,158,0,.1)}.listing-page .linkflair-tip{border-left:3px solid #468966;background:rgba(70,137,102,.1)}.listing-page .linkflair-news{border-left:3px solid #f2385a;background:rgba(242,56,90,.1)}.listing-page .linkflair-official{border-left:3px solid #2086bf;background:rgba(32,134,191,.1)}.listing-page .linkflair-update{border-left:3px solid #3b4c62;background:rgba(0,120,215,.1)}.res-nightmode .side .md blockquote,html[lang^=nm] .side .md blockquote{border-left:5px solid #3b81fb!important;color:#ddd!important}.comments-page .link.linkflair-solved{display:block}.side .md blockquote{padding:2px 10px 5px;border-left:5px solid #f5c684;background-color:#fef8f1;border-bottom:1px solid #e6edf6;border-right:1px solid #e6edf6;font-size:10px;margin:0 5px 0 0;color:#222}.side .md blockquote:hover{background-color:#fcecd9;border-left-color:#f0ad4e}.side .md blockquote a{font-size:11px}a[href*="#btn"]:hover{background:#259eff}a[href*="#Donsiders"]{background:#009e7e}a[href*="#Donsiders"]:hover{background:#259eff}a[href*="#btn"]{background:#0057a6}a[href*="#square-showflairs"]{float:right}a[href*="#square-showflairs"]::before{display:inline-block;height:10px;width:10px;content:"";background:-187px -5px #3b4c62;border:3px solid #e8e8e8;border-radius:50%;margin-left:5px}a[href*="#square-hflairs"]::after{content:"or";margin-left:50px}a[href*="#square-hflairs"]:hover::after{color:#3b4c62}.side .md [href$="#butt"]{display:inline-block!important;font-size:8pt;border:2px solid #3b4c62;padding:9px 8px;transition:background-color .5s;text-align:center;color:#3b4c62}.side .md [href$="#butt"]:hover{background:#3b4c62;color:#fff}.side .md>p:first-of-type{display:none}.comments-page .link.linkflair-bug .flat-list a.flairselectbtn:after,.comments-page .link.linkflair-help .flat-list a.flairselectbtn:after{content:"- flair your thread as solved once your problem is resolved";margin-left:6px;color:#008a00}.comments-page .link.linkflair-help .flat-list a.flairselectbtn{color:#3b4c62!important}.link a.thumbnail[href*="blogs.windows.com"] img,.linkflair-solved.link,.subscribers .word,a[href*='#iconz']+.keyNavAnnotation{display:none}.search-page .linkflair-solved.link{display:block}a[href*='#icon-chat']::before,a[href*='#icon-feedback']::before,a[href*='#icon-feedback2']::before,a[href*='#icon-night']::before{display:inline-block;height:20px;width:20px;content:'';margin:0 7px -4px 0}a[href*='#icon']:hover,a[href*='#iconz']:hover{text-decoration:none}a[href*='#icon-chat']::before{background:url(%%spritesheet%%) -5px -204px}a[href*='#icon-feedback']::before{background:url(%%spritesheet%%) -35px -204px}a[href*='#icon-night']::before{background:url(%%spritesheet%%) -125px -242px}a[href*='#icon-feedback2']::before{background:url(%%piracylogo%%) -5px -345px}a[href*="#icon-more"]{text-align:center;display:block;color:#259eff;font-size:16px}a[href*='#iconz-faq']::before,a[href*='#iconz-install']::before,a[href*='#iconz-tips']::before,a[href*='#iconz-updates']::before,a[href*='#iconz-wiki']::before{display:inline-block;height:20px;width:20px;content:'';margin:0 7px -4px 0}a[href*='#iconz-tips']::before{background:url(%%spritesheet%%) -204px -47px}a[href*='#iconz-faq']::before{background:url(%%spritesheet%%) -47px -47px}a[href*='#iconz-updates']::before{background:url(%%spritesheet%%) -102px -77px}a[href*='#iconz-install']::before{background:url(%%spritesheet%%) -229px -119px}a[href*='#iconz-wiki']::before{background:url(%%spritesheet%%) -174px -149px}.link a.thumbnail[href*="blogs.windows.com"]{background:url(%%spritesheet%%) -234px -149px no-repeat!important;width:45px;height:45px;margin:10px}.res-nightmode .subscribers .number:after,.subscribers .number:after{content:" leechers"}.arrow.down{pointer-events:none}.subscriber .arrow.down{pointer-events:initial}#baconBit{width:394px!important;height:304px!important;background-image:url(%%placeholder%%) no-repeat!important;transition:all 10s linear!important}.res-nightmode a[href*="#icon-chat"]::before,html[lang^=nm] a[href*="#icon-chat"]::before{background-image:url(%%piracylogo%%);background-position:-5px -405px}.submit-page .side:before{content:"Use search before posting";font-size:large;color:#529dff;margin-left:27px;top:2px;position:relative}.side .md a[href="http://bit.ly/piracywiki"]{z-index:1;text-indent:-9999px;background-image:url(%%wikibanner%%);background-position:-5px -5px;position:relative;height:70px;width:295px;display:block;margin:10px 0;border-radius:3px}.side .md a[href="http://bit.ly/piracywiki"]:after{content:"";background-image:url(%%wikibanner%%);background-position:-5px -105px;transition:ease-out opacity .3s;opacity:0;position:absolute;top:0;right:0;bottom:0;left:0}


.flairtoggle,
.titlebox .tagline {
	display: none;
}


/* --- FLAIR --- */

.flairselectbtn {
	border: 1px solid #ccc;
	padding: 0.1em .8em !important;
	border-radius: 2px;
	/*box-shadow: 0 1px 1px #EEE;*/
}
.flairselectbtn:hover,
.flairselectbtn:focus {
	text-decoration: none !important;
	border-color: #256DB6 !important;
	color: #256DB6 !important;
}

/* -- Flair selector popup -- */

.flairoptionpane {
	margin-bottom: -0.4em;
	overflow: visible;
}
.flairselector {
	box-shadow: 4px 4px 0 #eee;
	width: auto !important;
}

.flairselector.drop-choices.active {
	border: 1px solid #ddd;
	
}

.flairselector h2,
.flairselector .flairselection,
.flairselector .status,
.flairselector li a {
	display: none !important;
}

.flairselector ul {
	display: block;
	/*width: 150px !important;*/
	max-width: inherit;
	overflow: visible;
}
.flairselector li {
	text-align: center !important;
	position: relative;
	padding: 4px 0;
	padding-left: 4px !important;
	background: #F6F6F6;
	margin-bottom: 0.2em;
	font-size: 1.8em;
	width: 130px !important;
}
.flairselector li:hover {
	background: #F0F0F0;
}
.flairselector li.selected:after {
	content: "✓";
	background: #444;
	position: absolute;
	top: 50%;
	right: 0.2em;
	width: 24px;
	height: 24px;
	font-size: 12px;
	line-height: 24px;
	color: #FFF;
	border-radius: 50%;
	margin-top: -12px;
}
.flairselector form {
	border-top: none;
}
.flairselector button {
	width: 100%;
	display: block;
}
.flairselector form button {  
    margin-left: 0px;
}


/*Link Flair*/
.link .linkflairlabel {
    /*background-color: #CCC!important;*/
    color: #666;
    font-size: 13px;
    line-height: 1em;
    vertical-align: top;
    text-align: center;
    padding: 3px 5px;
    margin-top: 1px;
    border-radius:0;
    border: 0px;
    min-width:58px;
    max-width:300px;
}
.linkflairlabel[title="MOD POST"], .linkflairlabel[title="OFFICIAL"], .linkflairlabel[title="ANNOUNCEMENT"], .linkflairlabel[title="WEEKLY THREAD"], .linkflairlabel[title="MEGATHREAD"], .linkflairlabel[title="SUGGESTIONS"], .linkflairlabel[title="BEST OF 2017"], .linkflairlabel[title="SPOTIFY"] {
    background-color:#00a64f!important;
    color:#FFF!important;
}
.linkflairlabel[title="AMA"] {
    background-color:#f28787!important;
    color:#FFF!important;
}
.linkflairlabel[title="PSA"] {
    background-color: #f8a5a5;
    color:#000000!important;
}
.linkflairlabel[title="News"] {
    background-color: #EFE096;
    color:#000000!important;
}
.linkflairlabel[title="Meta"] {
    background-color: #8dda8a;
    color:#000000!important;
}
.linkflairlabel[title="Question"] {
    background-color: #71a9f7;
    color:#000000!important;
}
.linkflairlabel[title="Discussion"] {
    background-color: #c9b5f0;
    color:#000000!important;
}
.linkflairlabel[title="Release"] {
    background-color: #ffacec;
    color:#000000!important;
}
.linkflairlabel[title="Humor"] {
    background-color: #f2cea3;
    color:#000000!important;
}
.linkflairlabel[title="Guide"] {
    background-color: #A4DFD0;
    color:#000000!important;
}
.linkflairlabel[title="Screener Release"] {
    background-color: #dfc046;
    color:#000000!important;
}
.linkflairlabel[title="SCREENERS MEGATHREAD"] {
    background-color: #dfc046;
    color:#000000!important;
}


/* Users online */

div.side p.users-online{
  padding: 10px;
    border: 1px solid #d7ecff;
    border-left: 5px solid #d7ecff;
    border-right: 1px solid #d7ecff;
    background-color: #ffffff;
    color: #000;
    font-size: 8pt;
    border-radius: 0;
    font-weight: 400;
    margin: 0 5px 0 0
}

div.side span.subscribers {
    border-bottom:none;
}

.res-nightmode .subscribers .number:after,
.subscribers .number:after {
    content: " leechers"
}
.users-online .number:after {
    content: " seeders"
}

.leavemoderator,
.subscribers .word, .users-online .word {
    display: none
}

/* end */

.pagename{
    visibility: hidden;
}
.pagename a{
    visibility: visible;
}

/* visited links color */

#siteTable div.thing a.title:visited {
     color: #a849ff
     }

/* new links color */

#siteTable div.thing a.title { color: #0079d3; }

#siteTable div.thing a.title:hover { color: #a849ff; }

/* link colors (in comments) */

.comment .md a {color:#0079d3;}

.comment .md a:visited {color:#551a8b;}

.comment .md a:hover {color:#a849ff;}

  .md a {
    color: #0079d3; }

.last-clicked { color: white; background-color: white; }
