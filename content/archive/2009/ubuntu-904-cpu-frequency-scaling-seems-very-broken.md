Title: Ubuntu 9.04 CPU frequency scaling seems very broken
Date: 2009-04-27 14:47
Author: slacy
Category: General
Status: published

I just installed Ubuntu 9.04 on my Lenovo S10 (Intel Atom N270 @ 1.6GHz)
netbook, and have had some serious performance issues after installing. 
[Others have noticed similar
issues](http://jasondclinton.livejournal.com/72910.html).

In short, the machine never goes any faster than 800MHz, no matter what
I'm doing.  What's supposed to be happening is that the cpufreq module
(now compiled into the kernel instead of a loadable module) should be
increasing the processor speed when it detects high CPU usage.  For all
intents and purposes, this feature is 100% broken on my machine.   I can
manually override the cpufreq governor to set it to "performance" and
the machine becomes a fair bit more responsive, but uses a lot more
power.

It does look like there are several ways to make the default policy
"performance" and for the short term, I'm going to be doing this so that
my machine works at a reasonable pace.

I've also filed a [bug with
launchpad.net](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/367739)
and we'll see if that gets any traction.  There does seem to be a large
number of "cpufreq stuck" types of bugs in launchpad, which is very
discouraging. Even worse, /etc/init.d/loadcpufreq seems to not have been
updated to reflect that acpi\_cpufreq is now compiled into the kernel. 
[This is just
sloppy](https://bugs.launchpad.net/ubuntu/+source/sysvinit/+bug/368231).

I also suspect that this "hidden bug" is effecting a \*lot\* more 9.04
users than people think.  In general, when a fast 3GHz machine "only"
runs at 1.5GHz, it's a perfectly fine situation and most users won't
notice it.   But, when a 1.6GHz machine is stuck at 800Mhz, it's a
pretty big deal.
