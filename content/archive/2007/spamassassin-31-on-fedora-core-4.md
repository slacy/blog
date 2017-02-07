Title: Spamassassin 3.1 on Fedora Core 4
Date: 2007-01-15 19:53
Author: slacy
Category: Linux Stuff
Status: published

Well, I finally bit the bullet.

Spam has been flooding into my mailbox recently, and Spamassasin 3.0
just wasn't cutting it. I had hesitated to install Spamassassin 3.1
because there was no "official" Fedora Core 4 RPM around. I had 3
options: Upgrading my whole machine to FC6, installing Spamassassin from
source, or getting it through CPAN. I wasn't sure what to do.

It turns out that installing from source is totally the way to go.
Spamassassin provides a tarball and easy instructions on building your
own rpm straight from the source. So, I download the source pack, and
ran rpmbuild, per their
[instructions](http://spamassassin.apache.org/downloads.cgi?update=200610100328).
The RPM was quickly built, and I ran "rpm --upgrade" on them.

Everything went amazingly smoothly, and my spam today has been greatly
reduced. Messages that used to get less than a 5.0 and miss my filter
are now scoring in the mid-30's. The biggest rule improvements are the
URL blackhole lists, which account for the majority of the big boosts in
score.

Thanks, Spamassassin!
