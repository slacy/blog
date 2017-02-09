Title: Firefox 3.5 crashes under Fedora solved
Date: 2009-07-29 12:45
Author: slacy
Category: General
Tags: 32-bit, adobe, fedora core, firefox, flash
Status: published

I was having horrible crashing issues with the 32-bit version of Firefox
3.5.1 on my Fedora Core x86\_64 system, especially while using Flash,
but also while doing simple tasks like printing.  Fedora Core (unlike
Ubuntu) can run both 32-bit and 64-bit binaries on the same setup, due
to /lib being 32-bit, and /lib64 being 64-bit.

I finally realized that maybe the issue was some bizarre and missing
32-bit library that the .tar.gz distribution of Firefox was relying on,
and not giving me a reasonable error message about a missing dependency.

So, I did a:

> sudo yum install firefox.i386

which indeed pulled in a bunch of dependencies that I think had been
cleaned up by some other process that looked for orphaned dependencies.

Although I'm not using the Fedora-provided version of Firefox 2.0, my
personal install of 32-bit Firefox 3.5.1 (with Adobe flash, 32-bit) is
now back to its prior "reasonably stable" point.

I'm still planning on doing a fresh install of Ubuntu 9.04 when my new
hard drives come in.
