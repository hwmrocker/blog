---
title: "emerge vlc player in funtoo"
layout: post
categories:
 - linux
 - funtoo
---

When I tried to simply emerge vlc via `sudo emerge -a vlc` i got the following error:

```
  The following REQUIRED_USE flag constraints are unsatisfied:
    httpd? ( lua )

  The above constraints are a subset of the following complete expression:
    aalib? ( X ) bidi? ( truetype ) cddb? ( cdda ) dvb? ( dvbpsi ) dxva2? ( avcodec ) ffmpeg? ( avcodec avformat swscale ) fontconfig? ( truetype ) gnutls? ( gcrypt ) httpd? ( lua ) libcaca? ( X ) libtar? ( skins ) libtiger? ( kate ) qt4? ( X !qt5 ) qt5? ( X !qt4 ) sdl? ( X ) skins? ( truetype X exactly-one-of ( qt4 qt5 ) ) vaapi? ( avcodec X ) vlm? ( encode ) xv? ( xcb )
```

First i had no idea what this lines meant, but it seams that if you want to use `httpd` you need also `lua`.

On [videolan.org][vlc] they give an advice for the minimal set of useflags for the vlc ebuild.

I ended up adding two lines to `/etc/portage/package.use`:

```
media-video/vlc dvd ffmpeg mpeg mad wxwindows aac dts a52 ogg flac theora oggvorbis matroska freetype bidi xv svga gnutls stream vlm httpd cdda vcd cdio live vaapi -qt4 qt5 avahi lua directfb opus samba sdl sdl-image
media-video/ffmpeg vaapi opus samba sdl -ieee1394
```
I had a problem to build the lib for firewire which was a depency for ffmpeg. Since I have no firewire device I just droped it and removed the default useflag `ieee1394`.

[vlc]: https://www.videolan.org/vlc/download-gentoo.html
