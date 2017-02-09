Title: Throttling pipes in ubuntu linux using cstream
Date: 2009-08-24 13:06
Author: slacy
Category: General
Tags: cstream, linux, pipe, throttle, throttling, ubuntu
Status: published

When I stream music from my home to my work, I want to make sure that I
throttle my music such that it doesn't saturate my outgoing network
connection and make the rest of my internet slow.

All I wanted to do was throttle a stdout pipe that's being sent to the
music player.  I found reference to a utility called
[throttle](http://klicman.org/throttle/), but also found that it isn't
included in the Ubuntu 9.04 distribution.

There's a maliing list post that says that the program cstream will do
the same thing.

man cstream says:

> -t num    Limit the throughput of the data stream to num bytes/second.
> Limiting is done at the input side, you can rely on cstream not
> accepting more than this rate. If the number you give is positive,
> cstream accumulates errors and tries to keep the overall rate at the
> specified value, for the whole session. If you give a negative number,
> it is an upper limit for each read/write system call pair. In other
> words: the negative number will never exceed that limit, the positive
> number will exceed it to make good for previous underutilization.

So, I changed my audio transcoding script to say:

> lame --quiet -V6 \$FILE - | cstream -t 25000

The number "25000" comes from the fact that I don't want to use more
than 192kbps of my outbound stream, and cstream's argument is in bytes
per second.  192kbps = 24000 bytes/second, and I added a little extra. 
It would probably be safer if I also passed "-B 192" to lame, but that
would actually limit my overall quality, so I'm just going to cross my
fingers and hope that "-V6" doesn't produce &gt;192kbps for very long.
