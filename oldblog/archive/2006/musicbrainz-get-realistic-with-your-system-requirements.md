Title: Musicbrainz: Get realistic with your system requirements.
Date: 2006-03-14 00:28
Author: slacy
Category: Linux Stuff, Music
Status: published

I saw that [musicbrainz](http://musicbrainz.org), which is an automatic
music identification and tagging system, just upgraded to a new acoustic
fingerprinting technology provided by [musicdns](http://musicdns.org).
The problem is that their "beta" code (picard-0.7b) has rediculous
system requirements.

Its not the hardware thats ridiculous -- its the software. They require
beta versions of basically every UI toolkit known to man. Mainly,
wxPython version 2.6. Listen guys: If its not part of the current
distribution of Fedora Core 4, then there's no way in heck that I'm
going to download and replace an existing package like this. The
dependencies could ripple through my whole system, and basically break
the whole thing.

Either:

-   Ship a statically compiled binary (not really possible with Python,
    but it should be listed for completeness)
-   Include a binary distribution of the libraries.

'nuf said.
