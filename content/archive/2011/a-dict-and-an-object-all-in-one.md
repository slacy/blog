Title: A dict and an object, all in one.
Date: 2011-02-15 12:38
Author: slacy
Category: General
Tags: dict, mongodb, python
Status: published

I've been struggling with data modeling decisions for my MongoDB
interface layer.  Should results from the DB look like a dict, or like
an object?  Like both?  What are the advantages and disadvantages of
each approach?  I've got my own opinions on this, but thought I'd share
this interesting technique, making something behave as either a dict or
an object, in a very easy way:

    class Dicty(dict, object):
        def __init__(self):
            self.__dict__ = self

    d = Dicty()
    d['foo'] = bar
    print d.foo
    d.foo = 'baz'
    print d['foo']
    print d
    print dir(d)
