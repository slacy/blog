Title: Archiving GMail without using fetchmail
Date: 2009-07-30 10:27
Author: slacy
Category: General
Tags: archiving, backup, getmail, gmail, libgmail
Status: published

Thanks Paul and Greg for the advice on backing up my GMail account. 
Although fetchmail seems to work for some users, there are a couple of
easier to use scripts out there.

Paul pointed me at [Matt Cutts' great blog post about using the getmail
script to archive
GMail.](http://www.mattcutts.com/blog/backup-gmail-in-linux-with-getmail/)

Greg pointed me at libgmail which comes with some simple driver scripts
to download all your content.  You can get it from [the sourceforge.net
page](http://libgmail.sourceforge.net), and read more on the [libgmail
author's website](http://words.rancidbacon.com).

I'm running a big batch getmail run now, and putting all the messages in
MailDir format.  The thing that I'm actually looking for is a way to
preserve GMail's label structure using hard or soft links in a
MailDir-like format, for easy searching.   I suspect that libgmail will
allow this, but I haven't dug into it enough to know for sure.
