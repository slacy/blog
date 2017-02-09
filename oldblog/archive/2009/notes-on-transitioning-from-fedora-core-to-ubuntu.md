Title: Notes on transitioning from Fedora Core to Ubuntu 
Date: 2009-08-11 20:00
Author: slacy
Category: General
Tags: amazonmp3, flash, fonts, linux, ubuntu, unetbootin
Status: published

Just some quick notes before I forget them.

I've recently switched my primary desktop machine from Fedora Core 8
(very old, I know) x86\_64 to Ubuntu 9.04 (latest and greatest)
x86\_64.  In general, things went well, but there were a couple gotchas
that I had to work through, so I thought I'd list them here:

-   The default Ubuntu 9.04 desktop installer won't let you set up RAID
    by default.  So, you have to boot and run the "alternate" installer.
-   If you use [unetbootin](http://unetbootin.sourceforge.net) to "burn"
    the Ubuntu alternate install disk to a USB stick and boot from that,
    then it will have errors during the install asking you to "insert
    your CD-ROM".  Ugh.  The solution here is to select "Install" from
    the unetbootin boot menu instead of "default".  This will run a
    network-based install instead of trying to install from the USB
    image that you just burned.  I know it's silly, but at least
    it worked.
-   Ubuntu, unlike Fedora, only allows x86\_64 for it's libraries in
    /lib, unlike Fedora which puts 32-bit libraries in /lib and 64-bit
    ones in /lib64.  Ubuntu has an option (ia32-apt-get
    and ia32-libs-tools) to put some 32-bit libraries in /lib32, but I
    found that **this led to some serious apt-get dependency issues**,
    and I quickly gave up and uninstalled these packages (and removed
    the damage they caused).
-   There are a couple of critical things that are 32-bit only:
    -   The amazon mp3 downloader application.  There are some tutorials
        around about how to use a program called
        "[getlibs](http://www.ensode.net/roller/dheffelfinger/entry/installing_amazon_mp3_downloader_under)"
        to make it work right, and there are some
        [pkgbuild](http://bbs.archlinux.org/viewtopic.php?id=60607) and
        [wacky .deb creation
        scripts](http://bbs.archlinux.org/viewtopic.php?id=44870) to
        make this seem to work.  It's my understanding that both methods
        pollute /lib with 32-bit libraries, so I haven't tried it yet. 
        I have an e-mail out to the amazonmp3 downloader maintainer, and
        we'll see if that pans out.
    -   Adobe Flash.  Thankfully, Ubuntu seems to have worked this one
        out, and if you "sudo apt-get install flashplugin-installer" it
        just works, although it uses ndispluginwrapper, which is sort of
        a giant hack, but at least it works until Adobe gives full
        support for 64-bit flash on Ubuntu.
-   Although the Ubuntu 9.04 fonts looked pretty good out of the box, I
    found that my installing some alternate font packages, that I could
    really improve the look of many web pages.  The packages that I
    installed were: msttcorefonts, ttf-bitstream-vera, ttf-dejavu-core,
    ttf-droid, ttf-liberation, ttf-xfree86-nonfree.  I think that's a
    fairly good list, and was surprised that they weren't installed
    by default.

So, that about sums it up so far.  I'm running ext4, on an md RAID5
array, and things seem to be reasonably stable thus far.

Please note that I **did not** install Ubuntu on top of Fedora.  I'm not
sure what would happen if one were to do this.  I did a clean install on
fresh disks, and then copied my data back from a backup.
