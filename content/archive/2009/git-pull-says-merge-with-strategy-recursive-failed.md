Title: git pull says Merge with strategy recursive failed.
Date: 2009-09-23 20:09
Author: slacy
Category: General
Status: published

I'm running:

    $ git pull
    error: Entry 'settings.py' not uptodate. Cannot merge.
    fatal: merging of trees ad161889ded7144b034a6ec36cf452b2508280a9 and beb9642a3abc785ccaab06c4b266e830b6389847 failed
    Merge with strategy recursive failed.

I don't understand what I'm supposed to do here.  I thought maybe "git
merge" but that's not helpful.

I have settings.py modifed in my local client, and what I want to do is
pull from the origin and merge in the latest changes into my local
repository.  I don't want to have to commit settings.py, but I guess I
could (and just not push it).

**UPDATE:**

I've been using git for a while now, and I now know that the right thing
to do when you get this message is to **git add** and then **git
commit** the file that's failing to merge, then do the **git pull**
again.  You're not guaranteed to not get conflicts, but that's another
story.

GIT HAS THE WORST ERROR MESSAGES EVER!
