Title: HTTP Pipelining Considered Harmful
Date: 2005-06-13 22:26
Author: slacy
Category: Linux Stuff
Status: published

I just want to say that the more I learn about [HTTP
Pipelining](http://www.mozilla.org/projects/netlib/http/pipelining-faq.html)
the less I like it.

My first encounter with it was with one of those "Speed Up Firefox"
pages. Surprisingly, even the [mozilla
home](http://www.mozilla.org/support/firefox/tips#oth_pipelining) page
mentions this.

The problem with Pipelining is that it says that you can send multiple
requests down the same pipe before any results have been returned, or
even while results are being sent. This creates a whole host of problems
with respect to request ordering, because the first request must reply
before the second. This means that the second request is left in
limbo-land for the whole time of the first. What if the first request
closes the connection? What if the first request takes a really long
time? What if the first request never finishes?

You should **NOT** enable pipelining on Firefox! There are so many [make
firefox faster](http://www.google.com/search?q=firefox+faster) web pages
out there! DO NOT DO THIS.

To see one example of how bad HTTP Pipelining can be, follow the
instructions to turn it on, and then visit [Google
Maps](http://maps.google.com).

The main premise of most of these "Speed Up Firefox" pages is that
without pipelining, Firefox makes only one request to a site at once.
This is absolutely **not true**. The parameters
"network.http.max-connections"
and"network.http.max-connections-per-server" control how many
simultaneous (non-pipelined) requests are made to each server.
Pipelining makes more of them on the same connections, which leads to
many problems, and is a poorly supported feature in many web servers.
