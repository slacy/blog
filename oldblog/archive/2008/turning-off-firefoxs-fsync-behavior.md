Title: Turning off Firefox's fsync() behavior.
Date: 2008-12-04 11:23
Author: slacy
Category: General
Status: published

Firefox 3.x tends to like to fsync() its sqlite database frequently.
(see
[here](http://www.dslreports.com/forum/r20716906-Firefox-3-fsync-issue))
and this can cause the browser to lock up periodically under high disk
or CPU load.

There are several ways to mitigate this.

1.  Switch your local disk drive (Linux) to data=writeback by adding
    this to your /etc/fstab (see instructions elsewhere)
2.  Use FF's about:config to set the preference
    "toolkit.storage.synchronous" to "0" (it's an integer)

I've done \#2, and it seems to work great.  I've yet to see corruption
of my bookmarks / awosome bar and I'm seeing reduced freezes.
