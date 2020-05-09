---
---

[◄◄ Back to Guides](https://www.reddit.com/r/piracy/wiki/guides)

---
---

# WINDOWS 10/LTSB/LTSC INSTALLATION AND ACTIVATION

&nbsp;




**Note:** It is in the nature of hacktools to be picked up as malware by your antivirus. Hwidgen, the tool used to activate Windows 10, is safe. [Some further reading regarding hwidgen](https://www.reddit.com/r/Piracy/comments/d654al/contribution_hwidgen_source_code/). Make sure to either turn off your antivirus or set up a folder which you can add to your antivirus' exclusion list, which you will download hwidgen into.

**Note 2:** Some people may recommend buying cheap keys elsewhere. This is not recommended, as these are grey-market keys, often volume keys that were purchased by companies or sometimes just OEM keys taken from existing computers (school computers, etc). You're not buying directly from MS so you're not buying a license, you're just buying a key and living on the promise that MS won't discover and deactivate those keys.

It's essentially piracy with a middleman.

**Note 3**: We only recommend downloading and installing official Windows ISOs. Pre-cracked/altered windows ISOs are not recommended at all.

&nbsp;





---

## ► Installing a fresh copy of windows 10

This part is not related to piracy at all, since Microsoft provides a free download of windows 10. As such, you can find guides on how to install windows 10 anywhere on the internet. Example video here: [time stamp 3:15](https://youtu.be/MfwjISmkEJM?t=195).

Requirements:

* A USB drive of at least 4GiB. The Windows 10 ISO installation media is approximately 3.5 GiB in size.
* Another working PC (If you are building a new PC).

Download and run the [**media creation tool**](https://www.microsoft.com/en-us/software-download/windows10) from microsoft. It will create a bootable installation media for windows 10 on your USB drive. Then just boot into the USB drive in order to fresh install Windows 10.

&nbsp;



**Windows LTSB / LTSC**

Note: The eval ISOs of LTSB/LTSC cannot be extended past their typical 3 month expiry window. You need to grab the full ISOs.

> LTSB isos hosted by the-eye: https://the-eye.eu/public/MSDN/Windows%2010/

> LTSC x86_64 (64-bit) iso: http://cdn.digiboy.ir/?b=dlir-s3&f=SW_DVD5_WIN_ENT_LTSC_2019_64-bit_English_MLF_X21-96425.ISO (original thread [here](https://www.reddit.com/r/Piracy/comments/9wzu0f/ltsc_2019_rereleased_iso_x32x64_en/)).

To create a bootable USB drive from the downloaded `.iso` file, you'll need [**Rufus**](https://rufus.ie/), since the Microsoft's creation tool does not support LTSB/LTSC. Alternatively, you may use [WoeUSB](https://github.com/slacka/WoeUSB) if you're on Linux.

Further reading: [What is Windows LTSC?](https://old.reddit.com/r/Windows10LTSC/wiki/index)

Note that LTSC will stay frozen on the feature set of Windows 10 build 1809 (until the next long term channel, to be released in 2021), if you have an Xbox Game Pass, you'll need build 1903, which is only attainable with the consumer edition of Windows 10. Be careful if you have newer hardware (2019 or later), research to see if your hardware will perform optimally on LTSC.

&nbsp;





## ► Activating Windows 10

Just download and run [**hwidgen**](http://www.reddit.com/r/piracy/wiki/tools) to activate. Usage: [KMS38 mode for LTSC, else hwid.](https://i.imgur.com/lmjLOtq.jpg)

It's permanent and will not install a background service, which would be liable to be removed by an antivirus, causing your windows to become de-activated, which was historically the case with previous KMS activation tools. It grants, by all intents and purposes, a genuine licenese, because it takes advantage of the fact that Microsoft still offers a free win7/8 -> win10 upgrade, spoofs that upgrade ticket, thus granting you a digital license to Windows 10.

&nbsp;




## ► Upgrading to Windows 10 (from a previous version of Windows)

Alternatively, if you're currently on a previous version of Windows, you'll be pleased to learn that Microsoft still offers a free upgrade to Windows 10 from a prior Windows version (7 and 8). The upgrade tool is still available through Microsoft's accessibility portal (for people who use assistive technologies) which can be found here:

>https://go.microsoft.com/fwlink/?linkid=822784 (Immediately starts a 6 MiB download, don't freak out).

If your Windows 7 OS was activated with a SLIC loader (i.e. Daz's Windows loader), or your Windows 8.1 OS was activated with a KMS activator, then you will be able to upgrade to Windows 10 and your OS wil be genuine thanks to digital entitlement. Digital entitlement provides your Windows 10 copy a genuine digital license since "you upgraded to Windows 10 for free from an eligible device running a 'genuine' copy of Windows 7 or Windows 8.1."

This digital license is tied to your hardware. Therefore if you would prefer to "clean install" Windows 10 after the upgrade, you can reset Windows 10 and it will activate automatically after the clean installation. You may also sign in with your Microsoft account to have the key tied to your account.

Listed below are some relevant links to the upgrade process and digital entitlement:

>https://support.microsoft.com/en-us/help/12440/windows-10-activation

>https://support.microsoft.com/en-us/help/20530/windows-10-reactivating-after-hardware-change

>https://www.tenforums.com/tutorials/55398-link-microsoft-account-windows-10-digital-license.html

&nbsp;