Title: Lenovo S10 first impressions
Date: 2008-12-08 21:33
Author: slacy
Category: General
Tags: lenovo s10, linux, netbook, ubuntu
Status: published

Okay, I've had my Lenovo S10 since Friday.  I briefly played around with
the default Windows XP install, upgraded the BIOS, and then installed
Ubuntu 8.10 as my primary disk, and wiped the OKR (One Key Recovery)
partition, since I don't really want to ever restore Windows.

Here are my first thoughts:

1.  The screen is actually more functional than I thought it was going
    to be.  1024x600 is just fine for pretty much everything.  There's a
    little more scrolling than normal, but nothing huge.  I do find that
    I am running Firefox in fullscreen mode more, so maybe that makes up
    for it.
2.  The keyboard is actually quite good.  There are only a few weird
    things.  The number keys are offset to the left a bit more than I'm
    used to, and that means I hit 2 instead of 1, for example.  There
    are some other keyboard quirks, like the \~ key and PgUp/PgDn
    buttons, but I'm sure I'll be able to get used to those.  The key
    autoreapeat happens a bit faster than I'm used to, and doesn't seem
    to be adjustable in Ubuntu.  (Although repeat on/off does work). 
    I'm just tapping faster than normal.  The keyboard is large enough
    that I can touch type at full speed with nearly no problems at all. 
    Excellent!
3.  The synaptics track pad works, but the vertical motion is way too
    fast, and I'm tracking an xorg bug and discussion on mailing lists
    about the patches that are proposed to fix it.  As soon as I can get
    a build of the .deb for people to check out, I'll do so.
4.  Battery life.  I only have the "3-cell" version, and people complain
    a bit about the battery life.  It seems to be working for 2.5-3
    hours for me, which is really just great for what I'm using the
    laptop for.
5.  The CPU is plenty fast, the graphics are plenty fast, and 1GB seems
    like plenty of RAM.  It really doesn't feel like it needs an
    upgrade.  I've even been doing some ./configuge && ./make stuff for
    the drivers, and it works speedily and well.   The Atom shows up as
    Dual Core, due to hyperthreading.  CPU Frequency scaling works, and
    the steps are 800Mhz, 1.07GHz, 1.33GHz, and 1.6GHz.
6.  It's very light, and seems very well built.  The LED backlit display
    is very bright (on full brightness, which I don't really use
    at night).

There are a couple of weird quirks, that I've mentioned above but will
reiterate here:

1.  Touchpad vertical movement is too fast.  I'm getting used to it, but
    it would be nice for it to be "normal".
2.  Screen brightness is very dim after a resume from suspend.  (Dimmer
    than anything I can set with the brightness buttons, and it returns
    to normal when I adjust brightness manually)
3.  I haven't tested video (webcam) or microphone yet, but sound
    works great.
4.  Keyboard quirks (\~, PgUp, Home, F12, are all hard to press.  There
    are buttons unused by Ubuntu (The 'Home' button and Windows
    Menu Button)
5.  I'm having a bunch of trouble with 3-button (middle mouse button)
    emulation in X11.  Supposedly the synaptics driver does it
    automatically, but I haven't delved into this much.  It does work,
    but just not predictably.  I'd like to just set some key+click combo
    to middle mouse.
6.  Keyboard key repeat rate is too fast and delay is too short,
    settings under Ubuntu don't seem to take effect. (this is minor, and
    I'm sure I'll get used to it)

