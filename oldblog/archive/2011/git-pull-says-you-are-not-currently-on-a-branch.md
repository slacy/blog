Title: git pull says You are not currently on a branch...
Date: 2011-04-04 16:21
Author: slacy
Category: General
Tags: git, github, pip, python
Status: published

Was working through some git error messages generated by pip installs of
some Python code, and found that the issue was caused by this error:

    $ git pull
    You are not currently on a branch, so I cannot use any
    'branch.<branchname>.merge' in your configuration file.
    Please specify which remote branch you want to use on the command
    line and try again (e.g. 'git pull <repository> <refspec>').
    See git-pull(1) for details.

The solution (in this case, per the above directory) is to run:

    $ cd /path/to/git/repository/from/above
    $ git checkout master 

I wish pip didn't cause this problem. When you specfiy a git repository
on the commandline, this should happen automatically. Maybe this has
been fixed in pip 1.0 which was just released today.
