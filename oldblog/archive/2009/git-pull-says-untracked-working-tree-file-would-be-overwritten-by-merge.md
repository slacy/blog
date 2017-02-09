Title: git pull says Untracked working tree file ... would be overwritten by merge.
Date: 2009-09-23 20:21
Author: slacy
Category: General
Status: published

I'm trying to get my client back to some reasonable state, and I just
can't do it.

What I know:

-   I have (had?) some very minimal changes to a couple of local files.
-   Another user had added several new files and directories
-   I just want to "git pull" in the other user's changes, and merge
    them with my locally edited files.
-   I have comitted my locally edited files, but not yet done "git push"
    because I don't want those edits back on the origin/master.

When I run git pull, it says:

    $ git pull
    error: Untracked working tree file 'auth/__init__.py' would be overwritten by merge.
    fatal: merging of trees 0e6c93c1d03a08c1f8b14cf76096979064112349 and beb9642a3abc785ccaab06c4b266e830b6389847 failed
    Merge with strategy recursive failed.

What am I supposed to do now?  I'm tempted to just nuke this whole
repository and start over, since my changes are so minimal, but I'm
determined to understand & figure out git so that I don't have to go
through this nonsense every time.

    $ git status 
    # On branch master
    # Your branch and 'origin/master' have diverged,
    # and have 2 and 9 different commit(s) each, respectively.
    [...]

What does this mean? Does this mean that I have 2 commits, and that
origin/master has 9?  How do I merge these commits in together?  Do I
have to manually "git log" them and then "git merge"?  Argh!

GIT HAS THE WORST ERROR MESSAGES OF ANY PROGRAM I'VE EVER SEEN!
