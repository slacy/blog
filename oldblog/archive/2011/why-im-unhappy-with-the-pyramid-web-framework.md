Title: Why I'm unhappy with the Pyramid web framework. 
Date: 2011-02-25 23:04
Author: slacy
Category: General
Status: published

Here I am, writing this post instead of coding.  Why?  Because I'm
having to read through the
[Pyramid](http://docs.pylonsproject.org/docs/pyramid.html) source code
trying to figure out what the heck is going on with configuration.  Or,
to be more specific, how can I load module X when I'm in production, but
module Y when I'm in development.

I find myself in this state pretty often, and I don't mind reading the
source code.  Often times when using [other
frameworks](http://djangoproject.org), I'd learn something new about
Python when reading the source.

At it's heart, the problem with Pyramid is also what makes it great:
 They don't prescribe any one way to do anything.  It's totally agnostic
to which database, template engine, session framework, and auth/auth
framework you want to use.  This is what I like.  What I don't like is
that it also seems to not be able to make up it's mind about some
things.  Is it repoze? Is it zope?  Is it paster?  Is it pyramid?

When I read the source to Pyramid, it makes me throw up in my mouth a
little bit.  Here are the high level points about Pyramid that really
get on my nerves:

-   Configuration.  You can configure this thing in 3 different ways.
     zope's ZCML (XML-derived language), via the paster config language
    (looks like Microsoft .INI files), and via declarative configs (the
    Python code).   Why in the world they need 3 different ways to
    configure 1 framework is beyond me.
    <p>
    There's a class for "Settings" and 2 different classes both named
    "Configuration", one in pyramid.config, one in pyramid.configuration
    with odd deprecation messages in both places.  How can a web
    framework that just hit 1.0 have deprecated APIs?
-   Reliance on zope and repoze, paster, WebOb, Pygments, and a million
    other little libraries.  This means that figuring out something
    simple by reading code or docs leads down to bouncing between 2 or
    even 3 different libraries, trying to understand how they all
    fit together.  This is unnecessary and annoying.
-   zope.interface  Yes, this is super-annoying.  I'm not sure what
    value it adds, and seems very non-Pythonic to me.  I've never seen
    any other code that does this.
-   Anything related to zope.  It sucks.  ZODB?  Seriously?  Who would
    start a project today using this thing?  It seems to have stuck it's
    legacy fingers in all over the place.  For example, routes vs.
    traversal.  Every other framework I've ever seen/used is doing
    something like routes.  Traversal (as best as I can tell) seems to
    be a ZODB-ism that's worked its way in there, and confuses people
    all the time.
-   Lack of organized documentation.  The Pyramid web site looks great,
    but the actual contents of the documentation leaves a lot to
    be desired.  Figuring out simple things like configuration
    parameters, routes or traversal, which database to use (and how),
    user & session objects, auth/auth, etc.  It's all a mess.  Each
    section starts of with some great version of "Pyramid supports
    whatever you want" and then devolves into minutia of several
    possible half-baked solutions.

My recommendations for the Pyramid team:

1.  Ditch zope.  Yes, the whole thing.  Ditch ZCML, ZODB and traversal.
2.  Ditch paster.  Like Pyramid itself, this feels good on the surface,
    but gets itchy under your skin.
3.  Ditch repoze.  Take the parts you depend on, and pull them right
    into Pyramid itself.  Don't depend on all of repoze just because
    you can.
4.  Keep the flexibility, but start with a sane default.  Default
    to routes.  Default to a reasonable session implementation.  Default
    to a reasonable auth/auth implementation.

<span
style="font-size: 15px; font-family: Georgia, 'Bitstream Charter', serif; line-height: 28px;">I'm
stuck with Pyramid for now, but since I'm still fairly early in this
process, I'm going to start looking around to see what it takes to
switch to another framework (likely flask or bottle, but I'm not
sure)</span>
