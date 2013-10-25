#!/usr/bin/env python
import os

template = """---
layout: none
---
{% for cat in site.categories %}{{ cat | first }}
{% endfor %}
"""
with open("deletme.html", "w") as fh:
    fh.write(template)

os.system("jekyll build")
with open("_site/deletme.html") as fh:
    cats = sorted([c.strip() for c in fh.readlines() if c.strip()])

#clean up again
os.system("rm _site/deletme.html deletme.html")

template = """---
layout: default
title: Your New Jekyll Site
---
<div id="home">
  <h2>Blog Posts about %(catname)s</h2>
  <ul class="posts">
  {%% for post in site.categories["%(catname_raw)s"] %%}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
  {%% endfor %%}
  </ul>
</div>"""

for cat in cats:
    os.system('mkdir -p "posts-about/%s"' % cat)
    with open("posts-about/%s/index.html" % cat, 'w') as fh:
        fh.write(template % {"catname": cat.title(), "catname_raw":cat})
    os.system('git add "posts-about/%s"'%cat)
