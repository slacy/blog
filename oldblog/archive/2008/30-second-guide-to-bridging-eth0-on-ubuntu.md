Title: 30 second guide to bridging eth0 on Ubuntu
Date: 2008-03-18 20:13
Author: slacy
Category: General
Tags: br0, bridging, eth0, networking, ubuntu
Status: published

So, you want to switch eth0 from a 'direct' network connection to using
a software bridge? Ok, here's your 30 second guide. If you're using
DHCP, make your /etc/network/interfaces look like this:

> \# This file describes the network interfaces available on your
> system  
> \# and how to activate them. For more information, see interfaces(5).
>
> \# The loopback network interface  
> auto lo  
> iface lo inet loopback
>
> auto br0  
> iface br0 inet dhcp  
> \# Ports you want to add to your bridge  
> bridge\_ports eth0  
> \# Time to wait before loading the bridge  
> bridge\_maxwait 0

And then reboot your machine or run "/etc/init.d/networking restart".
Voila. All your traffic now goes through the software bridge.

Background: This is useful for when you want to run multiple virtual
machines, and give them all independent access to the network. The
virtual machines need virtual interfaces, and therefore, all the
interfaces (both the virtual ones and the 'real' eth0) have to go
through the bridge and out to the network. So, once you've bridged eth0,
its easy enough to add virtual interfaces (tap/tun) and use those.
