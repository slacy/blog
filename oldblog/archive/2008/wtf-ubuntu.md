Title: WTF, Ubuntu?
Date: 2008-03-16 08:07
Author: slacy
Category: General
Tags: ubuntu
Status: published

Hey, so, Ubuntu, what gives?

I'm running a "sudo apt-get install fobar-package-version" and I get
messages like this one:

> Media change: please insert the disc labeled  
> 'Ubuntu-Server 7.10 \_Gutsy Gibbon\_ - Release amd64 (20071016)'  
> in the drive '/cdrom/' and press enter

What gives? If I put that disc in the drive (the install CD) then when
my machine reboots, it'll boot to that disk, which isn't what I want.
How about you please just get whatever you need from the internet? Oh,
and by the way, I have a copy of the .iso image on my harddrive if you
really really need something thats in there. How about I just point you
at that? Would that be ok? Thanks!

Update: Edit /etc/apt/sources.list and remove the entry for the cdrom,
or make it point at the ISO image file to solve this issue.
