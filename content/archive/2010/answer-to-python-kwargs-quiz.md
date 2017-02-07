Title: Answer to Python kwargs quiz!
Date: 2010-07-13 20:16
Author: slacy
Category: General
Status: published

In a previous post, I asked if anyone knew the difference between these
3 forms of kwargs:

    def printargs(**kwargs):
      print kwargs

    printargs(foo='bar')
    printargs(**dict(foo='bar'))
    printargs(**{'foo':'bar'})

Here's the answer:

In the 3rd case, where you're explicitly passing in the dict as kwargs,
and using the {}-style of declaring the dict, your dict keys can be
things that are Python reserved words, or invalid.  Take this, for
example:

    printargs(**{'class': 'something', '#': 'another'})

The 3rd syntax (and it's equivalents) are the only way to pass arguments
with reserved words like this.

Unfortunately, you can't declare your explicit kwargs arguments to be
these reserved words, so once you're doing things this way, you may as
well just be passing around a dict full of args instead of using the
\*\* operator to do it as kwargs.
