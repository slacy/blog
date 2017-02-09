Title: mp3 encoding/transcoding commandline
Date: 2005-12-28 14:49
Author: slacy
Category: Music
Status: published

I was trying to remember this, and then I did:

lame -preset &lt;kbps&gt; &lt;input .wav&gt; &lt;output .mp3&gt;

Switching kbps to some interesting number (64,80,128, etc.) changes a
bunch of parameters, like filtering, bitrate, etc. Its better than the
"-vbr-new -V ..." style, because it encapsulates all those parameters.
It does use the "abr" style encoding, which means that the bitrate
specified can be \*any\* bitrate, not just the normal ones. I think I'm
using 112kbps (average) for my streaming server.
