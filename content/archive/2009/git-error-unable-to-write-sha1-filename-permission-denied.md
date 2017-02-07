Title: git error unable to write sha1 filename ... Permission denied
Date: 2009-09-23 19:49
Author: slacy
Category: General
Tags: git, linux, sha1, ssh
Status: published

I was having the following issue while doing a "git push":

    $ git push
    Counting objects: 50, done.
    Compressing objects: 100% (33/33), done.
    Writing objects: 100% (36/36), 4.42 KiB, done.
    Total 36 (delta 13), reused 0 (delta 0)
    error: unable to write sha1 filename ./objects/fc/0bf175cf9bf2ecdf15eee84adad32230107aa7: Permission denied

    fatal: failed to write object
    error: unpack failed: unpacker exited with error code
    To slacy@myhost.com:/home/git/name-of-repo
     ! [remote rejected] master -> master (n/a (unpacker error))
    error: failed to push some refs to 'slacy@myhost.com:/home/git/name-of-repo'

The issue turned out to be that because I'm using ssh + git to push the
files, the files in the .git/objects directories are created with the
user+group of the user on the host.  So, the first user to create the
file makes them with their own userid & groupid, and are set with
default permissions as u=rxw,g=rx,o=rx, and thus, when the second user
comes it to add a new file to that pre-existing subdirectory, they don't
have permissions.

I tried to solve this issue by creating "group git" and adding all users
who are using the repository in /home/git/name-of-repo, but it still
turns out that new files are created with userid:groupid as user:user
not user:git.

How do you get around this issue?  How do I make it so that new
directories created by git during the push process are given the correct
permissions (u=rxw,g=rxw,o=) and assigned to group git instead of the
user group?

This issue is easy enough to fix manually, by doing something along the
lines of:

    $ ssh userid@myhost.com
    (myhost.com)$ cd /home/git/name-of-repo/.git/objects
    (myhost.com)$ find . type d | xargs chgrp git
    (myhost.com)$ find . type d | xargs chmod g=rxw

But, I'm going to have to continue to do this as new directories in the
"objects" area are going to continue to be created with the wrong
permissions.

GIT HAS THE WORST ERROR MESSAGES IN ANY PIECE OF USER-FACING SOFTWARE
I'VE EVER SEEN.

There, I said it. Peace out.

UPDATE:
-------

Just read about the git config setting "core.sharedRepository" which
will automatically give group rwx permissions to newly created files in
the repository.  So, I ran:

    $ git config --add core.sharedRepository group
