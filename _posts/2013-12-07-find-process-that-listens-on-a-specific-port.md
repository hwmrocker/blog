---
title: "find process that listens on a specific port"
layout: post
categories:
 - linux
 - cli
---

Don't forget to run it as root, otherwise you might not see the programm that uses the port. `-P` will show the port numbers insted of words, and `-n` will not try to look up the host names and increases the output speed a lot.

    sudo lsof -Pn | grep LISTEN | grep :80

Read [this page][link] for more alternatives and better explanation

[link]: http://www.cyberciti.biz/faq/find-out-which-service-listening-specific-port/