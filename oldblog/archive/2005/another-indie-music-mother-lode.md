Title: Another indie music Mother Lode
Date: 2005-04-22 07:00
Author: slacy
Category: Music
Status: published

Okay, this is one of the biggest download sessions I've had in a while.
I found a bunch of music at [insound.com](http://insound.com/) and
started to scrape their song lists. Insound.com appears to be a CD store
for indipendent record labels, and they have quite a selection of 128k
mp3s available on their web site. They had put up more barriers than
other sites, but anyone who knows wget wouldn't have a hard time with it
-- they just were blocking any user-agent that didn't look legit. I'll
leave the details up to you, but you should just take the user agent
from your browser, and config wget to use that. Then, it'll all work.

The steps I followed were essentially:

1.  Use my regular browser to start looking at the "browse by
    artist" pages.
2.  Write a perl scrpt that would generate every URL in the entire
    "browse by artist" section.
3.  Take the URLs from the previous step, and fetch them via wget. This
    resulted in about 1040 web pages.
4.  Take the HTML files from the previous step, and use a perl script to
    look for the mp3 downloader script (download.cfm, in this case) and
    pull out each URL into a separate file.
5.  Use wget to fetch the resultant mp3 files -- there were about 2180
    files taking up a total of 8Gb of mp3 files
6.  Write another perl script to rename the files to have reasonable
    names that end in ".mp3" instead of "download.cfm..."

You can find the song list [here](http://slacy.com/music)  
  

