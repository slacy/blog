Title: URL Shorteners: Not destroying the internet, but destroying how we measure it. 
Date: 2010-04-15 12:06
Author: slacy
Category: General
Tags: http, location, redirect, url shortener
Status: published

For some work on [Parents Guild](http://parentsguild.com/)we've been
doing experiments with links from URL shorteners.  As you may know, URL
shorteners are the norm for services like Twitter, FriendFeed, and
FaceBook.

Here's the problem:
-------------------

When someone shortens a link to our site, this effectively destroys the
HTTP Referrer information.

What does that mean?  That means you lose all track of where the click
came from, and you can't tell who's clicking on what.  Traffic from URL
shorteners like bit.ly, fb.me, ow.ly, etc. all look *exactly* the same
as if the user has typed your URL in their location bar.  This is
unacceptable.  There is no way to use **any** analytics software to say
"Show me incoming links from the following tweet" or "show me incoming
links from bit.ly".   To help mitigate this problem, most URL shorteners
have implemented their own analytics solutions, but with literally
dozens of shorteners out there, this is an untenable solution for
website maintainers.  I want all my analytics on Google Analytics, or by
some means of parsing my own log files, thank you very much.

**What's actually going on here?**

Here's how things are supposed to work without URL shorteners:

A page on htttp://example.com/page.html contains a link that looks like
this: &lt;a href="http://destination.com/target.html"&gt;a
link&lt;/a&gt;.  When the user clicks on "a link", their browser sends a
request to destination.com with "GET /target.html" and some other header
information.  One critical piece of information is the Referer: HTTP
header, which for this case would be "http://expample.com/page.html". 
This indicates to the web server at destination.com that the link is
from example.com, and this fact can be logged and tracked.  Analytics
programs, like Google Analytics, or any analytics that are based on log
parsing, can see this Referrer field, and figure out who's linking to
your site, and what the URLs of those links are.

But, when links are shortened, http://example.com/page.html contains a
link like &lt;a href="http://bit.ly/AbCxYz"&gt;a link&lt;/a&gt;.  When
the user clicks on "a link", their browser connects to bit.ly, and it
issues "GET /AbCxYz".  It sends the referrer of
"http://example.com/page.html" to bit.ly, who then responds with "Oh,
yeah, the location is actually http://destination.com/target.html". 
This redirect information doesn't include the fact that the original
page was on example.com!  The browser takes Location and fetches the
page from destination.com.  But, one key thing has been left out!  **The
browser doesn't know what the referring page is anymore, so it leaves
this field blank!**

Even if bit.ly (or the other shorteners, for that matter) included some
information in their redirect response that included the original
referrer URL, it would be up to the browser to "do the right thing" and
send this referrer along to the client.

Possible solution \#1:
----------------------

Amend the HTTP spec to include a new status code for URL shorteners to
use.   Call this "HTTP 312 Transparent Redirect".    It should behave
exactly as HTTP 302 does, except that the server response should take
the Referer string as passed from the client, and put it in the
response.  When the client sees a 312 response, it should take the
Location field and the Referer field, and make a request to the server
specified, and include a new header "Shortener" that has the URL of the
shortened link for this request.

Pros: Fairly clean, reasonable extension to the existing protocol.

Cons: Requires new HTTP version, as well as new browser versions to work
right.  Older browsers wouldn't parse these headers.  Not sure how this
would work with JavaScript based analytics like Google Analytics.

Possible solution \#2:
----------------------

Add a field to robots.txt that says "shortened links should add these
HTTP GET parameters"  It would look something like this:

    Shortener: *
    Allow: /
    RefererArg: src
    ShortenerId: shrt

Then, when bit.ly constructs shortened links to my site, it would make
something that looks like this:

    Location: http://destination.com/target.html?src=http://example.com/page.html&shrt=http://bit.ly/AbCxYz

(This would be properly URL encoded, of course)

URL shorteners would then periodically crawl robots.txt of the sites
that they're shortening, and append these query params when they pass
through shortened links.

The syntax outlined above also has the important behavior of disallowing
shorteners for a gives site, as we can similarly do for well-behaved
crawlers.  This means that a site can control the known shorteners that
are producing links to it's sites!

Google Analytics could then also crawl the robots.txt file, understand
these shortener parameters, and display the proper referrer and
shortener information.

What can we do about this now?
------------------------------

As a web developer, there's not a lot you can do.  One thing would be to
implement your own version of Solution \#2.  If you know you're going to
post a shortened link somewhere, you could construct a custom URL with
query parameters for your own tracking.  For exmalpe, one could
implement
http://destination.com/inbound/&lt;ANYTHING&gt;/actual/path.html that
would then issue **another redirect** to
http://destination.com/actual/path.html.  This solution sucks, because
the user has to pay the penalty of the extra redirect, which can be
upwards of 200ms in some cases.

Another possible solution is to implement something like
http://destination.com/target.html?shrt=bit.ly where you just log and
ignore the shrt= parameter, but it's there for tracking purposes.  This
is also sloppy, but works as well.
