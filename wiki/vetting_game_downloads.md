---
---

[<- Back to FAQ](https://www.reddit.com/r/piracy/wiki/faq)

---
---

**Note 1:**

It is in the nature of antiviruses to flag pirated software/cracks as viruses/trojans/riskware, etc, so your game download will inevitably be flagged as such by your antivirus, even if it's safe to run. Plenty of fake downloads around the net, whether they be distributed in sketchy youtube videos or TPB malware uploads, will tell you the same thing in an attempt to get you to run an infected file. That is why SrrDB is such a useful tool, because you can vet your Scene game download (or other software, if it's a Scene release) to verify that it hasn't been repackaged to contain malware.

&nbsp;

**Note 2:**

In regards to the usage of the word "Scene", it has a very specific purpose. In short, sites like srrdb.com/predb.me will ***only*** track scene releases. If a group is not tracked by such sites, then it is not a Scene group.

Some more information:

[What is the difference between "The Scene" and p2p?](https://www.reddit.com/r/Piracy/comments/b0c0ns/difference_between_the_scene_and_p2p/) - Reddit thread. Outdated, but the idea is the same.

[Short, concise, and simplistic explanation of what "The Scene" is](https://www.reddit.com/r/Piracy/comments/32isgo/noobpirate_what_is_a_scene_cracktorrent/) - Reddit thread

[Warez Scene](https://en.wikipedia.org/wiki/Warez_scene) - Wikipedia

&nbsp;

**Note 3:**

[Fitgirl repacks](http://fitgirl-repacks.site/) are repackaged from original scene releases. Her releases are very popular and are safe to install (if you've obtained them from her website). However, her repacks are extremely compressed and can take hours to install, even on a beefy system. Keep this in mind before opting to download from her site. The point of repacks such as these is to offer people with **very** slow or data-capped internet a chance to download games in a timely manner.

&nbsp;

---

## ► **Doing a proper search for your game.**

You can begin by doing a proper search for the game. Visit [srrdb.com](https://www.srrdb.com/) and search for your game. Copy and paste the release name onto the search bar of a [torrent indexer](https://www.reddit.com/r/Piracy/wiki/megathread#wiki_torrent_indexers.2Fsites) (Don't use the pirate bay). In case you don't want to receive copyright infringement complaints from your ISP and you don't have a VPN, use [Ovagames.com](http://www.ovagames.com/) as it provides direct download links instead of torrents.

## ► **How to verify that a supposed "Scene" upload of a game is legitimate, ie. not a virus**

Click on the game listing that you found on SrrDB.

On the release page, you'll find a list of filenames and CRC checksums. Note the CRC value of the `.iso` file [\(pic\).](https://i.imgur.com/wbgdTOi.jpg)

The checksum value you copied is the CRC32 checksum of the original scene release. You want to determine what the checksum of your own downloaded `.iso` file is. If it matches that which is reported on SrrDB, then your download has not been modified in any way from the original scene release, and it is therefore safe to install.

&nbsp;

## ► **How to calculate the CRC32 checksum of your `.iso` file:**

Download and install 7zip. Right click on the `.iso` file, navigate to the `CRC-32` option in the context menu: https://i.imgur.com/Ov6osun.jpg

7zip will begin calculating the CRC32 checksum. This will take a short while, depending on the size of the file. Once it's finished, 7zip will show you the CRC32 value of your file. Compare it against SrrDB's reported value for the `.iso` file. If they match, then you're good to go. You may install.

&nbsp;

## ► **If your download is a set of rar files, use this method**

If your download is a set of (part'ed) rar files [\(pic\)](https://i.imgur.com/c7n8loo.jpg), then you can download the `sfv` file included in the SrrDB page [\(pic\)](https://i.imgur.com/0LzkDq0.jpg) and place it in the same folder where the rarset is located. The `sfv` file is just a simple text file which contains a list of all the part'ed rar filenames included in the original scene release, along with the CRC32 checksums for each file. Install [QuickSFV](https://www.quicksfv.org/index.html) which will allow you to double click on an `sfv` file in order to begin a hash check on all of the part'ed files to check if they're valid. A terminal window will pop up, and if all files come up as "Ok", then you're good to go.

If, after installing QuickSFV, you double click on an `sfv` file and it doesn't begin checking, you may have to manually assign `sfv` files to open with QuickSFV. If you're on Windows, right click on the `sfv` file, select Properties, then click the Change button, click More Apps, then scroll all the way down, select "Look For Another App On This PC". Navigate to `"C:\Program Files\QuickSFV` and select the `quicksfv.exe`. Done.

Afterwards, simply right click on the singular `.rar` file and select `extract here`. The rest of the numbered part'ed rars `.r01`, `.r02`, `.r03`, etc. will be detected and 7zip/winrar will extract the `.iso` file that was contained and part`ed into all these rar files. Then just mount the iso and install the game.

&nbsp;