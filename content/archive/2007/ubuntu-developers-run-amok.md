Title: Ubuntu developers run amok.
Date: 2007-09-27 08:16
Author: slacy
Category: General
Status: published

I'm not an Ubuntu user, so when I found out that the next version of
Ubuntu will *not* use [bash](http://www.gnu.org/software/bash/) as its
default shell for /bin/sh, I was really surprised. Funny enough, they've
decided to use [dash](http://gondor.apana.org.au/~herbert/dash/) instead
of bash, because its 'more POSIX-compliant' and because it has slightly
higher performance, making all your shell scripts run faster.

The funny thing is, this is just a horrible idea. I'll go through the
reasons:

1\. bash has been the default shell for nearly a decade, and thus, most
scripts are written in bash syntax, and sometimes use bash features even
though it says "\#!/bin/sh" at the top of the file. The Ubuntu
developers say "well, thats a broken script that needs to be fixed"
without any regard for what this will mean for their users.

2\. Having the login shell different from the scripting shell is a really
bad idea. This is like someone living in Spain teaching their kids to
speak Esperanto at home. It'll just lead to mass confusion.

3\. Shell scripting performance? Seriously, who cares? One of the use
cases that they quote in their
[DashAsBinSh](https://wiki.ubuntu.com/DashAsBinSh) wiki page is that
./configure for OpenOffice runs 2 minutes faster. Do I care? This is a
one time script, and even so, *no one actually runs it*! (other than the
guy who builds the OpenOffice packages). Even as a programmer employed
at a large & well-known web software company, I probably run ./configure
scripts one a week at tops, and more likely, once a month, and only for
my personal projects.

4\. If bash is so horribly slow, then why not spend your effort profiling
it and improving it?

You can read [a great bug
report](https://bugs.launchpad.net/ubuntu/+source/dash/+bug/61463) with
lots of follow-up replies from both the Ubuntu developers and real
users. Funny thing is, the Ubuntu developer community is being a stick
in the mud, and is really committed to dash. What hubris!

As a side note, they no longer use the catchphrase ["Ubuntu, Linux for
humans"](https://launchpad.net/bounties/all-linux-for-humans). I guess
it should be "Ubuntu, Linux for Ubuntu developers on a silly performance
rampage that brakes reasonable behavior for everyone else".

And I thought I would switch away from Fedora someday... guess not!
