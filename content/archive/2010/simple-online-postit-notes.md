Title: Simple online PostIt notes.
Date: 2010-04-26 21:29
Author: slacy
Category: General
Tags: demo, notes, postit, qostit, sticky notes, web stickies
Status: published

I've been really wanting a simple, online PostIt solution for a really
long time, and as part of my learning Django, jQuery, and jQuery Ui, I
finally realized that making one myself was actually not going to be
that hard.  And, it's now working and "shipped" on slacy.com, but before
I give you a link, I want to explain how it works.

There's no security.  There's no login/logout.  It's all based on
security through obscurity.  When you create a Board to put notes on,
it's assigned a random URL.  Think of this URL as your password.  Don't
give it to anyone you don't want to see your notes.  You can change the
URL, but this will make your Board easier to find.

Although multiple people can be viewing (and editing) a Board at the
same time, I'm not currently showing real-time updates, so you'll
totally clobber each others changes.  You can reload the page to see if
there are any other changes.

[With that, I present to you a demo board.  Please don't rename
it.](http://slacy.com/qostit/demo)

If you want to create your own Board, you can [start at the
top](http://slacy.com/qostit).

Any feedback would be greatly appreciated.  Things I know I want to do:

-   Adding a "password" to Boards.  So, you'd need to know both the URL
    and the password to view.
-   Doing proper realtime updates when 2 (or more) people are editing
    notes at the same time.
-   Themes & coloring.
-   Ability to iconify notes.
-   Mobile interface for phones.

I don't have time to do all this, so if you want to help out, let me
know. :)
