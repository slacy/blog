Title: More thoughts on RESTfulness. 
Date: 2012-02-28 12:00
Author: slacy
Category: General
Status: published

Here are some more brief thoughts on why extreme RESTful ness is a bad
idea:

> As soon as you're debating whether an API endpoint should be a PUT,
> POST or PATCH, you're wasting your time.

If you, as the API developer, can't decide which method is appropriate
for a given action, then you're almost certainly designing your APIs in
a way that's making them difficult to use.  For example:

What HTTP method would you use for updating the password on a user
account?

1.  Use HTTP PUT because it's a "modification of the User object"  But
    technically PUT is supposed to be idempotent, so you have to send
    the full user record in the request, but users aren't allowed to
    update some aspects of their data, like username, so you send these
    fields to be RESTful but just ignore the data in your backend.  To
    make this happen, you have to roundtrip the entire user record to
    the client, and use a PUT with an If-Modified-Since header to avoid
    race conditions.
2.  Use HTTP PATCH because "that's the more restful way to do it now
    that we know about the new PATCH method" and you use a JSON
    encoding, which is nice for you as the developer, but hard for
    clients to issue (think: wget clients).
3.  Use HTTP POST because "it's what the web has been doing for the last
    decade."  It works, it's simple, and well defined.  It's fully
    supported by every HTTP client out there.  Everybody understands how
    to POST and what it means.

You tell me what the right answer is.
