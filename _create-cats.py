import os
cats = [
    "android",
    "autojump",
    "bash",
    "cli",
    "cyanogenmod",
    "download",
    "food",
    "google",
    "image magick",
    "indexing",
    "inotify",
    "linux",
    "little helpers",
    "movies",
    "picasa",
    "pitfalls",
    "privacy",
    "programming",
    "python 2",
    "python",
    "sed",
    "settings",
    "sphere cam",
    "staatstrojaner",
    "ubuntu",
    "vim",
    "virtualenv",
    "windows",
    "xmacro",
]

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
