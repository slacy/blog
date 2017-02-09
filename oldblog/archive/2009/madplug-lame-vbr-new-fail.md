Title: audacious + madplug + lame --vbr-new == FAIL
Date: 2009-03-17 13:09
Author: slacy
Category: General
Tags: audacious, fedora, lame, linux, mp3
Status: published

I listen to all of my music via streaming it from my home machine, and
transcoding it on the fly. I recently made 2 changes to my setup:

1.  I'm using audacious for playback instead of xmms
2.  I switched to a more recent version of lame.

After doing so, about 1 in 10 files would fail to play (either silence,
or strange thumping noises) on audacious, saying one or more of the
following messages:

> (audacious:12805): MADPlug-WARNING \*\*: samplerate varies!!  
> (audacious:12805): MADPlug-WARNING \*\*: layer varies!!  
> (audacious:8645): MADPlug-WARNING \*\*: number of channels varies!!

If I downloaded the file and played that, it worked just fine, so it was
something weird about the fact that it was streaming.  My lame
transcoding commandline was:

> lame --mp3input -h --vbr-new -V 6 -B 320 -b 32 -S -m j \$file -

The problem seems to be --vbr-new, since if I remove that option, it
works great all the time.  Go figure.

In general, I think audacious sucks.  Now I also think that madplug
sucks.  Oh, and by the way, all of this was precipitated by Fedora
removing xmms from their repositories due to mp3 licensing issues. 
Fedora sucks too.  Ugh!  It seems as though mp3 playback under Linux has
taken a huge step backwards...
