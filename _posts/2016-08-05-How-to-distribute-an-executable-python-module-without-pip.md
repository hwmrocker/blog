---
title: "How to distribute an executable python module without pip"
layout: post
categories:
 - python
 - linux
 - bash
---

This will only work on linux, Free BSD, and probably Mac OS. Here is a simplified version of the file tree.

    $ tree
    .
    ├── boerewors
    │   ├── command_line.py
    │   ├── errors.py
    │   ├── helper.py
    │   ├── __init__.py
    │   └── warmup.py
    ├── __init__.py
    ├── __main__.py
    ├── setup.py
    └── tests
        ├── helpers.py
        ├── __init__.py
        └── test_warmup.py

`boerewors` is a python module that we want to distribute. In case we want to distribute this package to a server without pip and without root privileges we can run this little shell script:

    mkdir -p dist
    zip -r dist/tmp.zip boerewors -x \*.pyc
    zip dist/tmp.zip __main__.py
    echo "#!/usr/bin/env python" > dist/warmup
    cat dist/tmp.zip >> dist/warmup
    chmod +x dist/warmup
    rm dist/tmp.zip

This script zips the python module, creates file with a python shebang appends the zip file to it and marks it executable. The entry point of this executable is \__main__.py which contains only this lines:

    from boerewors.command_line import main
    main()

This file can now be copied to the server where we want to execute it. We are not bound to write our script in one file and even have test for development.
