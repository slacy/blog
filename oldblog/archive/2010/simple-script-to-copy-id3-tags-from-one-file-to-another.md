Title: Simple script to copy id3 tags from one file to another.
Date: 2010-11-28 20:32
Author: slacy
Category: General
Tags: id3, lame, mp3, python, tagging
Status: published

I use lame for batch transcodes of mp3 files, for when I want to put
them on a CD-R, or on my phone.  I transcode them down to a much lower
bitrate than what I store on my server.

But, if I just use lame for this transcoding, it dosen't copy the id3
tags properly.  I needed to write a script to copy the id3 tags from the
source file to the new, lower bitrate file.  Here's the script:

    #!/usr/bin/python
    import sys
    from mutagen.id3 import ID3

    source = ID3(sys.argv[1])
    dest = ID3(sys.argv[2])
    for key in source:
        dest[key] = source[key]
    dest.save()

There's two tricks to using this properly:  
1. The file being tagged ("dest" above) must already have some id3
header in it.  
2. The mutagen library writes out id3 v2.4 tags that many programs don't
understand, so I use a second program to copy the id3 v2.4 tags to id3
v2.3. Here's the complete transcoding script with the call to "cpid3.py"
which is above:

    #!/bin/bash
    TMPFILE=$(mktemp).mp3
    lame --add-id3v2 --pad-id3v2-size 1024 --quiet -f --preset fast medium "$1" "$TMPFILE"
    ~/bin/cpid3.py "$1" "$TMPFILE"
    eyeD3 --to-v2.3 "$TMPFILE"
    mv -f $TMPFILE "$1"
    echo "Done with: $1"
