Title: I've given up on web-based music services.
Date: 2009-08-13 10:24
Author: slacy
Category: General
Tags: linux, mp3, mt-daapd, Music, sharing, ubuntu, Web
Status: published

It was a long and tumultuous affair, but now I've officially given up on
web-based streaming of my personal music collection.

I started out with netjuke, which died and got absorbed into the
horrible jinzora project.   So then I switched to Ampache, which worked
fairly well, but needs some serious UI upgrades/changes to make it
reasonably useful.

Now that I'm fully ubuntu-ized, I'm using mt-daapd through an SSH tunnel
to listen via a native client app.  This solution has lots of
interesting benefits:

1.  Running mt-daapd locally means other people in my house can see my
    music, including my TiVo and any other desktops with an iTunes/daap
    compatible frontened.
2.  I don't have to worry about security issues with having all my music
    accessible via a web portal that could be hacked.
3.  mt-daapd is available as a package in Ubuntu, so that means upgrades
    are easy.  Doing upgrades (by hand) of php-based web apps was really
    becoming a drag.
4.  This means less junk on my slacy.com web server, which I'm trying to
    significantly trim down and make more secure by having
    less applications.

