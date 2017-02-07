Title: Transcoding AVCHD (.mts or .m2ts) files using mencoder on Linux
Date: 2008-02-12 19:56
Author: slacy
Category: General
Tags: canon hg10, m2ts, mencoder, mts
Status: published

The current top-of-trunk version of mplayer will decode and playback
.mts and .m2ts AVCHD files. The one caveat is that your computer has to
be fast enough to decode them, which mine isn't.

Therefore, transcoding the .mts files to a more easily playable format
is preferred. Since mplayer can decode the orignials, then mencoder can
transcode them directly. I'm still experimenting, but the following
command produces a pretty nice output, and is significantly smaller than
the original .mts file.

> \# mencoder \$file -o ./\$file.avi -oac copy -ovc lavc -lavcopts
> vcodec=mpeg4:vbitrate=5000 -fps 60 -vf scale=1280:720

This will run at about 35FPS on my Athlon 4400+. I'm not specifying any
fancy filters, like deinterlacing or denoising, and both of those could
probably increase the quality of the output. Doing a 2-pass encode would
also increase the quality of the output. Those commands would look like
this:

> \# mencoder \$file -o \$file.avi -oac copy -ovc lavc -lavcopts
> vcodec=mpeg4:vbitrate=5000:vpass=1:turbo -fps 60 -vf scale=1280:720  
> \# mencoder \$file -o \$file.avi -oac copy -ovc lavc -lavcopts
> vcodec=mpeg4:vbitrate=5000:vpass=2 -fps 60 -vf scale=1280:720

You'd probably only really need to do a 2-pass encode if you set the
bitrate much lower than the 5Mbps that I've specified.

Now, I might actually think about buying that [Canon
HG10](http://www.amazon.com/Canon-AVCHD-Definition-Camcorder-Optical/dp/B000U8HBRW/ref=pd_bbs_sr_1?ie=UTF8&s=electronics&qid=1202874937&sr=8-1)
instead of just borrowing it...
