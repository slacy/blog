Title: The last Fedora update I'll ever do.
Date: 2008-02-19 15:04
Author: slacy
Category: General
Tags: atrpms, dag, Fedora 8, freshrpms, linux, livna, upgrade
Status: published

Yesterday, I finally finished updating this computer from Fedora Core 6
to Fedora Core 8. I've completely swarn off Fedora, and if there were an
easy way for me to migrate away, I'd do that instead of these insane
upgrades.

Here were the major stumbling blocks:  
1. The "depsolve hang in upgrade" bug which meant I needed to wait for a
respin or follow instructions listed in redhat's bug database. (I
decided to wait for the respin)  
2. The "respins" from fedoraunity.org took a while to be created, and
use the totally insane 'jigdo' downloader. They took about 2.5 days to
download 4GB. By contrast, a bittorrent download af the same data takes
about 4 hours.  
3. The installer ran mostly smoothly, but took several hours to upgrade
my system.  
4. The installer didn't upgrade over 1100 packages on my system. I had
to boot it up and run "yum update" to finish updating these.  
5. Even after 'yum update' I had a bunch of issues getting my monitor
resolution back to 1280x1024 (it wanted to be 800x600)  
6. Fedora doesn't inculde mp3 playback, mencoder, or mplayer, so you
need to enable 'extra' yum repositories to get these files. There are
several choices, and they usually just fuck up your system beyond
repair. (atrpms, freshrpms, dag, livna, etc.)

All in all, it took about 3 months to progress from step 1 to step 6.

At least my system still works. Mail works, the web works, gallery
works, music works. Phew.

Next time, I'm going to build a new computer, and I think I'll just
install gentoo. I'm not sure yet, though.
