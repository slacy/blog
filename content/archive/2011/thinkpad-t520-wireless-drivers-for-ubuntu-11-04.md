Title: ThinkPad T520 Wireless Drivers for Ubuntu 11.04
Date: 2011-08-31 09:42
Author: slacy
Category: General
Status: published

Just got a new laptop, a ThinkPad T520, and I'm running Ubuntu 11.04
(Natty)

With no additional drivers, the wireless (RealTek 8188ce) would work
somewhat intermittently.  Sometimes it was great, and other times it
wouldn't associate at all.

The correct fix is to connect to a wired network, then add a PPA for the
RealTek compiled drivers, and add the drivers themselves, like this:

``` {dir="ltr"}
sudo add-apt-repository ppa:lexical/hwe-wireless
sudo apt-get update
sudo apt-get install rtl8192ce-dkms
```

After doing that, everything works great. I hope this works for you as
well!

(Found this after Googling for quite a while.
 Source: <http://ubuntuforums.org/showthread.php?t=1580036&page=2>)
