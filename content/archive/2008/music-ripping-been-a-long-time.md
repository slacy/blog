Title: Music ripping (been a long time!) 
Date: 2008-02-05 21:53
Author: slacy
Category: General
Tags: scraping, squar3, wget
Status: published

Its been a long time since I've scraped a site that has a bunch of music
tracks on it, and its kind of fun in that "I feel like a hacker but I'm
not doing anything illegal" kind of way. Clearly its wrong to download
gigs upon gigs of music from someone's server, but when its a publicly
accessible directory and there's a blog with a bunch of links, how can
you feel bad about it? Today's target is squar3.com.

So, first we:

> \# wget -N -r -R".mp3,.zip,.mov" -X"/" http://squar3.com/site/traxx

Which produces a bunch of index.html files (and a bunch of foo?N=D type
files. I diff'd those, and they look identical, so I just nuked them
with a "find . -print0 -iname "\*?=?" | xargs -0 rm") Then, you can rip
through those files and pull out all links to mp3 files, using something
like this:

> \# find . -print0 -iname "\*.html" -exec perl -n -e 'if (\$\_=\~/A
> HREF="(.\*.mp3)"/) { print \$1."\\n"; }' {} \\;

And then you can fairly easily pull out [a list of all the URLs for the
entire site](http://slacy.com/blog/wp-content/squar3.urls), and then use
"wget -i" to get all the files. Easy!
