---
title: "use tcpdump on an android phone"
layout: post
categories:
 - android
 - tcpdump
 - wireshark
---

I needed to intercept packets that where send by an app to verify that those packets where not malformed. On linux i used wireshark and tcpdump. Since android is a kind of linux i hoped that i might find tcpdump.

You need a rooted device, a terminal emulator and the binary of tcpdump. I am using Cyanogenmod 10.1.3 and therefore the device is allready rooted and they a good terminal emulator preinstalled.

The first step is to get the binary. I took it from [this blogpost][blog]. Just [download this file][binary] from your android device. I didn't compile it, so I cannot guarantee you that there are no backdoors or other harmfull stuff added to the source code before. And since you have to run it as root, you should think twice if you [want to compile it][compile].

Move the downloaded file to `/storage/sdcard0/tcpdump`. Then open your terminal and copy paste the following instructions to install the binary. You have to install it again after you update your device. At least after the cyanogenmod update.

    su
    mount -o remount,rw /system
    cp /storage/sdcard0/tcpdump system/bin
    cd system/bin
    chmod 777 tcpdump
    mount -o remount,ro /system

To capture the packets just type the following. But make sure your terminal emulator can send `CTRL` + `C`.

    tcpdump -s 1514 -w /storage/sdcard0/out.pcap



[blog]: http://gadgetcat.wordpress.com/2011/09/11/tcpdump-on-android/
[binary]: http://www.strazzere.com/android/tcpdump
[compile]: http://androidap.blogspot.de/2010/11/tcpdump-for-android.html