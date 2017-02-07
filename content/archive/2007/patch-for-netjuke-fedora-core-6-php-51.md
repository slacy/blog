Title: Patch for Netjuke & Fedora Core 6 & PHP 5.1
Date: 2007-03-09 09:47
Author: slacy
Category: Linux Stuff, Music
Status: published

After upgrading to FC6, which includes PHP 5.1, when I clicked on the
"play" icons in the Netjuke UI, the playlist would show in the browser
instead of starting playback. The problem seemed to be that Netjuke was
now returning "text/html" for the mime type of the generated .m3u,
instead of whatever it used to be. The problem boiled down to some
simple code in play.php. To fix the problem, change the following line:

> header ("Content-type: audio/x-mpegurl\\r\\nContent-Disposition:
> inline; filename=netjuke-".substr(time(),-7).".m3u" );

to

> header ("Content-type: audio/x-mpegurl");  
> header ("Content-Disposition: inline;
> filename=netjuke-".substr(time(),-7).".m3u" );

I'm not sure why they originally wrote it that way -- its a really silly
way to set 2 headers at the same time. Too bad Netjuke isn't maintained
anymore... :(

P.S. [Jinzora still
blows.](http://slacy.com/blog/index.php/2006/09/05/jinzora-still-blows/)
