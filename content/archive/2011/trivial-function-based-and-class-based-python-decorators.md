Title: Trivial function-based and class-based Python decorators.
Date: 2011-02-09 14:43
Author: slacy
Category: General
Tags: decorator, python
Status: published

Here's a trivial function-based decorator:

    def wrap(method):
        def call(*args, **kwargs): 
            print "calling wrapped method" 
            return method(*args, **kwargs)
        return call

    @wrap
    def some_function(arbitrary, arguments=None):
        print "%s %s" % (arbitrary, arguments)

And here's a trivial class-based decorator:

    class Wrap(object):
        def __init__(self, method):
            print "construct"
            self._method = method 
        def __call__(self, *args, **kwargs): 
            print "call" 
            self._method(*args, **kwargs)

    @Wrap
    def some_function(*args, **kwargs): 
        print "Inside %s %s" % (str(args), str(kwargs))
