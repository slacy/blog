Title: Shuttle SS51 performance problems.
Date: 2005-11-13 01:23
Author: slacy
Category: Linux Stuff, Web
Status: published

I've been living with a Shuttle SS51 system for my main desktop and
server for about 3 years now. It seemed fast when I first built it (P4
2.4GHz) but now its feeling a lot sluggish. I started to do some
benchmarking to see if I could pump up the performance, and here's what
I found:

- The default memory clock settings are way to low, @100MHz. The CPU I
have goes up to 166MHz. This is an effective increase of about 50% from
100 to 166. (Note: I had it set at 166 all along, but found the default
disappointing). There's also a mystery "Auto-Detect DIMM clock" setting
that boosts performance quite a bit.

- Small Form Factor PC's seem cute, and look great on your desktop, but
having them on the top of your desk just means that the noise they
generate is closer to your ears. The system (fans, HDD) has gotten
significantly louder over time, and now its really annoying. When new,
it was pretty good. I think this is mostly caused by the Maxtor drives
that I have in there now. I'm going to stick with Seagate Barracuda's
from now on.

- The onboard VGA system takes away about 11% of your memory bandwidth
if you're running 1280x1024 @16bpp. If you run 1280x1024 @24bpp, it uses
up about 20% of your memory bandwidth. This is what I learned today, and
I'm **really** disappointed. The system is using a shared memory
architecture for the onboard VGA system, which I've been using because I
don't want to add a huge powerhungry (and hot) graphics card. I'll never
make that decision again.

- The fan had gotten really loud, so I ripped an old one out of another
case and replaced it. Huge difference.

- I chopped out the fan grill to increase air flow. The highspeed
setting of the fan doesn't come on much anymore.

So, I went down to my [favorite pc supplier](http://pixelusa.com) and
had them spec out a new system for me. It should be ready on Tuesday,
and I'll start my adventure into 64-bit. The specs of the new system
are:

- Athlon 64 x2 4400+ (Dual Core)  
- 2G RAM  
- 3 \* 250G Seagate Barracudas, running RAID5 (Linux Software Raid)  
- NVidia fanless GPU  
- Antec P180 Case (quiet)  
- Antec NEO Power Supply (efficient)

The one thing that PixelUSA doesn't have a great selection of is heat
sinks. I'm planning on using a fanless [Scythe
Ninja](%20http://www.silentpcreview.com/article251-page1.html) to get
the job done. I was skeptical of the fanless designs, but I'm fairly
certain that if you have a case with good air flow, that its all the
same in the end.

I'm going to continue using Fedora Core 4 on that system, after
considering switching to Ubuntu. Ubuntu looks good, but seems like more
of a desktop distribution than FC4.
