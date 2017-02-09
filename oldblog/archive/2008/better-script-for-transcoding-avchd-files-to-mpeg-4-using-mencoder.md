Title: Better script for transcoding avchd files to mpeg-4 using mencoder.
Date: 2008-03-30 20:55
Author: slacy
Category: General
Status: published

So, you've got a shiny new Canon HG10 (or similar) that outputs avchd
files, and you've got a Linux box, and you want to do something with
those movies? Well, I've got a script for you. This will transcode an
.mts or .m2ts to an .avi, using an excellent 2-pass encoding. All you
need in the current top-of-trunk mencoder from subversion (see
[mplayerhq.hu](http://mplayerhq.hu)).

> \#!/bin/bash  
> \#  
> \# We make a temp directory for each encoder so that we can run more
> than one  
> \# in parallel (dual core, baby!). Set variables below to change
> config  
> \# options. Most notably, you'll need to give the path to your
> mencoder. To  
> \# transcode to AVCHD, you'll need the latest mencoder from subversion
> (see  
> \# http://mplayerhq.hu)  
> \#  
> ORIGDIR=\`pwd\`  
> FILE=\$@  
> MENCODER=\~slacy/Desktop/mencoder/mencoder  
> TMPDIR=/tmp/transcode.\$\$  
> LOG=\$FILE.mencoder.log  
> BITRATE=3000
>
> mkdir -p \$TMPDIR  
> cd \$TMPDIR
>
> \# If you want to encode using x264, you can use the two lines below.
> I got  
> \# these working, but my computer still isn't fast enough to play back
> the  
> \# generated files, so I gave up on x264 encoding. I keep the
> originals  
> \# around, so its not a huge deal.  
> \#  
> \# \$MENCODER \$ORIGDIR/\$FILE -o \$FILE.avi -oac copy -ovc x264
> -x264encopts
> bitrate=\$BITRATE:pass=1:subq=1:bframes=1:frameref=1:turbo=2 -fps 120
> -ofps 60 -vf yadif=3,scale=1280:720 &gt;&gt; \$LOG  
> \# \$MENCODER \$ORIGDIR/\$FILE -o \$FILE.avi -oac copy -ovc x264
> -x264encopts
> bitrate=\$BITRATE:pass=2:subq=6:partitions=all:8x8dct:me=umh:frameref=5:bframes=1:b\_pyramid:weight\_b
> -fps 120 -ofps 60 -vf yadif=3,scale=1280:720 &gt;&gt; \$LOG
>
> \# Here are the encode lines to generate the mpeg-4 encoding. Note
> the  
> \# 2-pass, which gives much higher quality.  
> \#  
> \$MENCODER \$ORIGDIR/\$FILE -o \$FILE.avi -oac copy -ovc lavc
> -lavcopts
> vcodec=mpeg4:vbitrate=\$BITRATE:vpass=1:mbd=2:trell:v4mv:last\_pred=2:dia=-1:vmax\_b\_frames=2:vb\_strategy=1:cmp=3:subcmp=3:precmp=0:vqcomp=0.6:turbo
> -fps 120 -ofps 60 -vf yadif=3,scale=1280:720 &gt;&gt; \$LOG  
> \$MENCODER \$ORIGDIR/\$FILE -o \$FILE.avi -oac copy -ovc lavc
> -lavcopts
> vcodec=mpeg4:vbitrate=\$BITRATE:vpass=2:mbd=2:trell:v4mv:last\_pred=2:dia=-1:vmax\_b\_frames=2:vb\_strategy=1:cmp=3:subcmp=3:precmp=0:vqcomp=0.6:turbo
> -fps 120 -ofps 60 -vf yadif=3,scale=1280:720 &gt;&gt; \$LOG
>
> \# Make sure there isn't anything in the way...  
> rm -f \$ORIGDIR/\$FILE.avi  
> rm -f \$ORIGDIR/\$LOG
>
> \# And now move the newly generated files back where the original came
> from.  
> mv \$FILE.avi \$ORIGDIR  
> mv \$LOG \$ORIGDIR
>
> \# And remove our tmpdir to clean up.  
> rm -fr \$TMPDIR
