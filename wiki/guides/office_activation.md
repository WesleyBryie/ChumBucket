---
---

[◄◄ **Back to Guides**](https://www.reddit.com/r/piracy/wiki/guides)

[◄◄ **Back to FAQ**](https://www.reddit.com/r/piracy/wiki/guides)

---
---

# WINDOWS OFFICE INSTALLATION AND ACTIVATION

&nbsp;


For a fully free and open source alternative to MS Office, you may also try [LibreOffice.](https://www.libreoffice.org/)

&nbsp;


**Note:** Some people may recommend buying cheap keys elsewhere. This is not recommended, as these are grey-market keys, gathered from MSDN channels, each key sold multiple times ([extra reading](https://www.reddit.com/r/windows/comments/b7jolc/is_cheap_windows_10_licenses_lifetime_or_one_time/ejshgai/)). You're not buying directly from MS so you're not buying a license, you're just buying a key and living on the promise that MS won't discover and deactivate it.

It's essentially just piracy with a middleman.

&nbsp;

**Note 2**: We only recommend downloading and installing official/untouched Windows ISOs. Pre-cracked/altered windows ISOs are not recommended at all. Above all, it is recommended to stay away from any software found at The Pirate Bay. It is full of malware torrents, even those [by skulled users.](https://www.reddit.com/r/Piracy/comments/cxbn33/psa_ransomware_all_current_vegas_pro_17_torrents/)

&nbsp;

**Troubleshooting** `Office License isn't Genuine`: https://infohost.github.io/office-license-is-not-genuine




---
---


## ► Download Office

It is recommended to download Office via [tb.rg-adguard.net/public.php](https://tb.rg-adguard.net/public.php), which is a front end for MSFT-provided downloads. MSFT provides download links for Office on their website, but they are buried on within a complex tree, on top of which you would need a license key in order for them to reveal the download links. The download links are static, however, so `rgadguard` serves as a neat little tool for organizing MSFT software downloads. The downloads executed by `rgadguard` will show download URLs `officecdn-microsoft-com.akamaized.net`, `officecdn.microsoft.com.edgesuite.net` (To check the download history in Chrome and Firefox, hit `CTRL+J`), which are domains belonging to [Akamai](https://www.akamai.com/), the CDN provider contracted by MSFT for the purpose of distributing their software suite.

Choose your preferred version of office to download from `rgadguard`. Naturally, you'll want to choose the latest version of Office, which would be Office 2019 or O365, which can be activated through the use of a Mondo License, which will allow you to retain the local feature set (cloud features will remain inaccessible without paying).

&nbsp;






## ► Install Office

Once you have the `img` file downloaded, for whatever version of Office you downloaded, you'll want to mount it. On Windows 8/10, just double click on it. If it's not set to [open with File Explorer](https://ibb.co/BZDKJf3) by default, right click on the file > Properties > Change > File Explorer. Inside the folder structure of the mounted `img`, navigate to the `Office` folder and run the Setup `exe` file that corresponds to your system. Eg. If your Windows is 64-bit, run the `Setup64.exe` installer.

&nbsp;






## ► Office Activation Methods

2 of the better methods of activating Office are:

1. Activating via `MAS` (Microsoft Activation Scripts) by Massgravel. Original page at [Nsane Forums](https://nsaneforums.com/topic/316668-microsoft-activation-scripts/) (Needs login). Downloads available at the MAS GitHub Repo [Releases page.](https://github.com/massgravel/Microsoft-Activation-Scripts/releases)

2. Activating via `KMS_VL_ALL_AIO` by abbodi1406. Original [page at MyDigitalLife forums](https://forums.mydigitallife.net/threads/kms_vl_all-smart-activation-script.79535/#post-838808) (Needs login). [Codepen page](https://codepen.io/abbodi1406/full/yLaYNKr), use one of the backup links to download.


&nbsp;

The benefit of `MAS`, as stated by Massgravel, is that it utilizes a remote KMS host for activation, as such no local binaries will be kept on your machine, minimizing the chances of your antivirus raising issues. The disadvantage is that the remote KMS host may not be online forever. Other remote KMS hosts, such as those provided by Kmsguides, have been online for several years, so the possibility of the remote KMS host going offline may not be that big of a consideration.

The benefit of `KMS_VL_ALL` is that a local KMS host is created, eliminating the risk of the KMS host going offline. The disadvantage is that your antivirus will be more likely to pick up on the binaries that are needed to be kept locally in order for the local KMS host to function.

You can always add an exception for any detections regarding the KMS activation that your antivirus brings up, if it is your own machine. If you are activating someone else's machine, which you may not always have access to in order to solve any issues brought up by a overzelaous antivirus, you may want to consider activating via `MAS`.

Alternatively, you can just flip a coin and choose a number.

The versions of Office provided by Microsoft are Retail versions, and to activate via KMS, your Office installations need to first hold a Volume License. Lucikly, both `KMS_VL_ALL` and `MAS` will convert your Office installations to Volume License before activating them.

Office 365 is only offered with a retail version with no Volume License available that would be able to be activated with a KMS host. If you don't care about O365 cloud features and want to preserve the local feature set, you can still choose to activate via `MAS` or `KMS_VL_ALL_AIO`, which will automatically convert O365 to a `Mondo` license and activate it, which will allow you to retain the local O365 feature-set.

&nbsp;






## ► Activate via MAS

Download `MAS` from the MAS GitHub Repo Releases page linked above. Extract the files from the `7z` archive and run the `cmd` file located in the `All-In-One-Version` folder with administrator privileges.

If your Windows 10 is activated with `KMS38`, first navigate to the `Extras` option and choose to protect your KMS38 from being overwritten by the regular KMS activation which we will run next.

To activate Office, choose the option `Online KMS Activation`, then run the option to activate (activates for 180 days), then run the option `Renewal and Activation Task`, which will create a System Scheduled Task to automatically re-run the activation task every so often to renew the activation with the remote KMS host.

&nbsp;





## ► Activate via KMS_VL_ALL

Download `KMS_VL_ALL_AIO` cmd file from the Codepen page linked above. Extract the `cmd` file from the archive and run it with administrator privileges.

If your Windows 10 is activated with `KMS38`, choose option `5` to toggle the option `Process Windows` so that it shows `[No]` next to it.

To activate Office, run the option `Install Activation Auto-Renewal`.

&nbsp;