Title: How to tell when your method is on the wrong class.
Date: 2010-07-29 11:44
Author: slacy
Category: General
Status: published

1. Your code uses self on the RHS of an assignment.
---------------------------------------------------

Here's a Python example:

    class accumulator(object):
      def __init__(self):
        self.sum = 0 

    class value(object):
      def __init__(self):
        self.value = 0 

      def accumulate(self, accum_instance):
         accum_instance.sum += self.value

Instead of saying:

    a = accumulator()
    v = value()
    v.accumulate(a)

These methods should be re-arranged such that we don't have "self.value"
on the RHS of the assignment in the accumulate method, which would make
our calling code look like this:

    a = accumulator()
    v = value()
    a.accumulate(v)

The calling actually looks quite similar, but the semantics of who's
responsible for the work is more clear.

2. You have method names like "add\_to", "increment\_by", "combine\_with" or "compute\_from"
--------------------------------------------------------------------------------------------

Instead of calling "self.increment\_by(bar)" you should likely be
calling "bar.increment(self)"

Note, this violates one of my rules below of passing only "self" as a
method argument. At some point, the difference between foo.method(self)
and self.method(foo) becomes subjective, and it's your job as the
programmer to decide how these pieces of code relate to each other, and
where the functional separation lies. The best way to decide issues like
this is to try to come up with some rule for where methods live and
behave. The exact guts of "method" would need to be known -- is it
modifying self, or it's argument, or both? Try to come up with a rule
like "treat arguments as const wherever possible" and you may find that
these issues sort themselves out. You may even find that splitting a
class up, or joining two classes together might be a good solution to
make your code more readable.

3. Your method doesn't use "self" at all, or only very minimally.
-----------------------------------------------------------------

Here's another surprisingly common practice, a method that looks like
this:

    def some_method(self, foo, bar, baz):
      self.counter += 1
      foo.process(bar)
      bar.aggregate()
      baz.compute_from(bar)

This method should likely live somewhere outside of the current class,
and in the classes  
of foo, bar, or baz.

4. You're passing self (and no other arguments) as an argument to another method.
---------------------------------------------------------------------------------

If you have code that says:

    some_class.some_method(self)

Then you likely want to say:

    self.better_method(some_class)

Similarly, passing a handful of member variables from self to another
method is an indication that method should live in the current class.
 For example:

    some_class.some_method(self.foo, self.bar, self.baz)

could be rewritten as:

    self.better_method(some_class)

Unless better\_method would end up violating more of these rules. :)

5. Your method delegates most of it's functionality to another class or module.
-------------------------------------------------------------------------------

For example:

    def some_method(totally_reasonable_argument):
      other_class.process(totally_reasonable_argument)
      other_class.member_variable += self.size
      other_class.log(totally_reasonable_argument)

Look how every line calls into functions in other\_class (which could
also be a module). Clearly, this method should be living inside
other\_class and not on the current class.

6. Your method returns an instance of a different class.
--------------------------------------------------------

For example:

    class SomeClass(object):
      def generate_something(foo, bar):
        # likely some computation involving foo & bar here...
        # but, we're returning an instance of a totally different class.
        # This method should likely be split into 2 pieces, one living here,
        # and another piece in class something.
        return something(foo, bar)

Of course, there's always a time and a place for a factory method, but
in Python, these should actually be fairly few and far between.
