Title: Scraping insound.com (again)
Date: 2006-03-19 09:56
Author: slacy
Category: Music, Web
Status: published

[insound.com](http://insound.com), an online record store, provides lots
of free high quality mp3 samples. They're always putting new stuff live,
so its worth coming back and scraping them every once in a while. I
wrote a [simple perl script](http://slacy.com/music/scrape) to do this
automatically. Note that this is the single largest scrape in my whole
music collection -- over 9.5G of music, \~3000 files, so don't run this
perl scrpt if you don't have the space and time to let it run. The good
side is that insound has lots of good artists, and if you put this stuff
in your collection, you're sure to find something thats worthy of
purchasing from their site.

Note that you'll have to spoof your user-agent if you want to get a good
wget from insound. It disallows things that don't look like a real
browser.
