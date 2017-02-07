Title: Playing avchd files from mplayer
Date: 2008-03-30 20:42
Author: slacy
Category: General
Status: published

The current top of trunk mplayer can play avchd files produced by a
camera like the Canon HG10 (which we now own! Woot!)

The trick is that you have to pass "-fps 60" to it, otherwise it just
bombs out with a non-sensical error message. Oh, and you have to get
mplayer from subversion to make this work. Oh, and you have to have a
screamingly fast computer.

Anyway, more detailed instructions on using mencoder to transcode avchd
files soon (Yes, I know I posted about this before, but this time I've
got a refined script that I think is worth mentioning).
