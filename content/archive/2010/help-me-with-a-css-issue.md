Title: Help me with a CSS issue?
Date: 2010-04-23 10:07
Author: slacy
Category: General
Tags: absolute, advice, css, divs, help, html, offset, positioning, relative
Status: published
Attachments: blog/wp-content/uploads/2010/04/example.png

Hey, having issues with CSS+HTML again.  I'm working with a resizable
&lt;div&gt;, and I want to make sure that no matter what size it's
container, that I have a middle section that fills the "main" middle
area of the div.  [Here's a link to a simple example
file.](http://slacy.com/blog/wp-content/uploads/2010/04/foo.html) And
here's what it looks like:

[![](http://slacy.com/blog/wp-content/uploads/2010/04/example.png "example"){.aligncenter
.size-full .wp-image-1173 width="401"
height="400"}](http://slacy.com/blog/wp-content/uploads/2010/04/example.png)

What I want is for the &lt;div class="middle"&gt; to be the full height,
up to the "top" of the bottom element, and I don't want to have to
specify that height in pixels, since the container &lt;div&gt; can be
resized dynamically.  I know I could set the size of it programatically,
but there's got to be a valid pure-CSS way to do this, right?

I was expecting something like &lt;div style="top: 24px;
bottom:24px:"&gt; to work, but that's not working either.  ARGH!  Help!

P.S. One possible solution I've thought of is to have "middle" be
height:100%, width:100%, but then use margin-top and margin-bottom to
offset the desired 24px, and make sure that the top and bottom div's
appear on top of the middle one.  This also seems like a big hack,
though, and has some other drawbacks that I don't want to go into here.
