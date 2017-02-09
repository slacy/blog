Title: Ripping SXSW 2008 mp3 files
Date: 2008-02-19 21:29
Author: slacy
Category: General
Tags: 2008, download, mp3, Music, sxsw, torrent
Status: published

I've grown impatient waiting for 2008.sxsw.com to release their torrent
of mp3 files. I'm wondering if they're going to do it at all.

So, I decided to just suck down the whole site and scrape out all the
URLs to all the mp3 files and download them. It was very
straightforward.

First, scrape the site by doing something like this:

> wget -nd -nH -r –no-parent -nc
> http://2008.sxsw.com/music/showcases/alpha/0.html

Then, do something like:

> grep mp3\_download \*.html

(Yes, they were silly enough to use a CSS class for all their mp3
download links named 'mp3\_download'.)

Then, you'll have a file with a bunch of raw HTML links. Pull that into
something like emacs and do some replace-regexp commands to trim it to
just the URLs themselves. (There are 740 of them). I then took the
resulting list of mp3s, split it into 2 files, and am running two copies
of wget in parallel to suck them all down. [Here's a copy of the list of
all 740 mp3 files](http://slacy.com/blog/wp-content/sxsw-2008-mp3s).

Send me an e-mail to my private account if you'd like me to hook you up
with a .tar.bz2 of all 740 files. I wonder if they'll release that
.torrent soon? :)

UPDATE: The download completed overnight, and the resultant files are
about 3.4GB.
