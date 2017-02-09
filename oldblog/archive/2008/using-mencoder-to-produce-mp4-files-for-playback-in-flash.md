Title: Using mencoder to produce .mp4 files for playback in flash
Date: 2008-09-08 19:11
Author: slacy
Category: General
Status: published

> Although Flash 9.0+ says it supports .mp4 file playback, I've found
> that its actually quite picky about what it will actually play.  So,
> if you want to produce a file using mencoder that plays in flash, you
> need to:
>
> Download and compile the MP4Box executable from the [GPAC
> distribution](http://gpac.sourceforge.net/doc_mp4box.php)  
> Run an mencoder command to produce an AVI file that has h264 video &
> AAC audio:
>
> mencoder \$FILE -o \$OUTPUT -oac faac -srate 44100 -ovc x264
> -x264encopts bitrate=\$BITRATE:turbo:pass=1 -fps 60000/1001 -ofps
> 30000/1001 -vf field=0,scale=\$RES 2&gt;&1 &gt;&gt; \$LOG  
> mencoder \$FILE -o \$OUTPUT -oac faac -srate 44100 -ovc x264
> -x264encopts bitrate=\$BITRATE:pass=2 -fps 60000/1001 -ofps 30000/1001
> -vf field=0,scale=\$RES 2&gt;&1 &gt;&gt; \$LOG

Then, you need to pull out the h264 video & AAC audio from the AVI file,
and put them back in a mp4 container using MP4Box, like this:

> MP4Box -aviraw video \$VIDEO\_OUTPUT
>
> MP4Box -aviraw audio \$AUDIO\_OUTPUT
>
> mv \$AUDIO\_OUTPUT \${AUDIO\_OUTPUT/.raw/.aac} \# Make the .raw file
> an .aac file
>
> MP4Box -add \$VIDEO\_OUTPUT -add \$AUDIO\_OUTPUT \$FINAL\_OUTPUT.mp4
