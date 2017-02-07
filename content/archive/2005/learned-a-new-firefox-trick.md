Title: Learned a new Firefox trick
Date: 2005-09-07 15:37
Author: slacy
Category: Web
Status: published

This is really really great Firefox trick that I learned the other day.
Its based on their support for "Keywords" for Bookmarks.

First, I'll describe a Keyword: A Keyword is a text name for a bookmark
that you can type into the location bar instead of typing the full URL
or clicking on the bookmark. For example, you could bookmark
http://google.com, and then give it a keyword "g" and then just type "g"
in the location bar to go to google. To set the keyword for a Bookmark,
create the bookmark, then right click on it and select "Properties".
That dialog box has an item called "Keyword" that you can set.

Got that?

Okay, now comes the fun part. If you create a bookmark with a keyword,
and the URL to the bookmark contains the string "%s", then when you type
the keyword in the location bar, everything after the keyword gets put
in the "%s" part of the bookmark URL. What does all that mean? It means
you can create a bookmark to a URL like this:

http://www.google.com/search?hl=en&q=**%s**&btnG=Google+Search

And assign it the keyword "g", then in the location bar, type "g slacy"
to go straight to the google search results for "slacy". Pretty cool,
huh? Not impressed? Think of things like this:

http://local.google.com/local?hl=en&lr=&c2coff=1&q=%s&near=94041&btnG=Search&sc=1&rl=1
with the keyword "mtv" to do google local searches in Mountain View.

http://google.com/movies?near=94041&q=%s with the keyword "movie" to do
movie searches in Mountain View.

Or anything else you could possibly imagine. Its great for intranet
searches too!
