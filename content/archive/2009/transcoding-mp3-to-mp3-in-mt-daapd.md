Title: transcoding mp3-to-mp3 in mt-daapd
Date: 2009-08-24 12:44
Author: slacy
Category: General
Tags: itunes, lame, linux, mp3, mt-daapd, Music, transcoding, unix, vbr
Status: published

Introduction
------------

mt-daapd is an iTunes daap-protocol server for Unix systems.  I'm using
mt-daapd on by Ubuntu 9.04 system to stream music over the internet to
my workplace.   The issue is that many of my mp3 files are 256kbps mp3
files, and streaming these takes up more bandwidth than necessary.

mt-daapd includes a transcoding system called "ssc" for "Server Side
Conversion".  This system works by either a shared-object plugin (i.e.
ssc\_ffmpeg) or via an external script file (i.e. ssc\_script).

using the ssc\_script functionality, one can invoke 'lame' (the mp3
encoder) to transcode high bitrate mp3 files into lower bitrate mp3
files.  The setup for this in mt-daapd wasn't very obvious, so I'll
document it here.

Install mt-daapd
----------------

The version of mt-daapd provided by Ubuntu 9.04 includes support for
transcoding, so you can just run:  
` $ sudo apt-get install mt-daapd`

Turn on ssc
-----------

Edit your /etc/mt-daapd.conf file, and make sure you have the following
lines in the correct places:

> ssc\_codectypes = mpeg
>
> always\_transcode = mpeg
>
> ssc\_prog = /path/to/script/shown/below/mt-daapd-mp3-ssc.sh
>
> \[plugins\]
>
> plugins = ssc-script.so

Create mt-daapd-mp3-ssc.sh
--------------------------

You'll need to create a shell script to do the transcoding via
ssc\_scrpit / ssc\_prog.  Here's the script I'm using:

> \#!/bin/bash
>
> FILE=\$1  
> OFFSET=0
>
> if \[ "\$2" == "" \]; then  
> OFFSET=0  
> else  
> OFFSET=\$2  
> fi
>
> if \[ "\$3" == "" \]; then  
> FORGELEN=\$3  
> fi
>
> lame -V6 --quiet "\$FILE" -

Note that I'm looking at the 2nd and 3rd args, but I'm not doing
anything with them.  These arguments are used to make sure that seeking
works properly in your daap client.  I don't care about seeking, and
doing it properly is somewhat hard, so I've just ignored those
arguments.  I think that this could be accomplished properly using the
program 'mp3splt' but I haven't looked into it enough to see what it
would take.

Make sure the script above is put somewhere accessible by the user
specified as 'runas' in your mt-daapd.conf.   Make sure the script is
executable by this user as well.

Restart mt-daapd and see if it works
------------------------------------

Restart mt-daapd via:

> \$ sudo /etc/init.d/mt-daapd restart

Then reconnect your daap client (I use rhythmbox).  You can see if the
script is working by running "ps auwxww | grep lame" just after pressing
play on a song.  You should see your script executing lame and doing
realtime transcoding.
