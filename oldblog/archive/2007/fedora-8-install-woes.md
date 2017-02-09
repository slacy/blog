Title: Fedora 8 install woes.
Date: 2007-12-12 18:40
Author: slacy
Category: General
Tags: anaconda, Fedora 8, hang, installer
Status: published

I tried to install Fedora 8 last night, and just like the last 2 or 3
Fedora upgrades, it failed. This time the problem is that the installer
(anaconda) hangs at about 25% done "resolving dependencies" Ugh. I
strace'd anaconda and found that it was trying to do something in /tmp,
/usr/tmp, and /var/tmp (god knows what), and was using up 100% of my
CPU.

After a bit of searching I found a link to the bug ["depsolve hang in F7
to F8 upgrade"&gt;](https://bugzilla.redhat.com/show_bug.cgi?id=372011)
(of course!)

Seems like they have some kind of updates patch for the Fedora 8
installer, but it hasn't yet been rolled into the released images. Ugh.
You can read about it more on the [Fedora 8 common
bugs](https://fedoraproject.org/wiki/Bugs/F8Common) wiki page. There's
nothing like a "common bugs" page to make you feel **really** confident
about a linux distro.

Any suggestions about how I could move my system from FC6 to Ubuntu?
User data via backups is easy, but I'm loathed to even think about
trying to replicate my postfix, mysql, and httpd configs in a new
distro...
