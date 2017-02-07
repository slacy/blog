Title: Running amazonmp3 downloader on Ubuntu 9.04 amd64 (Jaunty) via a chroot
Date: 2009-08-13 13:22
Author: slacy
Category: General
Tags: amazon mp3, amazonmp3, chroot, intrepid, jaunty, mp3, Music, schroot, ubuntu
Status: published

The one biggest (and most annoying) missing package for Ubuntu 9.04
amd64 is the amazon mp3 downloader package.  This is **critical** being
able to download special cheap albums from amazon, and is only available
as a 32-bit package for Ubuntu 8.04 (Intrepid).

There are several descriptions on the net on how to hack around missing
library dependencies and download them (via getlibs) or to tweak out the
pkgconfig file to shoe horn the amazonmp3.deb file into an amd64 system.

I like to keep my installs really pristine, and avoid workarounds like
getlibs and modified packages, so I've decided to go with a 32-bit
chroot for running amazonmp3.  Generally, the process involves
downloading another version of Ubuntu (in our case, 8.04, which is what
the amazonmp3 package was built against), and then chroot-ing into this
install area to run the 32-bit program.  Several existing tools make
this easier than it sounds.

Get Ready
---------

There are several dependent packages that you should install first.  In
your base system, please run:

> \$ sudo apt-get install debootstrap schroot

Install 32-bit Intrepid into a subdirectory
-------------------------------------------

Using the new debootstrap package that you just installed, you can now
run:

> \$ mkdir \~/chroots
>
> \$ sudo debootstrap --arch=i386 intrepid \~/chroots/intrepid-32

The second command will take a while to run, and will download several
hundred MB of intrepid packages, and install them under the newly
created directory \~/chroots/intrepid-32

Edit /etc/schroot/schroot.conf
------------------------------

You should add a section to /etc/schroot/schroot.conf that looks like
this:

> \[intrepid-32\]  
> type=directory  
> description=Intrepid 32-bit  
> location=/home/YOUR\_USERNAME/chroots/intrepid-32  
> priority=3  
> users=YOUR\_USERNAME,root  
> groups=YOUR\_USERNAME,root  
> root-groups=root,adm  
> run-setup-scripts=true  
> run-exec-scripts=true  
> personality=linux32

Do a little bit of post-install cleanup.
----------------------------------------

I've found that by default, I don't have sudo permissions inside the
chroot, so I do this one small step:

> \$ sudo cp /etc/sudoers \~/chroots/intrepid-32/etc/sudoers

That way, when I enter the chroot, I have sudo permissions available as
well.

Get inside the chroot and make sure it works
--------------------------------------------

You can now go inside the chroot via the following command:

> \$ schroot -c intrepid-32

You should see that while inside the chroot, your prompt should start
with "(intrepid-32)" indicating that you're chrooted.  Great.  Give a
simple sudo command a try to make sure it works, like this:

> \$ sudo ls \~

Type your password, and confirm that you can run things as root.

At this point, you can do anything else you want in the chroot, like
installing other packages, or cleaning things up.  You may want to run
"sudo apt-get update ; sudo apt-get dist-upgrade" just for fun.

Install amazonmp3.deb in the chroot
-----------------------------------

The chroot shares your home directory, /tmp, and several other
directories with your main system (so be careful!).  But, this also
makes life easier.  While you're outside of the chroot, download
amazonmp3.deb and put it in /tmp or your home directory. Then, get
inside the chroot, and run:

> (intrepid-32)\$ sudo dpkg -i amazonmp3.deb

It will complain about some missing dependencies.  Install those
libraries via apt-get, and then run the dpkg -i again, and you should be
in business.  To run amazonmp3, you may need to double-check your
DISPLAY environment variable and make sure that it's properly set inside
the chroot.  Once you've done that, you should be able to easily run
amazonmp3 inside the chroot, and download music to your home directory.

Good luck!
