---
title: "Sorted tag cloud that support spaces"
layout: post
categories:
 - jekyll
---

Tobias Sjösten wrote [a nice article] about how to create a tag cloud in jekyll without using any plugin. But one thing bothered me a little. The tags came in the order, how they where introdouced in the blog posts. I wanted them to be sorted alphabetically.

On stackoverflow was a [solution][so] to iterate over an hash ordered by its keys. I improved it a little, so we can use spaces and underscores and mixed them together.

Tobias iterated directly over the categories:

    {{"{%"}} for category in site.categories %}
      ...
    {{"{%"}} endfor %}

And he accessed the category name with `category | first` and the list of posts with `category | last`.

    {{"{%"}} capture cat_list %}{{"{%"}} for cat in site.categories %}{{ cat | first }}{{"{%"}} if forloop.last != true%}|{{"{%"}} endif %}{{"{%"}} endfor %}{{"{%"}} endcapture %}
    {{"{%"}} assign sorted_cats = cat_list | split:'|' |  sort %}

Now I can just iterate over the sorted list like that:

    {{"{%"}} for catname in sorted_cats %}

To access the the posts from a category we can just do this: `site.categories[catname]`.

Here is my final tag cloud:

    <ul class="tagcloud">
      {{"{%"}} capture cat_list %}{{"{%"}} for cat in site.categories %}{{ cat | first }}{{"{%"}} if forloop.last != true%}|{{"{%"}} endif %}{{"{%"}} endfor %}{{"{%"}} endcapture %}
      {{"{%"}} assign sorted_cats = cat_list | split:'|' |  sort %}
      {{"{%"}} for catname in sorted_cats %}
        <li style="font-size: {{"{{"}} site.categories[catname] | size | times: 100 | divided_by: site.categories.size | plus: 70 }}%" class="tag">
          <a href="/posts-about/{{"{{"}} catname | slugize }}/">
            {{"{{"}} catname }}
          </a>
        </li>
      {{"{%"}} endfor %}
    </ul>

If you want to know how the tag cloud works, read the [article][link] from Tobias.

[link]: http://vvv.tobiassjosten.net/jekyll/jekyll-tag-cloud/
[so]: http://stackoverflow.com/questions/6387540/how-to-sort-a-hash-converted-to-an-array-in-liquid