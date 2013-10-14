import os
cats = [
    "linux",
    "cli",
    "image magick",
    "cyanogenmod",
    "android",
    "ubuntu",
    "picasa",
    "download",
    "google",
    "python 2",
    "programming",
    "python",
    "movies",
    "little helpers",
    "autojump",
    "inotify",
    "sed",
    "staatstrojaner",
    "virtualenv",
    "workon",
    "food",
    "windows",
    "sphere cam",
    "index",
    "pitfalls",
    "vim",
    "xmacro",
    "settings",
    "bash",
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