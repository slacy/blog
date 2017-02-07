Title: Python: str(None) should return '' not 'None'
Date: 2010-04-07 13:24
Author: slacy
Category: General
Tags: none, python, str
Status: published

Think about the following code:

    x = some_function_that_might_return_none()
    if str(x):
      do_one_thing()
    else:
      do_another_thing()

do you think do\_another\_thing() will ever execute?

Did you know that str(None) is 'None' and thus:

    if str(None):
      this_willl_always_execute()

I can see how you might want str(None) to be 'None' for debugging
display, etc., but to preserve the semantics of "if" I think it should
be '' or some other value that fails a simple if statement.
