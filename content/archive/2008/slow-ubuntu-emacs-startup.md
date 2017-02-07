Title: Slow ubuntu emacs startup
Date: 2008-12-30 11:10
Author: slacy
Category: General
Status: published

I found that starting emacs (under X11) was quite slow after I changed
the default font.  After googling around for a while, I found [this
great post](http://slated.org/fix_emacs_slow_startup) that says to add:

    (modify-frame-parameters nil '((wait-for-wm . nil)))

To your .emacs file. I did it, and it made startup zippy fast. (NB: I
added it to my (cond (window-system ...)) section.
