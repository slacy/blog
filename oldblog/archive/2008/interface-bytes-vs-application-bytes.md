Title: Interface bytes vs. application bytes
Date: 2008-04-18 17:05
Author: slacy
Category: General
Status: published

My rsync is throttled to 60kBps (kilobytes per second) which if you
multiply by 8, is 480kbps.

But, mrtg is reporting about 550kbps of actual traffic on my interface.
I suppose this is because of TCP & ethernet overhead. (15% overhead!)
The other crappy part is that by "768kbps" uplink maxes out somewhere
around 685kbps (90% of stated bandwidth) which sort of sucks too.

Anyway, I've throttled back the rsync so that I can surf the web (at
all) and people can maybe still see photos on the gallery. Oh well. The
rsync will likely still take over a week to complete...
