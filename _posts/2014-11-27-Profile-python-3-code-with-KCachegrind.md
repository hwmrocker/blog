---
title: "Profile python 3 code with KCachegrind"
layout: post
categories:
 - programming
 - python
 - python 3
---

Grab [this script][script] and run yours like this:

```bash
python3 lsprofcalltree.py <your_script.py>
```

and analize it with [kcachegrind][kcachegrind].

```bash
kcachegrind <your_script.py.log>
```

I found the [original script][lsprofcalltree] at [python.org][profiling].


[lsprofcalltree]: https://people.gnome.org/~johan/lsprofcalltree.py
[revisions]: https://gist.github.com/hwmrocker/0ad625369feadd57d8c6/revisions
[script]: https://gist.github.com/hwmrocker/0ad625369feadd57d8c6/
[profiling]: https://wiki.python.org/moin/PythonSpeed/Profiling
[kcachegrind]: http://kcachegrind.sourceforge.net/html/Home.html
