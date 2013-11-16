---
title: "strip color codes with sed"
layout: post
categories:
 - linux
 - cli
 - sed
---

    sed -r "s:\x1B\[[0-9;]*[mK]::g" file

I found this solution on [commandlinefu][link]

[link]: http://www.commandlinefu.com/commands/view/3584/remove-color-codes-special-characters-with-sed