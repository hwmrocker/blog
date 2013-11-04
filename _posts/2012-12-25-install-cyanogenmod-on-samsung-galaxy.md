---
layout: post
title: "Install Cyanogenmod on Samsung Galaxy S3 from Ubuntu"
date: 2012-12-25
comments: false
categories:
 - linux
 - ubuntu
 - android
 - cyanogenmod
---


There are a lot of Howtos telling you how install Cyanogenmod on your phone, but most of them assuming you are using Windows. I kicked out my last Windows PC years ago so thats not an option for me.

Luckily I could combine different posts to get it working for me. Which made me
even more disturbed was the fact that every how to hosted their own zip files
with the images that should be transmitted to phone or even installed on your
computer.

I tried to find the original websites and download the stuff from there instead
of trusting that the images are ok. I would like to spend a little bit more time
to find the correckt image from the offical site than trusting someone I don't
know that he didn't installed a backdoor in my image :P

### Preperation:

Download the following files

- [heimdall](http://www.glassechidna.com.au/products/heimdall/)
- [clockworkmod rommanager](http://www.clockworkmod.com/rommanager)
- [cyanogenmod rom](http://get.cm/?device=i9300)
- [google apps](http://wiki.cyanogenmod.org/w/Google_Apps "Google_Apps")


### Install the rom manager
connect your phone to your laptop with an usb cable.

press vol down + center + power for 10 sec to enter odin mode

extract the recover.img if the rommanager was delivered as a rar file and flash the recovery loader:

{% highlight bash %}
hamdall --flash recover.img --no-reboot
{% endhighlight %}

after the progress bar is full, diconnect the device and remove the battery or the image
is deleted imeadatelly after the reboot and you have to try it again.

### install the cyanogen mod image

put the zip files for cm and google app to the phone. E.g external SD card.

press vol up + center + power for 10 sec until it reboots into the recovery loader

make a factory reset
install from zip
install cm (you need to browse to the directory where you put them)
install google

reboot :)
