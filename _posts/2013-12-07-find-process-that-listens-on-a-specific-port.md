---
title: "find process that listens on a specific port"
layout: post
categories:
 - linux
 - cli
---

Don't forget to run it as root, otherwise you might not see the programm that uses the port. `-P` will show the port numbers insted of words, and `-n` will not try to look up the host names and increases the output speed a lot.

    sudo lsof -Pn | grep LISTEN | grep :80

Read [this page][link] for more alternatives and better explanation.

Update: I got a tip from [Johannes][shezilink] for a solution that could be easy remembered by people who speak german.

	sudo netstat -tulpen | grep LISTEN | grep :80

Tulpen is the german plural word of tulip. If you just use the singular `tulpe` the command will run very slow because it tries to lookup tha names for the ports and ip adresses.

[link]: http://www.cyberciti.biz/faq/find-out-which-service-listening-specific-port/
[shezilink]: http://shezi.de/