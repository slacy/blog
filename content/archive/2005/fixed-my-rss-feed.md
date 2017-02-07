Title: Fixed my RSS feed
Date: 2005-08-11 01:19
Author: slacy
Category: Linux Stuff, Web
Status: published

I knew my RSS feed was broken for some XML parsers, but I didn't know
why, and I didn't know how.

Well, I finally had the time to sit down and figure out what the problem
was. It boiled down to the fact that **many** XML parsers are insanely
anal about their formatting. Because of some WordPress plugin work that
I was doing, I had accidentally left a blank line in one of my .php
files, and that blank line made it to the top of the RSS feed. Because
XML says that the
"<?xml" entity must start on the first character of the file, i was generating an invalid xml feed.< p ?>

This is super annoying. I thought that XML was supposed to be a
human-friendly format. Barfing because of a single newline at the top of
a file seems rediculous.

Well, now Google can parse my feed (so you can add me to your iGoogle
homepage at http://google.com/ig) and so will Thunderbird, so I'm able
to see my own posts again. Whew!

I wonder how many other XML parsers this was effecting? I thought the
numbers would be low, but I guess if they're all using Xerces or
something, they were probably all broken in the same way.

Oh, and I also sort of blame WordPress for letting me get into this
situation in the first place. I can't believe that my plugin code was
effecting my RSS feed, but I guess anything is possible.
