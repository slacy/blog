Title: Running do-release-upgrade or 'apt-get dist-upgrade' on an LXC container.
Date: 2014-10-17 14:37
Author: slacy
Category: General
Status: published

I've found that running do-release-upgrade or even a "apt-get
dist-upgrade" on a containerized machine instance using LXC won't
actually complete successfully.  I found a [post on
ubuntuforums](http://ubuntuforums.org/showthread.php?t=1863056)
explaining the solution, but wanted to capture it here for my own
reference.

    # First make sure to stop the LXC machine using
    # either lxc-stop or the virt-manager GUI or
    # commandline. 

    $ cd <directory that contains the lxc image> 
    $ sudo su - 
    # mount -t devpts devpts ./dev/pts 
    # mount -t proc proc ./proc 
    # mount -t sysfs sysfs ./sys
    # chroot .
    # apt-get dist-upgrade 
    # do-release-upgrade 
    # <Ctl-D to exit chroot> 
    # umount ./dev/pts
    # umount ./proc 
    # umount ./sys

I also had at least one case on one container where the
do-release-upgrade or dist-upgrade process had messed with
/etc/resolv.conf, and I needed to make sure to put an entry in there for
8.8.8.8 so that the subsequent commands worked.  That was done manually,
and was fixed by network-manager when the container was finally booted
after the update.

Using this technique, I have several LXC containers running 14.04 on my
12.04 machine.  Pretty cool.
