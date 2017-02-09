Title: Switched to realtime transcoding of my mp3s with Netjuke
Date: 2005-08-21 23:32
Author: slacy
Category: Linux Stuff, Music
Status: published

Well, I bought a bunch of actual Compact Discs the other day (a had been
craving a bunch of stuff thats not available on eMusic.). My new
strategy is to encode them as the highest quality mp3s I can. That means
using lame's "-preset insane" setting, which makes 320kbit CBR files.

The problem then comes when I try to play these back over the network --
I can only do 1 320kbit stream outbound on my DSL, and then it starts
choking on the bandwidth. So, I turned on realtime transcoding in
Netjuke to fix this. Now, everything is coded to VBR with an average of
around 128 kbit. That should allow plenty of headroom for multiple
listeners. Since its all done on the fly, I can change it to 192 or 224
or 256, or whatever I feel like, which is pretty cool.

I'm tempted to not use Netjuke's transcoding, and make a mod\_rewrite
script that just pumps all the mp3s through Lame. That way all my
streaming music applications will get the same transcoding scheme, and I
can use referrer and domain rules to turn transcoding on and off.
