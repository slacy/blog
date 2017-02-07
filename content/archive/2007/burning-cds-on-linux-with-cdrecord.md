Title: Burning CDs on linux with cdrecord
Date: 2007-03-04 16:26
Author: slacy
Category: Linux Stuff
Status: published

I don't know why, but I find the program "cdrecord" the most problematic
of almost all Linux commands. It never works right, always fails with
mysterious messages, and even in the "best case" prints out cryptic
things like "Warning: using inofficial libscg transport code version
(schily - Red Hat-scsi-linux-sg.c-1.83-RH '@(\#)scsi-linux-sg.c 1.83
04/05/20 Copyright 1997 J. Schilling').". Yuk!

Thankfully, I don't need to burn CDs or DVDs often (only when I upgrade
to a newer version of Linux) and since the Fedora Project just
discontinued support for Fedora Core 4, that time has come!

Here's a command that works for me on by sort of old Pioneer DVR-106D. I
could try "speed=16" (the rating of the drive) and see what happens.

> cdrecord -tao -v speed=2 dev=ATA:0,0,0
> /home/shared/linux/Zod-binary-x86\_64/FC-6-x86\_64-disc1.iso

Mostly, I'm writing this down for my own memory, so that I can search
around the next time I have to do this...

**NOTE:** Well, the command succeeded, but the disc that was burned was
bogus (it got i/o errors). I hate cdrecord. It sucks. I wonder if my
drive is busted? Sometimes it gets stuck in "performing OPC" and never
returns, hanging my IDE bus, and thus, hanging my entire computer, and
then when I have to restart, my RAID setup goes into rebuild mode, and
takes hours to recover. Yuk!
