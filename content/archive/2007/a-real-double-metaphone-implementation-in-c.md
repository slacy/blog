Title: A real double metaphone implementation in C++
Date: 2007-05-20 21:34
Author: slacy
Category: Linux Stuff, Web
Status: published

I've been doing some work on a baby name explorer web app, and I needed
a good C++ implementation of the [double
metaphone](http://aspell.net/metaphone/) algorithm. There are several C
and C++ implementations mentioned on the web site, but most of them are
chock full of usage-specific junk, like Perl strings, Microsoft Visual
Studio cruft, etc. So, I took the C implementation from the Perl module,
removed all the perl string code, and replaced in with STL strings.

It works great, and I'm on my way to a proper baby name explorer web
app. [Here's the derivative C++ double-metaphone
implementation](http://github.com/slacy/double-metaphone).
