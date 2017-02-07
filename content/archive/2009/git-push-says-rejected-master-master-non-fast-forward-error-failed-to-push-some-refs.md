Title: git push says rejected master - master (non-fast forward) error: failed to push some refs
Date: 2009-09-23 20:37
Author: slacy
Category: General
Status: published

If you're seeing an error like this:

    $ git push
    To ssh://userid@example.com/home/git/repository
     ! [rejected]        master -> master (non-fast forward)
    error: failed to push some refs to 'ssh://userid@example.com/home/git/repository'

Then it means you need to run "git pull" first. Of course.

GIT HAS THE WORST ERROR MESSAGES OF ANY PROGRAM EVER WRITTEN!
