Title: Multithreadded GDB trick
Date: 2007-10-04 13:36
Author: slacy
Category: General
Status: published

I learned this once, then forgot it because I didn't blog about it, and
now I just learned it again, so I'm writing it down this time:

To show stacks of all running threads in gdb, just type:

> (gdb) thread apply all info stack

I can't cut and paste any example output because someone would probably
get kinda pissed if I did that.
