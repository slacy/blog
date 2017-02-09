Title: 365GB @ 50kBps = 88 days
Date: 2008-12-29 15:00
Author: slacy
Category: General
Status: published

So, I finally set up a script to back up my entire computer (365GB of
content, as we speak) to my remotely hosted machine.

This gives me an offsite backup of important files that I may have here,
in case of disaster.

But, there's a catch.  First, my uplink speed from home is only 768kbps,
good for about 75kBps.  And, I don't want to use 100% of that, because
at that rate, it would still take 59 days to rsync everything.

So, I've throttled it back to 50kbps, so that I can still listen to
music at work (128kbps or so) and still get reasonable performance from
web surfing.  But, at that rate, it'll take 88 days to sync all the
content.   Other than walking the drives over to the colo, is there any
better way?

By the way, if you'd like the Python script that initiates the rsync,
let me know.  It has a bunch of smarts in it to manage multiple backups
from multiple days without duplicating the content, etc.  Its an Python
adaptation/rewrite of a script that I've been using to back up the same
files locally to a big USB enclosure.

I know there's probably a host of remote backup managers, but I mostly
wanted something simple and straightforward.  I looked a bit at
rdiff-backup, but that seemed too heavyweight, and when I tried to run
it, I got weird errors because the versions of it are different on the
local & remote machines, and it made me really nervous that it's all
fucked up.  Rsync + ssh has been around for ages, and will continue to
work for ages.
