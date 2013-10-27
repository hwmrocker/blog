---
title: "Multidesktop tip: Move window to new screen"
layout: post
categories:
 - linux
 - ubuntu
 - compiz
---

First you need to install the compizconfig-settings-manager the extra plugins.

    sudo apt-get install compizconfig-settings-manager compiz-plugins-extra

Now you can open the settings manager

    ccsm

Select **Put** from the category **Window Management**. You can also  type `put` in the filter input box to make it easier to find. Enable the plugin. If you click on the name you can also configure it and change the keyboard shortcuts. I use `Alt`+`Super`+`Right` for *Put To Next Output*.

Now you have to log out and log in again to be able to use the new settings. At least when you installed the extra plugins.