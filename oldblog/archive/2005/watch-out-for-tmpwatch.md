Title: Watch out for tmpwatch.
Date: 2005-04-22 07:00
Author: slacy
Category: General
Status: published

Okay, so lets say you're doing a download of about (what should be) 18Gb
of music files, and you're putting them in /tmp before you copy them
into your music folder.

When the download appears to finish, 3 days later, you notice that you
only have 5Gb of files, and that there are huge chunks of files missing.
What happened?

A.) There were HTTP errors and some files did not respond.  
B.) The serving website found out what you were doing, and stopped you.  
C.) tmpwatch ran in the middle of the night and deleted huge chunks of
valuable data.  
D.) You ran out of disk space.

The answer, my friends, is C. What was happening was that tmpwatch runs
on a nightly basis, and deletes things that it thinks are more than 10
days old. Even these files were just downloaded, wget makes their
modification times match the HTTP headers so that it can compare them
later and redownload the ones that have changed. Therefore, the files
that seemed "new" to you actually had a modification time of months ago.

The man page for tmpwatch says that it tries to look at access time, but
seemingly, writing the file isn't considered accessing it, so it deleted
them all. So, the download process took 3 days, but tmpwatch ran twice,
so over 2/3 of the data was deleted. I got just under 6Gb. I'm
recovering, but slowly. This time I'm limiting wget's download rate so
that it doesn't max out my DSL. It should take another week or so to
complete, I think.

Lesson learned: Always download directly into your music folder, not
into /tmp.  
  

