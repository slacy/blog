Title: Is there any way to finagle Python into supporting attributes with a '-' character in them?
Date: 2010-07-12 12:47
Author: slacy
Category: General
Status: published

Check out this bit of example code:

    class test(object):
      def __init__(self):
        # We use self.__dict__ here because of the odd name of the 
        # attribute. 
        self.__dict__['font-weight'] = 'bold'
        self.__dict__['height'] = '32px' 

    t = test()
    print t.height # WORKS 
    print t.__getattribute__('font-weight') # WORKS  
    print t.font-weight  # BROKEN: Syntax error

What I'm showing here is that the internal object structure supports
attribute names with special characters in them (like hyphen), but the
language syntax barfs when you try and access these attributes in a
normal manner.

Is there any way to "trick" the language into allowing for easy support
for attribute names with a hyphen or other special character in them?

I'm working my way towards expressing CSS selectors in native Python,
and want to make it easy for CSS developers to transition to the library
that I'm working on.   (Note that jQuery has this problem, and that they
use camel case for things like font-weight and margin-right, etc.)

Even worse, CSS uses terms like "class" and "id" that are reserved words
in Python, so there's pretty much no way around that issue.
