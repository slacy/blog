Title: How to split views.py into a directory (Django, Python)
Date: 2009-07-24 15:35
Author: slacy
Category: General
Tags: django, models, python, views
Status: published

So, I've been doing some Django programming on the side, and the thing
that annoys me is that Django forces you to put nearly all your source
code into 2 files:  models.py and views.py

Being a reasonable person, I wanted to have a separate file for each
view in my system.  In other words, I want to create a views directory,
with \_\_init\_\_.py inside, and my view files in there.  Not being a
Python expert, I found this harder than expected.  Here's what you need
to do:

1.  Create a views directory.
2.  Split views.py into one file per method in the new views directory.
3.  Edit views/\_\_init\_\_.py and for each view, say "from myview
    import \*"
4.  Use your views as you previously did in urls.py

I've heard some rumblings that you could create an \_\_init\_\_.py that
did something like go through every file in the current directory and
import everything there.  That seems a bit over the top, and I'm happy
to manage the imports in \_\_init\_\_.py for now.

I believe a very similar technique should work for Models, but I haven't
tested it.
