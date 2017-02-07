Title: Striving for the perfect RESTful API is a fool's errand.
Date: 2012-02-28 11:40
Author: slacy
Category: General
Status: published

There's always a lot of talk on programmer's blogs about RESTful APIs.
 Of particular note are articles [like this
one](https://github.com/rails/rails/issues/348), which talks about how
[Ruby on Rails is switching to a brand new HTTP method
"PATCH"](http://weblog.rubyonrails.org/2012/2/26/edge-rails-patch-is-the-new-primary-http-method-for-updates).

Here's the big issue:

### API design should have nothing to do with which transport you're using.

and

### HTTP is a transport layer.

Your API should (and probably will) work over at least two possible
transports.  The first "transport" is local function calls inside your
application itself.  The second transport is probably going to be JSON
or XML over HTTP, and there are tons of other possible transports people
might ask for or want to use, like [Google
Protobufs](http://code.google.com/p/protobuf/) over
[WebSockets](http://dev.w3.org/html5/websockets/).

### It needs to be as easy as possible for your clients to issue requests to your API.

Yes, it really does.  Make it easy.  Make it ***dead simple*** to use
your API.  As soon as you start down the path of "use form-encoded
fields and HTTP POST to create objects" and "use &lt;some encoding TBD
because PUT doesn't dictate an encoding&gt; and HTTP PUT to update
objects" **you're doing it wrong**.  Your clients don't care about the
transport (PUT vs. POST) they just want to get, create, update and
delete objects, and they want to be able to easily issue those requests
from whatever systems they already have.  In the case of HTTP, this will
probably be wget, curl, in-browser JavaScript and backend server-side
libraries.  Making your clients explicitly choose between the poorly
named PUT & POST is just nonsense.  Making them shoe-horn an alternate
encoding or even form-encoding for PUT requests is nonsense.  They don't
care at all.  In fact, they probably don't even care what the URLs are.
 They just want your API to be easy to call and to work reliably.

### Here's a perilous RESTy example:

Imagine your prototypical web-based chat application.  You're going to
need a way to say "get me new chat messages on a given channel."  So,
you come up with a URL like this:

/channel/&lt;channel name&gt;/updates

Your RESTy API design says "Use an HTTP GET and the If-Modified-Since
header to ask for new messages since the timestamp of the newest chat
item".  This sounds good.  It sounds right. It sounds RESTful.

Okay, great, so you implement the whole thing in your backend.  You have
your unit tests testing it, issuing requests to a test server via a
great HTTP library. Awesome.  It all works.

You pass off the API to your frontend development team.   They say "hey,
this looks great!"  A week and a half later, they come back to you and
say:

> I can't figure out how to properly get chat updates!  Every time I use
> the API I get all the chat messages, not just the new ones!

Ah! I know exactly what the issue is!  You're not properly setting the
If-Modified-Since header!  So, you go over to their desk and sit down,
and they pull up Chrome's Developer Tools.

> See, here's where I'm making the request from JQuery to your API.  I'm
> asking for /channel/foobar/updates via \$.ajax(...)  So, **HOW THE
> HECK TO I SET a custom value for If-Modified-Since?**

Reading the documentation, I believe this is possible via some
combination of the ifModified flag to \$.ajax(), and/or the beforeSend
function, and the XHR setRequestHeader function. But, you'll quickly
start reading [jQuery bug
reports](http://bugs.jquery.com/ticket/4918) and [Google Groups
posts](https://groups.google.com/forum/?fromgroups#!topic/jquery-en/-eec5qOKNDE) about
why this approach might not work, and we haven't even started talking
about how the string for the If-Modified-Since header has to be
formatted in a fairly particular way, so you'll probably need a custom
date formatting library.  Your coworker on the frontend team might say:

> Hey, so why can't I just pass a timestamp or better yet **an object
> sequence number** as a GET parameter  and just don't use this
> If-Modified-Since header since even if I can get it working, it's
> going to be half a dozen extra lines of code or a special utility
> function every time I call your API.

**"But that's not RESTful!"**  You'll shout!

And then you'll realize the mistake you've made.  In your quest to fully
exploit HTTP, you've made it pretty hard for your clients to actually
call your API.
