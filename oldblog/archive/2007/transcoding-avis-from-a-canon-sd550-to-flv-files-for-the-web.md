Title: Transcoding AVIs from a Canon SD550 to FLV files for the web.
Date: 2007-11-26 20:22
Author: slacy
Category: General
Tags: canon sd550, ffmpeg, mplayer, sd550, transcoding
Status: published

So, I've been wondering what to do with the AVI files that we've been
taking using our Canon SD550 camera. The movies are great, but they're
HUGE. The camera only uses mjpeg compression, so there's a lot of room
for improvement in the compression. So, I looked at transcoding them to
FLV files, since Gallery2 has a built-in FLV player, so the files could
be played right in Gallery.

I came up with the following script that does a simple 2-pass encoding
to produce a reasonable output file at 1.25Mbps. I choose to go with a
higher bitrate and higher quality, but this could be turned down to
around 700kbps and still be reasonable. Here's the script:

> \#!/bin/bash  
> input=\$1  
> output=./flv/\${input/.avi/.flv}  
> logdir=\`dirname \$output\`  
> mkdir -p \$logdir  
> logfile=\$output.log  
> ffmpeg -y -i \$input -ar 11025 -ab 64k -aic -umv -b 1250k -r 30 -pass
> 1 \$output -passlogfile \$logfile  
> ffmpeg -y -i \$input -ar 11025 -ab 64k -aic -umv -b 1250k -r 30 -pass
> 2 \$output -passlogfile \$logfile  
> rm \$logfile\*

And I run it like this:

> \# find . -iname "\*.avi" | xargs -n1 -P2 \~/bin/flv\_transcode.sh

It will create a toplevel "flv" directory, and put all the transcoded
output in that subdirectory. Mencoder can't directly produce FLV output,
so this ffmpeg-based solution is a bit easier. Now, we just have to wait
for Macromedia to support h264 files...
