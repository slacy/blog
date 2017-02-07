Title: Installing Ubuntu under KVM under Ubuntu
Date: 2008-03-29 20:45
Author: slacy
Category: General
Status: published

Here's the commandline that you'd use to install Ubuntu under KVM under
Ubuntu. I'm using Gutsy, so this may not work with newer or older
versions.

First, I recommend that you see [my post on bridging
eth0](http://slacy.com/blog/index.php/2008/03/18/30-second-guide-to-bridging-eth0-on-ubuntu/).
Do that first.

Then, run the following:

> sudo kvm -no-kvm -net nic -net tap -vnc :1 -hda root-base-10G.img -hdb
> home-base-200G.img -hdd var-base-50G.img -cdrom
> ../install\_imgs/ubuntu-7.10-server-i386.iso -boot d

Note how I've passed 3 different disks, one for "root", one for "home"
and one for "var" (and /tmp). I think this will be a good configuration
because these "base" images will be shared across multiple machines via
qemu overlays (more on that later). And there's a totally separate disk
for "home", which is where most of the user data will go.
