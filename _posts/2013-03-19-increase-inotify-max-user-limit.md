---
layout: post
title: "increase the inotify max user limit"
date: 2013-03-19
comments: false
categories:
 - inotify
 - linux
 - ubuntu
---

    sudo vi /etc/sysctl.conf

    fs.inotify.max_user_instances = 8000
    fs.inotity.max_user_watches = 524000

I found [here](http://community.spotify.com/t5/Desktop-Linux/Spotify-wont-start-FileSystemMonitorLinux-failed/td-p/243130/page/2) another solution.

    sudo -s echo 8192 > /proc/sys/fs/inotify/max_user_instances
