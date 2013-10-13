---
layout: post
title: "save edited file in vim as root"
date: 2013-06-28
comments: false
tags:
 - vim
 - linux
---
If you start to edit a file as a regular user and realise you should have done it as root. You can still save the files as root:

    :w !sudo tee %
or

    :w !sudo tee new-file.name
