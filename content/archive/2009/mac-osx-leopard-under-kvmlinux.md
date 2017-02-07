Title: Mac OSX Leopard under KVM/Linux
Date: 2009-02-04 14:51
Author: slacy
Category: General
Tags: Add new tag, kvm, linux, osx, virtualized
Status: published

Some collected links.  I have yet to get this working properly.  The
osx86 install images hang at "dsmos: Starting"

http://d4wiki.goddamm.it/index.php/Howto:\_Mac\_OSX\_on\_KVM

It seems as though KVM/qemu itself needs to be patched to emulate the
AppleSMC hardware device.  I can't yet find out of the current Ubuntu
7.x or 8.x distros of KVM include this patch or not.  It does seem like
this has already made it to opensuse, and the patch is nearly a year
old, so maybe it's in Ubuntu 8.x or 9.x:  Here's the patch itself:

http://svn.exactcode.de/t2/trunk/package/emulators/kvm/04-qemu-applesmc.patch

Unfortunately, the author's website (http://alex.csgraf.de/self/) seems
to be really borked and no longer has the relevant information other
than the "getsmc" script referenced from the wiki page.  (Not sure if
this getsmc script is for Apple h/w + OSX or Apple + Linux)

There is an "applesmc" kernel module for Ubuntu, but I suspect this is
for accessing the \*real\* SMC device, not for emulating one on
non-Apple hardware.
