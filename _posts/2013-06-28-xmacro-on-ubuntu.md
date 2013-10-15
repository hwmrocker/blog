---
layout: post
title: "xmacro on Ubuntu"
date: 2013-06-28
comments: false
categories:
 - linux
 - ubuntu
 - xmacro
 - little helpers
---

Install it with:
    
    sudo apt-get install xmacro

Record the macro:

    xmacrorec2 > yourfile.txt

Now record your keystrokes and mouse movements, to end it just hit `Esc`.

To play it back, just run it using the text file like so:

    xmacroplay "$DISPLAY" < yourfile.txt

Tip: In my case this wasn't enough because the replay was too fast. I just opend the txt file with an text editor and added some of these Lines:

    Delay 1

Now it works like a charm :)
