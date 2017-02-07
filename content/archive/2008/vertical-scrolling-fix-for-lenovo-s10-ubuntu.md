Title: Vertical scrolling fix for Lenovo S10 (Ubuntu)
Date: 2008-12-13 21:54
Author: slacy
Category: General, Photos
Tags: lenovo s10, linux, synaptics, synaptics driver, ubuntu, xorg
Status: published

So, the Lenovo S10 works great with Linux, particularly Ubuntu 8.10, but
the one thing thats a bit wonky is the way the trackpad works.  The
trackpad is non-square, but reports square coodinates, so the vertical
motion is exaggerated.

I've compiled a hacked version of the X11 Synaptics driver that includes
a fudge factor for the Y component.  It does hw.y \*= 0.6 internally,
and this pretty much compensates for the incorrect coordinates.

[Here's a link to a modified replacement Ubuntu .deb
package.](http://slacy.com/blog/wp-content/xserver-xorg-input-synaptics_0.15.2-0ubuntu7_i386.deb)

Just download that file, and then run:

dpkg --install xserver-xorg-input-synaptics\_0.15.2-0ubuntu7\_i386.deb

And you should be good to go.  If/when the Ubuntu maintainers publish a
new or upgraded version of this package, this version will be
overwritten, so you'll be SOL.  So, be careful with those autoupgrades!

In other news, there are patches underway to do this in a more
configurable way, and its possible that future versions of the Synaptics
driver will include the ability to adjust the vertical sensitivity.
