---
layout: post
title: "How to run a differnt shell command but with the same parameters"
date: 2013-07-04
comments: false
tags:
 - linux
 - bash
---

I had a script that modifies the docstrings from a python file. I use meld to pre check if all the changes are correct.

    $ meld clientpackets.py{.new,}

But now I wanted to run the same line but replace just meld with mv. I found the solution [at stackoverflow](http://stackoverflow.com/questions/202610/how-do-i-reuse-a-command-in-bash-with-different-parameters)

    $ !!:s/meld/mv/ mv clientpackets.py{.new,}
