Title: Python object question about __setattr__ and __getattr__.
Date: 2011-02-07 16:25
Author: slacy
Category: General
Tags: getattr, python, setattr
Status: published

Okay, I'm making a mock "object-like" object out of a dict. Details
should be pretty much irrelevant. The behavior that I want is like this:

    o = ObjectLike()

    # Here, we construct and assign arbitrary nested objects of
    # type ObjectLike.
    o.foo.bar.baz = 'something'

    # We can see the nested objects:
    print o.foo
    <__main__.ObjectLike object at 0x7fe824b4a710>

    # And, here's the string value at the leaf: 
    print o.foo.bar.baz 
    'something'

    # Here's the trick.  I want the line below to raise an AttributeError:
    print o.queeg

The only way I was able to get the nested object assignment to work is
by overriding \_\_getattr\_\_ to create the nested attributes.  But,
that means that the last print line will print out an empty ObjectLike
object instead of raising AttributeError. Ugh!

Help?  Is this possible in Python?
