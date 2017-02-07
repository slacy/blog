Title: Did my first clean, successful git merge last night.
Date: 2009-10-13 10:29
Author: slacy
Category: General
Status: published

This is an accomplishment that I think deserves recognition:

Andrea and I have been collaborating on our project via git, and were
working in parallel last night.  And, last night was the first time that
we did a successful merge of our parallel development branches.  Here's
what we did:

-   Steve: git add edited files
-   Steve: git commit
-   Steve: git push
-   Andrea: git add edited files
-   Andrea: git commit
-   Andrea: git pull
-   Andrea: Look at "git status" and see files needing merge.  Edit
    files (by hand) and do the merge
-   Andrea: git add files edited in the previous step
-   Andrea git commit
-   Andrea: git push
-   Andrea: git pull
-   Steve: git pull

Success!  The master repository, Steve & Andrea's working branches were
merged!  Hooray!

Hopefully this won't be a horrible process of lost files, clobbered
changes, and misc junk next time!
