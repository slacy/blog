Title: Cannot make directory '/var/run/screen': Permission denied
Date: 2010-06-25 19:55
Author: slacy
Category: General
Status: published

I just ran an apt-get update ; apt-get dist-upgrade, and noticed that a
bunch of screen-related programs had been updated.

When I tried to run screen, I got this:

    # screen
    Cannot make directory '/var/run/screen': Permission denied

I looked at [this old bug on
launchpad](https://bugs.launchpad.net/ubuntu/+source/screen/+bug/172651),
which seemed to have been fixed ages ago.  But, the last entry is
telling, and mentions /etc/init.d/screen-cleanup.

To fix the problem, either reboot, or run:

    # sudo /etc/init.d/screen-cleanup start

And it'll be fixed. You're welcome.
