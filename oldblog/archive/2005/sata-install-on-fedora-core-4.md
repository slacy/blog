Title: SATA install on Fedora Core 4
Date: 2005-11-19 19:29
Author: slacy
Category: General
Status: published

When Setting up my new system, which is running on an ASUS A8N-SLI
Premium motherboard, I had some issues:

First off: I did not try to use any of the "hardware" RAID that comes
with the motherboard. It has 2 RAID controllers, and I disabled both in
the BIOS before starting. Linux software raid seems to work just great,
and use up very little CPU. That said...

After installing Fedora Core 4 from CDs (network and usb disk installs
failed) the box didn't boot up. It just went through the boot messages
and sat there.

I finally figured out that the problem was the drive boot order: What
linux thinks of as "/dev/sda" (first SATA drive) isn't actually "drive
0" to the bios. So, the hard drive boot sequence needed to be change to
set the boot order so that "drive 2" (the 3rd drive) was the first drive
in the boot.

Then, I was able to get to the GRUB boot prompt, and boot up the box.
There was some issue with GRUB thinking that the system should be on
(hd2,0). I think this may have been caused by my previous attempts to
fix the problem, but anyway, for inital boots, I needed to manually
change the GRUB boot parameters so that it was hd0,0. Then it worked.

This is way more than I ever wanted to know about the internal workings
of linux.
