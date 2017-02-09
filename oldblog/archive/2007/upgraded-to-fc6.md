Title: Upgraded to FC6
Date: 2007-03-08 18:25
Author: slacy
Category: General
Status: published

So, due to the wacky daylight savings policy, I needed to upgrade my
computer (or manually tweak tzdata, which I'm not too happy about). When
I ran the Fedora Core 6 installer (anaconda), I got the following
dialog:

> Multiple devices on your system are labeled k?;\[\]qu??lqBs,?|. Labels
> across devices must be unique for your system to function properly.
> Please fix this problem and restart the installation process.

My only option was "Reboot". So, I used e2label to make sure all my
filesystems were labeled, and got the same dialog. After banging my head
against a wall for about 3 days, I broke down and read the source code
for anaconda and pyparted to see what would cause this bug, and realized
that pyparted was trying to read labels from swap partitions too. So, I
did this:

> swapoff -a  
>   
> mkswap /dev/swap1 -L swap1  
>   
> mkswap /dev/swap2 -L swap2  
>   
> mkswap /dev/swap3 -L swap3  
>   
> swapon -a  

And then reran the installer, and guess what? It worked! Clearly, this
is a bug in pyparted (returning labels from unlabelled swap partitions)
and anaconda (not labeling swap partitions when it creates them) itself.
Once I knew this, I searched on bugzilla.redhat.com, and found that
there was already a bug opened that says exactly what I did.

[RedHat bug
160622](https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=160622)  
  
[My post to fedora-list that was summarily ignored, but I responded to
myself with the solution so that it would be preserved in the archives
for other users to
see](https://www.redhat.com/archives/fedora-list/2007-March/msg00609.html)

Everything else went fairly smoothly. There only seems to be one broken
thing on my system now, and thats Netjuke. Ahh, the glories of
unmaintained open source software that has no feasible replacement at
this time.
