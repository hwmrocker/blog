---
title: "ansible, bash and patterns"
layout: post
categories:
 - ansible
 - bash
 - linux
---

I wanted to use ansible to quickly check on a bunch of servers which version of puppet they run.

    ansible -i workhosts all -m raw -a "puppet --version" -K -s

Three servers had a different version, now i wanted just to check the servers not in the live group.

    ansible -i workhosts all:!live -m raw -a "puppet --version" -K -s
    bash: !live: event not found

Bash will try to lookup the last command from the history that starts with live and try to replace this term with it. Even "double quotaions" doesn't stop it. As I found [here][here] you need to use single quotes like this:

    ansible -i workhosts 'all:!live' -m raw -a "puppet --version" -K -s

[here]:https://stackoverflow.com/questions/21051151/why-can-i-not-use-an-exclamation-mark-in-bash-echo-not-even-when-it-is-escaped