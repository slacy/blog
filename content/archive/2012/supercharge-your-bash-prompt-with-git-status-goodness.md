Title: Supercharge your bash prompt with git status goodness.
Date: 2012-06-12 14:45
Author: slacy
Category: General
Status: published

Here's a thought:

Wouldn't it be awesome if your bash prompt could show you:

-   Your current working directory.
-   Which git repository you're currently in.
-   Which git branch you're currently on (if not master).
-   How many outstanding files you have (files that need to be
    added or committed).
-   How many changes ahead (or behind) origin/HEAD you currently are.
-   Your current virtualenv (for Python development, but doesn't hurt
    other languages)

Well, all this is possible (and more, probably!).  I worked a bit on
getting all these features working this afternoon.  The source code is
pretty rough, but I think this could be useful enough for others that I
should start to share it.  I'll likely put this in it's own github
repository eventually.  But, for now, here's a simple [gist with my
\~/.bash\_prompt source.](https://gist.github.com/2920594)

To use this, just copy it to your home directory, and add the following
to the bottom of your \~/.bashrc:

source \~/.bash\_prompt
