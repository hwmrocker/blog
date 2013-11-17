---
title: "git commandline completion"
layout: post
categories:
 - linux
 - bash
 - cli
 - git
 - little helpers
---
The git repo on github has a nice helper function for better tab completion for git. In case you type: git add `TAB` `TAB` you get a list of files that changed, or a new in your repo. If there is only one it will auto complete it. To install it copy the *git-completion.bash* to home folder, or use this code:

    wget https://raw.github.com/git/git/master/contrib/completion/git-completion.bash \
    -O ~/.git-completions.bash

To activate it and test if the completion works now as expected.

    . ~/.git-completion.bash

To activate it automatically when you open a terminal.

    echo ". ~/.git-completion.bash" >> "~/.bashrc"