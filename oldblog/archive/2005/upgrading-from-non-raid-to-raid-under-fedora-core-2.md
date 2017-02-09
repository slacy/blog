Title: Upgrading from non-RAID to RAID under Fedora Core 2
Date: 2005-04-22 07:00
Author: slacy
Category: General
Status: published

This is a quick how-to about what I had to go through to upgrade my
Fedora Core 2 system from a dual-drive non-RAID configuration into a
dual-drive RAID1 mirrored system. The problem was this:

I had two 60G drives in my system, mounted on "/" and "/music". The one
on /music was serving as my backup drive as well, with a nightly rsync
over from important areas. It was at 99% capaciy, so an upgrade was
eminent. I decided that the right strategy, instead of a nightly rsync,
was to use software RAID1. Read on for the steps it took to get the new
system up and running, and for the important points I learned about
going from non-RAID to RAID.  
  

Goals
-----

What I wanted to do was end up with a single "/" filesystem  
composed of a RAID1 (mirror) of 2x250G drives. My current system was
two  
separate 60G drives.

First, the backup.
------------------

Like all good system maintenence instructions, this is where I tell you  
that you should really back things up before you start. But, as you all  
know, backing up an entire system (120G at this point) isn't realistic.  
Just back up the stuff that matters.

Some important accessories
--------------------------

Having a USB drive enclosure is a fairly nice accessory. In my case, I  
was going to use it to copy over everything other than my "/"  
drive, and its convenient because you don't have to open up your case
and  
power down your system just to copy some files from another drive.

Some important pieces of software
---------------------------------

In FC2, hopefully you're using "yum" to update your system  
packages. Use "yum" to get the package "mdadm" which  
contains mdadm and a couple other tools. This is the new preferred way
to  
configure RAID systems. The "old" way is raidtools &  
raid.conf. mdadm does not use raid.conf, and does not require a  
configuration file. Everything that it needs to know is stored in the  
superblock of the RAID partition itself.

Get down to a single drive system.
----------------------------------

If possible, remove all drives from your system, including the CD-ROM,  
except for your "/" drive. Additionally, put it in a spot that is  
NOT the same as where your RAID drives are going to go. For example,
you  
probably want your RAID drives to be the **master** drives on your two  
IDE controllers. Thus, your RAID drives will be /dev/hda and /dev/hdc.
Put  
your "/" on /dev/hdb or /dev/hdd. Make sure that your bios can  
boot from this alternate location, and boot from it just to try things
out.  
At this point, your system is ready to accept the new raid drives. Shut  
down, install the new drives, and reboot your system.

At this point, you should have a working system with 3 drives, and the 2
RAID drives in their final destination locations. Good for you.

Partition the drives identically
--------------------------------

Now that you have a working system with the drives installed, you
should  
boot up and partition the drives using fdisk. I decided to partition
them  
as such:

    Disk /dev/hda: 251.0 GB, 251000193024 bytes
    255 heads, 63 sectors/track, 30515 cylinders
    Units = cylinders of 16065 * 512 = 8225280 bytes
     
       Device Boot      Start         End      Blocks   Id  System
    /dev/hda1               1         250     2008093+  83  Linux
    /dev/hda2             251         500     2008125   82  Linux swap
    /dev/hda3             501       30515   241095487+  fd  Linux raid autodetect

Note very carefully how I have set up the "Id" column. Use the  
fdisk command "t : Change a partition's system Id" to set this  
value. The RAID partitions MUST have the type "0xfd" as shown  
above. I have partitioned each drive identically, and I plan on hda1
being  
"/boot" and hdc1 being a backup of /boot. hda2 and hdc2 are both  
swap, and hda3 and hdc3 make up the RAID array.

Set up your other non-RAID partitions
-------------------------------------

At this point, its prudent to do all the "other stuff" thats  
necessary to get a working system. This is all non-RAID specific, but
are  
necssary.

### Format your swap and /boot partition, and copy files over

This is fairly straightforward. Choose the partition you want to be
your  
/boot partition (can not be RAID) and run mkfs on it. For example:

    # mkfs /dev/hda1
    # mkswap /dev/hda2

Make a mount point (something like /mnt/boot2) and mount the new /boot,  
and copy all the files from the old /boot onto the new /boot.

**A Note About Copying Files:** For this setup, I used a "tar-copy"
which  
is something I learned to use ages ago when I was told that "cp was
very  
slow for this sort of operation" A tar-copy is essentially a command
that  
looks like this:

    # cd /source/location
    # tar cvf - . | (cd /destination/directory ; tar xf - )

But, it doesn't copy pipes or other special files. My advice to you is  
to take a good look at the "cp" man page, and do a recursive copy of all
the  
files instead of using the tar copy. At the very least, make sure you  
specify the "-a" option, which turns on a few very important flags

**Another Note:** You'll need to do a fair bit more to your /boot  
partition before you can boot from the RAID. See below

### Install grub in your boot MBR

This is straightforward. Just run:

    # grub-install --root-directory=/mnt/boot2 /dev/hda

Thats it for that one.

Use mdadm to create the RAID array
----------------------------------

Boot up your system, and use mdadm to create the raid array. The
command  
line will look something like this:

    mdadm -C --level=raid1 /dev/md0 -n 2 -x 0 /dev/hda3 /dev/hdc3

This should correctly initalize the raid array. Once you have created  
the drive, you can "Assemble" it, which essentially means to  
"start running" the RAID array. Note that we have not added a  
filesystem to this drive yet. To assemble the array, type:

    mdadm -A /dev/md0

Now, the array has been created, and is assembled. At this point, you  
can check that its running, like this:

    # mdadm -D /dev/md0
    /dev/md0:
            Version : 00.90.01
      Creation Time : Wed Sep  1 19:26:36 2004
         Raid Level : raid1
         Array Size : 241095360 (229.93 GiB 246.88 GB)
        Device Size : 241095360 (229.93 GiB 246.88 GB)
       Raid Devices : 2
      Total Devices : 2
    Preferred Minor : 0
        Persistence : Superblock is persistent
     
        Update Time : Fri Sep  3 11:02:01 2004
              State : clean, no-errors
     Active Devices : 2
    Working Devices : 2
     Failed Devices : 0
      Spare Devices : 0
     
     
        Number   Major   Minor   RaidDevice State
           0       3        3        0      active sync   /dev/hda3
           1      22        3        1      active sync   /dev/hdc3
               UUID : a450119b:32910153:21807701:cf41ceea
             Events : 0.148714

Note that since I'm writing this on my running system, mine is  
"clean, no-errors" and does not have a line that says  
"reconstructing" Since a new array needs to be  
"reconstructed" when its initally built, your new array should say  
reconstructing, and have a percent complete. I highly suggest that you
just  
wait for the reconstruction process to finish. It will eliminate one  
variable from the bootup equation thats coming later. Just let it sit
for a  
couple hours, and it'll be fine.

Create the filesystem on /dev/md0, and mount it.
------------------------------------------------

Now, you need to create the root filesystem. This is easy, just type:

    # mkfs.ext3 /dev/md0

And let it finish. No problem here. Then, you should create a mount  
point, and mount up the new filesystem:

    # mkdir /mnt/md

    # mount /dev/md0 /mnt/md

If that worked, you now have a RAID partition where you can copy all
your  
files.

Boot to a single-user system
----------------------------

You NEVER want to copy your root filesystem while the system is in
multi-user mode! The files will be in the process of being modified, and
all hell could break loose, and you'll never be certain that your new
copy is actually valid. So, get this puppy into single user mode:

    # init 1

Copy all your files from the existing "/" onto your new RAID array
------------------------------------------------------------------

See my note above about using a tar-copy versus a recursive cp command.
I think the thing you want here is a recursive copy with the "-a" and
"-x" flags. It is very important that you use the "-x" flag so that you
don't make a recursive copy of your copy (since your destination,
/mnt/md is included in everything under "/")

Run mkinitrd
------------

mkinitrd is the thing that creates the inital RAM disk that the kernel
uses during bringup. You have to do this so that the new initrd includes
the necessary RAID drivers. If you don't do this, then it won't work at
all. Ever. You wil be in great pain

This is the step that I had no idea I needed to do. The key things to  
note are that mkinitrd is too smart for its own good, and won't create
an initrd that contains RAID unless a raid device is currently mounted.
So, since your RAID device is already running and mounted, you're good
to go.

**Make sure to back up your old initrd before you start!**

My /boot partition looked like this:

    # ls /boot
    boot                initrd-2.6.8-1.521.img      os2_d.b
    boot.b              initrd-2.6.8-1.521.img.bak  System.map
    chain.b             kernel.h                    System.map-2.6.8-1.521
    config-2.6.8-1.521  lost+found                  vmlinuz
    grub                module-info                 vmlinuz-2.6.8-1.521

So, the name of the initrd thats working is **initrd-2.6.8-1.521.img**

    # mv initrd-2.6.8-1.521.img initrd-2.6.8-1.521.img.bak
    # mkinitrd /mnt/boot2/initrd-2.6.8-1.521.img 2.6.8-1.521

That should create the new file. Since you have kept the name the same,
then you won't have to modify your grub setup. Easy squeezie

Try it out
----------

Cross all ten fingers and toes, and reboot your system. Make sure to  
modify your BIOS to boot from the first drive (/dev/hda) and if you're  
daring, you can remove your old "/" drive. It should all work

If you have other files on other drives, then when your system comes up,
you can use a USB enclosure to mount those files, and copy them over.
That should give you a complete copy of your old data! Hooray!
