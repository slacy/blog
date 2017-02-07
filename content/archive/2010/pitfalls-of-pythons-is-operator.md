Title: Pitfalls of Python's 'is' operator 
Date: 2010-08-20 09:07
Author: slacy
Category: General
Tags: comparison, integer, is operator, long, python
Status: published

I saw [this post on
Friendfeed](http://friendfeed.com/python/826795fd/is-not-b-but-p-q-guess-why),
and thought I'd reproduce the code here, because it's a really
interesting Python snippet, and to me, basically says **never, ever use
the 'is' operator**.  Here's the snippet that I just reproduced on
Python 2.5.2 and 2.6.5:

    In [1]: a = 500

    In [2]: b = 500

    In [3]: a == b
    Out[3]: True

    In [4]: a is b
    Out[4]: False

    In [5]: p = 50 

    In [6]: q = 50

    In [7]: p is q
    Out[7]: True

Totally crazy, right?

The 'is' operator is testing "are these objects completely identical" In
other words, are they pointing at the same implementation. For basic
types like integer, things get complicated, because Python treats
integer values between -5 and 256 differently. There's some hint at this
when looking at the documentation for the function PyInt\_FromLong(),
which takes a C++ long and returns the Python integer representation of
that object. The comment there says:

> The current implementation keeps an array of integer objects for all
> integers between -5 and 256, when you create an int in that range you
> actually just get back a reference to the existing object.

And thus, values **outside** of that range have different
implementations, and thus, return False when comparing via 'is'.
 There's also some discussion of this on
[StackOverflow](http://stackoverflow.com/questions/306313/).
