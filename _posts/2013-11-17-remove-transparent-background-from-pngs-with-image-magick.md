---
title: "remove transparent background from pngs with image magick"
layout: post
categories:
 - linux
 - cli
 - image magick
---

I created some business cards with inkscape and exported high resolution pngs. But every white spot on the card is transparent. Here is image magick command if you want to get rid of it without adding a white background layer or edit the file by hand with gimp.

    convert card.png -flatten card-white.png

If you want to change multiple files in place, just use mogrify:

    mogrify -flatten *.png

You can even chose the background color as text `-background black` or hex value `-background "#333"` or `-background "#fefefe"`. You have to set the background before you flatten the image.

    convert card.png -background "#aaa" -flatten card-gray.png

I found the [solution][link] to this problem on [stackoverflow][link].

[link]: http://stackoverflow.com/questions/2322750/replace-transparency-in-png-images-with-white-background