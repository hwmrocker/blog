---
title: "unlock jolla phone, from permanently locked mode"
layout: post
categories:
 - Jolla
---
Put your phone into the [Recovery Mode][recovery]:

1. Power off your phone, disconnect from all cables
2. Remove the battery
3. Hold down the Volume-Down-Button
4. Insert the battery again
5. Push the Power-Button
6. Release all buttons as soon the phone vibrates
7. Connect your phone with the PC via USB

Now you should have a second network interface, and now you can use telnet to access the recovery menu.

    telnet 10.42.66.66

Just select number 4 and enter your device lock code.

```
-----------------------------
     Jolla Recovery v0.3.1      
-----------------------------
Welcome to the recovery tool!
The available options are:
1) Reset device to factory state
2) Reboot device
3) Bootloader unlock [Current state: locked]
4) Shell
5) Try btrfs recovery if your device is in bootloop
6) Exit
Type the number of the desired action and press [Enter]: 
4

If you continue, this may void your warranty. Are you really SURE? [y/N] y
Type your devicelock code and press [ENTER] key:
(please note that the typed numbers won't be shown for security reasons)
[OK] Code accepted.
```

modify the devicelock settings file

    mount /dev/mmcblk0p28 /mnt
    sed -i "/nemo\\\devicelock\\\maximum_attempts=/c\nemo\\\devicelock\\\maximum_attempts=-1" /mnt/usr/share/lipstick/devicelock/devicelock_settings.conf

disconnect the phone and reboot it.

I found the info on [this zendesk page][zendesk]

[recovery]: https://jolla.zendesk.com/hc/en-us/articles/204709607
[zendesk]: https://jolla.zendesk.com/hc/en-us/articles/201440487-What-are-the-Device-Lock-and-Security-code-
