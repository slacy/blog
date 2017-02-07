Title: Simple python decorator example
Date: 2009-09-17 19:55
Author: slacy
Category: General
Status: published

I'm learning how to write a simple Python decorator function, and
couldn't find a good example on the 'net.  So, here's one:

>     #!/usr/bin/python
>
>     def simple_decorator(orig_function):
>       # This inner function should have the same call semantics as
>       # the function that you're decorating.
>       def decorator(c,d):
>         c = c + 1
>         d = d + 1
>         # Here's where we call the original function, but in this case, with
>         # modified arguments.
>         result = orig_function(c,d)
>         # And here, we return the result
>         return result
>
>       # Here 'decorator' is our compositing function
>       return decorator 
>
>     @simple_decorator
>     def add(a,b):
>      return a+b
>
>     a = 1
>     b = 2
>     print add(a,b)
>     print a
>     print b
