---
title: "convert a bunch of images to jpg"
layout: post
categories:
 - linux
 - cli
 - image magick
---

If you have a couple of png files and want them smaller, e.g. screenshots from high resolution tablets or phones:

    mogrify -format jpg *.png; rm *.png