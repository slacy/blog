Title: git rebase HEAD says settings.py: needs update
Date: 2009-09-23 20:11
Author: slacy
Category: General
Status: published

I'm running:

    $ git rebase HEAD 
    settings.py: needs update

What does this mean?

    $ git update settings.py
    git: 'update' is not a git-command. See 'git --help'.

GIT HAS THE WORST ERROR MESSAGES OF ANY PROGRAM EVER WRITTEN!

Why can't it just say "hey, I think you need to run "git fobaz
--frobzang core.zangBinger wowPop HEAD origin/master settings.py"

That would be better than "needs update" which is totally ambiguous.
