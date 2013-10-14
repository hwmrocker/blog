---
layout: post
title: "python tell"
date: 2013-06-28
comments: false
categories:
 - Python
 - pitfalls
 - indexing
---

Maybe you think that both examples would produce the same output, but the tell of the filehandler will give you a wrong output in the first version. This version is a bit faster but in this case also a bit inaccurate.

{% highlight python %}
infh = open("bigfile")
print infh.tell()
for line in infh:
    # ...
    print infh.tell()
    line = infh.readline()
{% endhighlight %}

{% highlight python %}
infh = open("bigfile")
print infh.tell()
line = infh.readline()         
while len(line) > 0:
    # ...
    print infh.tell()
    line = infh.readline()
{% endhighlight %}

