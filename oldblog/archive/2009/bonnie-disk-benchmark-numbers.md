Title: bonnie++ disk benchmark numbers
Date: 2009-09-21 12:35
Author: slacy
Category: General
Tags: array, bonnie++, hdd, raid5, sata
Status: published

I just built a new RAID 5 drive array out of 3 Seagate ST31000528AS 1TB
drives, giving me 2TB of usable space.  I was curious about the
performance, so I ran bonnie++ on the array, and got:

    $ bonnie++ -f -d /tmp -s 8G -n 1024
    [wait a very long time]
    Version 1.03c       ------Sequential Output------ --Sequential Input- --Random-
                        -Per Chr- --Block-- -Rewrite- -Per Chr- --Block-- --Seeks--
    Machine        Size K/sec %CP K/sec %CP K/sec %CP K/sec %CP K/sec %CP  /sec %CP
    whisper          8G           132035  24 56505  15           168485  25 325.7   1
                        ------Sequential Create------ --------Random Create--------
                        -Create-- --Read--- -Delete-- -Create-- --Read--- -Delete--
                  files  /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP
                   1024 20728  59 385904  85   352   0 11134  32 502866  97   222   0
    whisper,8G,,,132035,24,56505,15,,,168485,25,325.7,1,1024,20728,59,385904,85,352,0,11134,32,502866,97,222,0

I had a hard time finding many compiled bonnie++ result pages comparing
different systems, so let me know if you know of one, or if I should
submit this data there.

In short, it's pretty darned fast, but I don't even have SATA-2 to make
it scream.
