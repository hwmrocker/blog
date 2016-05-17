---
title: "jenkins and arch linux or systemd"
layout: post
categories:
 - linux
 - arch
 - systemd
---

first install jenkins

    sudo pacman -S jenkins

then start it (or enable it first)

    systemctl start jenkins

lookup the initial password. (show the systemd log files for user jenkins)

    journalctl -u jenkins

here you find the similar lines

    ...
    May 17 11:15:46 hwm-arch jenkins[8295]: *************************************************************
    May 17 11:15:46 hwm-arch jenkins[8295]: *************************************************************
    May 17 11:15:46 hwm-arch jenkins[8295]: *************************************************************
    May 17 11:15:46 hwm-arch jenkins[8295]: Jenkins initial setup is required. An admin user has been created and a password generated.
    May 17 11:15:46 hwm-arch jenkins[8295]: Please use the following password to proceed to installation:
    May 17 11:15:46 hwm-arch jenkins[8295]: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    May 17 11:15:46 hwm-arch jenkins[8295]: This may also be found at: /var/lib/jenkins/secrets/initialAdminPassword
    May 17 11:15:46 hwm-arch jenkins[8295]: *************************************************************
    May 17 11:15:46 hwm-arch jenkins[8295]: *************************************************************
    May 17 11:15:46 hwm-arch jenkins[8295]: *************************************************************
    ...

open the [dashboard view][1] [http://localhost:8090][1] in your browser. Do not create a new user as suggested, it will not work. But search for the login button and use the long password you found in the previous logs.

Now you can create a new admin user.

[1]:http://localhost:8090