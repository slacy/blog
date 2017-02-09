Title: Why doesn't Fedora Core include spamassassin 3.1?
Date: 2006-08-30 11:10
Author: slacy
Category: Linux Stuff
Status: published

I've been battling all the image spam thats been happening lately, and
my current solution has been to look at the messages that make it
through my spam filters, and boost the scores for those rules.

The weird part is that my Fedora Core 4 installation has
spamassassin-3.0.6, and the latest is version 3.1. So, I've just been
copying the 3.1 scores from the [spamassassin tests
page](http://spamassassin.apache.org/tests_3_1_x.html) and putting those
in /etc/mail/spamassassin/local.cf. Its worked pretty well, and cut down
some of the spam. I did have to boost RECV\_IN\_XML up to 15 to catch a
bunch more things, but I think thats fairly safe.

The real question is: Why doesn't the Fedora team get spamassassin 3.1
into the distro?!
