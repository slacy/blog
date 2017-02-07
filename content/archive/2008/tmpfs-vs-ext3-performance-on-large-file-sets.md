Title: tmpfs vs. ext3 performance on large file sets
Date: 2008-08-06 15:35
Author: slacy
Category: General
Status: published

I've been experimenting with tmpfs at work, and decided to run a simple
performance benchmark comparing a native ext3 filesystem with a tmpfs
filesystem.

I'm using bonnie++ to run the tests, and each is creating 20,000 files
of random size between 0 and 250,000 bytes, stored in 1000 directories.
The first test has a working set size of about 2.5GB. Here are the
results from my workstation which has 4GB RAM:

ext3:

    # bonnie++ -f -s 0 -n 50:250000:0:1000 -d /tmp
    Version 1.03d       ------Sequential Create------ --------Random Create--------
                        -Create-- --Read--- -Delete-- -Create-- --Read--- -Delete--
    files:max            /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP
       20:250000:0/1000   348  11   325   3  1368   8   745  22  1697  11   395   3

And here's tmpfs:

    # bonnie++ -f -s 0 -n 50:250000:0:1000 -d /tmpfs
    Version 1.03d       ------Sequential Create------ --------Random Create--------
                        -Create-- --Read--- -Delete-- -Create-- --Read--- -Delete--
    files:max            /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP
       20:250000:0/1000  2384  59 16163  97 +++++ +++  8757  99 18576  97 40316  98

Which shows that reading from tmpfs is somewhere between 10x and 50x
faster than local ext3 for a small file set, even if this file set fits
in RAM (and thus, in buffer cache as well as in tmpfs). The "+++"'s in
the tmpfs results are there because it was so fast that they couldn't
time it. In other words, its wicked fast.

When you increase the working set size beyond that of the physical RAM
of the workstation, tmpfs starts to show its weakness. Here's the output
from a run that had a 6.25GB footprint:

    # bonnie++ -f -s 0  -n 50:250000:0:1000 -d /tmpfs
    Version 1.03d       ------Sequential Create------ --------Random Create--------
                        -Create-- --Read--- -Delete-- -Create-- --Read--- -Delete--
    files:max            /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP
       50:250000:0/1000   409   6    78   2 72403  98   416  11    49   2 62921  97

Note how the read performance has gone *way* down. We'll have to compare
that to the same test run on an ext3 filesystem:

    Version 1.03d       ------Sequential Create------ --------Random Create--------
                        -Create-- --Read--- -Delete-- -Create-- --Read--- -Delete--
    files:max            /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP
       50:250000:0/1000   231   7   245   3   745   3   252   7    70   1   242   1

Which shows that reading sequentially created files via the native
filesystem (vs. swapped out and in tmpfs) is about 3x faster. In this
case, ext3 has won by a good margin. ext3 doesn't have such a wide
margin for randomly read & created files, and is only about 1.4x faster
than tmpfs.

So, should I put the majority of my temporary files in tmpfs, or not?
