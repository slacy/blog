Title: Script to automatically download tracks from Pitchfork's Best New Tracks feed
Date: 2010-09-17 10:25
Author: slacy
Category: General
Status: published

Pitchfork has a nice [RSS
feed](http://feeds2.feedburner.com/PitchforkBestNewTracks) with their
"Best New Tracks".  Each feed post usually contains a link to an MP3
file you can download.  They're not using RSS media enclosures (i.e. a
podcast) so you can't just plop this thing in a standard podcast
downloader.

So, I wrote this script to scrape the feed and download any new links to
\*.mp3 files it finds in the &lt;decscription&gt; section of each feed
item.  It's fairly straightforward, and is smart enough to not download
the same file twice.

` #!/usr/bin/python`

from BeautifulSoup import BeautifulSoup  
import cgi  
import os  
import re  
import string  
import urllib2  
import urlparse

rss\_data = urllib2.urlopen(  
    'http://feeds2.feedburner.com/PitchforkBestNewTracks').read()

soup = BeautifulSoup(rss\_data)  
posts = soup.findAll('description')

mp3\_urls = \[\]  
for p in posts:  
    pstr = str(p)  
    pstr = pstr.replace('&lt;', '&lt;')  
    pstr = pstr.replace('&gt;', '&gt;')  
    desc\_soup = BeautifulSoup(pstr)  
    links = desc\_soup.findAll('a',
href=re.compile('.\*pitchforkmedia.\*mp3\$'))  
    mp3\_urls += \[l\['href'\] for l in links \]

for url in mp3\_urls:  
    u = urlparse.urlparse(url)  
    filename = os.path.basename(u.path)  
    enc\_url = url.replace(' ', '%20')  
    if not os.path.exists(filename):  
        print "Downloading: %s" % filename  
        song = urllib2.urlopen(enc\_url).read()  
        f = open(filename, 'w')  
        f.write(song)  
        f.close()  
    else:  
        print "Skipping: %s" % filename  
</code>

I'll leave the cron job setup up to you.
