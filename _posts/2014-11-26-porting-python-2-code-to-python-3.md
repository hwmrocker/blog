---
title: "Porting python 2 code to python 3"
layout: post
categories:
 - python 2
 - python 3
 - python
 - programming
 - free software
---

I needed to profile a python 3 script of mine. During this process if wanted to use a great [helper script][lsprofcalltree] but it was not compatible with mine, so i had to port it to python 3.
Porting python 2 code to python 3 is really easy, thanks to ``2to3``. The last time i ported a library all I had to do was to call ``2to3 -w`` and it worked.

This time it didn't worked as smoothly, but it was very easy to change the last bits. The whole process took no longer than 5 minutes.

The first step was to run ``2to3``.

```
2to3 -w lsprofcalltree.py
```

After I tried to run the code, I got two `NameError` messages.

```
NameError: name 'execfile' is not defined
NameError: name 'file' is not defined
```

The file problem was a really easy fix, all I neede to do was replace it with file

{% highlight diff %}
@@ -112,12 +112,12 @@ def main(args):
         except SystemExit:
             pass
     finally:
         kg = KCacheGrind(prof)
-        kg.output(file(options.outfile, 'w'))
+        kg.output(open(options.outfile, 'w'))
 
 if __name__ == '__main__':
{% endhighlight %}

The second change was a little bit bigger. Since ``execfile`` was inside a string that got evaluatet, 2to3 didn't catch this change. I created an empty new python file with just an execfile statement run 2to3 to see how the new output looked and applied those changes to the new file.

{% highlight diff %}
@@ -108,12 +108,12 @@ def main(args):
     prof = cProfile.Profile()
     try:
         try:
-            prof = prof.run('execfile(%r)' % (sys.argv[0],))
+            prof = prof.run("exec(compile(open(%r).read(), %r, 'exec'))" % (sys.argv[0],sys.argv[0]))
         except SystemExit:
             pass
     finally:
         kg = KCacheGrind(prof)
{% endhighlight %}

You can see all the [different versions][revisions] after each step and the [final result][script] at github. And the best, it's MIT licensed.

[lsprofcalltree]: https://people.gnome.org/~johan/lsprofcalltree.py
[revisions]: https://gist.github.com/hwmrocker/0ad625369feadd57d8c6/revisions
[script]: https://gist.github.com/hwmrocker/0ad625369feadd57d8c6/
[profiling]: https://wiki.python.org/moin/PythonSpeed/Profiling
[kcachegrind]: http://kcachegrind.sourceforge.net/html/Home.html