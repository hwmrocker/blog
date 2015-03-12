---
title: "emerge python3.4 in Funtoo"
layout: post
categories:
 - linux
 - funtoo
 - python3
---

insert the following line into /etc/make.conf

    PYTHON_ABIS="2.7 3.4"

and unmask python 3.4, either with 

    emerge -auDN @world --autounmask-write
    etc-update

or just edit the /etc/portage/package.unmask and insert the line your self

then update your world

    emerge -auDN @world