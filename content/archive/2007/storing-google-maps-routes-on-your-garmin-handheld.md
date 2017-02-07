Title: Storing Google Maps routes on your Garmin Handheld
Date: 2007-12-19 08:37
Author: slacy
Category: General
Tags: garmin, garmin vista cx, google maps, gpsbabel, kml, vista cx
Status: published

So, I set out last night to store [this route in Bear Valley,
CA](http://maps.google.com/maps?f=d&hl=en&geocode=9936204321909569547,38.471030,-120.049946%3B6202449343810219082,38.459740,-120.047810&time=&date=&ttype=&saddr=Snowshoe+Rd+%4038.471030,+-120.049946&daddr=38.461419,-120.042136&mra=dme&mrcr=0&mrsp=1&sz=16&sll=38.464258,-120.045526&sspn=0.011173,0.020084&ie=UTF8&t=h&z=16&om=1)
from Google Maps onto my Garmin Vista Cx handheld. We're probably going
to be walking that route, and I wanted to make sure that we don't get
lost.

The first step is to take the URL from above, and postpend "&output=kml"
to it, and save that as a file called something like "bv.kml". [Taking a
look at the KML file](http://slacy.com/blog/wp-content/bv2.kml), I can
see that its got a sequence of Placemark entries with directions, as
well as a LineString that has the actual detailed route. What I want to
do is take the LineString segment, turn it into a GPX Track, and load
that Track onto my Garmin.

As far as I can tell, [gpsbabel](http://gpsbabel.sf.net) can't translate
the LineString into a Track inside a GPX file. It will output the
Placemark entries into GPX, which is good, but it doesn't seem to be
able to do the Route.

The good part is that the LineString is an easy to understand format, so
I just [hand-crafted a GPX
file](http://slacy.com/blog/wp-content/bv3.gpx) with a track that has
those coordinates. Then, I used gpsbabel to upload to my Vista Cx.
Voila! I've got the track stored and I can use the GPS to follow it!
Here's the gpsbabel commandline that I used:

> \# rmmod garmin\_gps  
> \# gpsbabel -r -t -i gpx bv3.gpx -o garmin -F usb:
