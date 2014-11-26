---
title: "use at to schedule future tasks"
layout: post
categories:
 - linux
 - bash
 - cli
---

You can use this simple form to schedule future tasks.

```bash
echo "git push" | at 12:00
```
or even on another day.

```bash
echo "/etc/init.d/nginx restart" | at 03:00 Nov 25
```

To view task queue use `atq`. And `atrm <jobnumber>` to rm jobs again.
