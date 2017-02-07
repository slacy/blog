Title: Python Multi-dimensional dicts using defaultdict
Date: 2010-05-12 12:54
Author: slacy
Category: General
Tags: defaultdict, dict, python
Status: published

I asked previously how to avoid code like this:

    # Implement d[3][4] = 5
    if not 3 in d:
      d[3] = {}
    d[3][4] = 5

I found the answer, and it lies in
[collections.defaultdict](http://docs.python.org/dev/library/collections.html#defaultdict-objects).
defaultdict is just like dict, except that you pre-specify an initial
default values for items that aren't present. For example:

    d = defaultdict(lambda: 1)
    d[5] += 3
    print d

Will print out "{5: 4}" and I didn't have to explicitly assign d\[5\] to
1 before doing the increment.

This leads to the question: Can you create a defaultdict whose default
is another defaultdict? Yes!

    d = defaultdict(defaultdict)
    d[3][4] = 5

Is totally valid. But, that inner defaultdict doesn't have a good
default value, so if you want more dimensions, you have to start
stacking them up, like this:

    d = defaultdict(lambda: defaultdict(defaultdict))
    d[3][4][5] = 6

And so on, as you want more dimensions. Not a huge price to pay, I
guess.
