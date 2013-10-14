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
    "index",
    "inotify",
    "linux",
    "little helpers",
    "movies",
    "picasa",
    "pitfalls",
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
  <h1>%(catname)s Blog Posts</h1>

  <ul class="posts">
  {%% for category in site.categories %%}
    {%% if category[0] == "%(catname_raw)s" %%}
      {%% for post in category[1] %%}
  <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
      {%% endfor %%}
    {%% endif %%}
  {%% endfor %%}
  </ul>
</div>"""

for cat in cats:
    os.system('mkdir -p "%s"' % cat)
    with open("%s/index.html" % cat, 'w') as fh:
        fh.write(template % {"catname": cat.title(), "catname_raw":cat})
    os.system('git add "%s"'%cat)