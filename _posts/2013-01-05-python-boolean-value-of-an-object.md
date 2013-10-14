---
layout: post
title: "Python boolean value of an object"
date: 2013-01-05
comments: false
categories:
 - Python 2
 - programming
 - Python
---
This is helpfull if want to use Mock-objects in Case an Object is not available, but still want to know if a real object is available or not. I found the [solution][link] at [stackoverflow][link].

{% highlight python %}
class Foo(object):
    def __init__(self, bar):
        self.bar = bar
    def __nonzero__(self):
        return self.bar % 2 == 0
{% endhighlight %}

[link]: "http://stackoverflow.com/questions/1087135/boolean-value-of-objects-in-python"