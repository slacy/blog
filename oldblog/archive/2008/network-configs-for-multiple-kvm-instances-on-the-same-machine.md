Title: Network configs for multiple KVM instances on the same machine.
Date: 2008-04-23 15:00
Author: slacy
Category: General
Status: published

You need to give them all different MAC addresses, and you need to
change /etc/udev/rules.d/70-persistent-net.rules on each one so that
eth0 is always the MAC address that you've assigned to that machine
(otherwise it ends up as eth1 and the network doesn't properly come up)

Thanks to
[ubuntuforums.org](http://ubuntuforums.org/showthread.php?t=608452).
