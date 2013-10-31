---
title: "Twitter interview, puddle volume"
layout: post
categories:
 - programming
 - python
 - fun problem
---

I stumbled upon this [blog post][link] about a programming question for during a twitter interview. 

Given this picture of walls with different height:

{% highlight python %}
                 _ _
                |7 7|_
       _        |    6|
      |5|      _|     |
      | |    _|4      |
     _| |  _|3        |
    |2  |_|2          |
    |_ _ 1 _ _ _ _ _ _|
     0 1 2 3 4 5 6 7 8
{% endhighlight %}

The representation of this walls is the array `[2, 5, 1, 2, 3, 4, 7, 7, 6]`. Imagine it will start to rain. How much water would be collected by this walls?

{% highlight python %}
                 _ _
                |7 7|_
       _        |    6|
      |5|~ ~ ~ ~|     |
      | |~ ~ ~|4      |
     _| |~ ~|3        |
    |2  |~|2          |
    |_ _ 1 _ _ _ _ _ _|
     0 1 2 3 4 5 6 7 8
{% endhighlight %}

In this case the correct value would be 10. Micheal had a solution that will iterate over each number 2 times. When I read this, I thought it must be possible to do this in just one round trip. And I [did][mygist].

If you want to try it for yourself, here are some nice test cases that could help you: the tuple has two elements first the array of levels, and then the number of the expected amount of water. In case you find a better/shorter/more elegant solution please comment on [my gist][mygist] or send me an email.

{% highlight python %}
#!/usr/bin/env python
def water(levels):
    # enter your code here
    pass

testcases = [
    ([1,0,1], 1),
    ([5,0,5], 5),
    ([5,0,4], 4),
    ([4,0,5], 4),
    ([4,0,5,0,2], 6),
    ([0,1,0,1,0], 1),
    ([0,1,0,0,1,0], 2),
    ([4,2,2,1,1,1,3], 8),
    ([0,3,2,1,4], 3),
    ([1,0,1,0], 1),
    ([1,0,1,2,0,2], 3),
    ([2,5,1,2,3,4,7,7,6], 10),
    ([5,1,0,1],1),                 # thanks https://news.ycombinator.com/item?id=6640085
    ([2,5,1,2,3,4,7,7,6,3,5], 12), # thanks https://news.ycombinator.com/item?id=6640105
    ([3,0,1,0,2], 5),
]

if __name__ == "__main__":
   for case in testcases:
      w = water(case[0])
      if w == case[1]:
         print "TRUE: %s holds %s" % (case[0], w)
      else:
         print "MISMATCH: %s holds %s (got %s)" % (case[0], case[1], w)
{% endhighlight %}

[link]: http://qandwhat.apps.runkite.com/i-failed-a-twitter-interview/
[mygist]: https://gist.github.com/hwmrocker/7241002/edit