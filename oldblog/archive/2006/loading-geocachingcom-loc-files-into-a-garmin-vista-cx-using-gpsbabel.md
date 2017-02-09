Title: Loading Geocaching.com LOC files into a Garmin Vista Cx using gpsbabel
Date: 2006-12-20 23:00
Author: slacy
Category: Geocaching, Linux Stuff
Status: published

Crazy title, I know.

If you've got a Garmin Vista Cx, Legend Cx, Vista Cx or similar, and a
Linux box, here's how to load a set of
[geocaching.com](http://geocaching.com) cache locations onto the unit:

First, download and install gpsbabel from
[SourceForge](http://sf.net/projects/gpsbabel). Make sure that you have
the package libusb-devel installed so that you get the usb drivers
correct.

Attach the Garmin via its USB cable.

rmmod garmin\_usb  
./gpsbabel -i geo -f geocaching.loc -o garmin -F usb:

That should do it!

Presumably this should work equally well on an OSX or Windows box as
well, since gpsbabel is cross platform.
