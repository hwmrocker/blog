---
title: "Delete remote tags with git"
layout: post
categories:
 - git
---

I recently needed to do this.

```bash
git tag -d 12345
```

But i realized, that these tags where just deletet locally. Even a `push --tags` didn't help. But luckily I found [this blog post][url]. You need to do this push to force a deletion.

```bash
git push origin :refs/tags/12345
```

[url]: http://nathanhoad.net/how-to-delete-a-remote-git-tag