Title: Ajaxian » Atmosphere: Comet Abstraction Framework
Date: 2009-03-16 09:10
Author: slacy
Category: General
Tags: ajax, bayeux, comet
Status: published

I've been reading a lot about Comet, which is also called Ajax Push,
Long Polling, etc.  There are lots of moving pieces involved to get a
working Comet server & client solution, and **lots** of people seem to
be trying to build server & client side frameworks that make it easier
to develop Comet applications.  Take for example, this one that I just
saw on [ajaxian.com](http://ajaxian.com)

> Atmosphere 0.1-ALPHA1 is now officially released and support Tomcat,
> Jetty, Grizzly and GlassFish. Finally a Comet/Ajax Push framework you
> can build on top of it and deploy everywhere!

via [Ajaxian » Atmosphere: Comet Abstraction
Framework](http://ajaxian.com/archives/atmosphere-comet-abstraction-framework).

I think this really misses a key point:  The success of Ajax has been in
it's simplicity and *lack* of standards and definitions.  It's easy to
craft up your own message format (XML, plaintext, json, Google Protocol
Buffers, etc.) and combine that with some easy to use client-side code
(i.e. XMLHttpRequest via JQuery) and craft up a nice workable website
that works with nearly any HTTP server, and any browser.

But, with Comet, the prevailing winds seem to be blowing in the
direction of heavyweight protocol specs (BOSH, Bayeux Protocol), heavy
server implementations ([cometd.org](http://cometd.org),
[lightstreamer](http://lightstreamer.com), etc.)  and heavy client
implementations like the one linked above.

I really believe that the future of Comet lies in a more ad-hoc
philosophy that says "whatever works for your application works"  
Layering extra levels of both server side and client side stacks is just
going to raise the barrier to Comet adoption in mainstream site
development.
