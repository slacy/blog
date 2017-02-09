Title: More Python style discussions.
Date: 2010-07-14 13:38
Author: slacy
Category: General
Status: published

So, I work with a lot of code that likes to do stuff like this:

    def process(some_dict, some_key):
      sum = 0
      value = some_dict.get(some_key, None)
      if value is not None:
        sum += value
      return sum

but I find the use of get() to be really gratuitous (especially in this
case) and would rather write:

    def process(some_dict, some_key):
      sum = 0
      if some_key not in some_dict:
        return sum
      sum += some_dict[some_key]
      return sum

But I'm sympathetic to the original author's form, because in my form,
I'm querying the dict twice, whereas in theirs, they're doing it once. I
guess another alternative would be:

    def process(some_dict, some_key): 
      sum = 0 
      try: 
        sum += some_dict[some_key]
      except KeyError: 
        pass
      return sum 

I'd love to hear your thoughts on which of these is the most Pythonic
(or maintainable, or readable) form for this kind of logic.

Note that these examples are purely synthetic, and there's usually an
extra set of looping to calculate the sum. I've just simplified things
to make it look nice.
