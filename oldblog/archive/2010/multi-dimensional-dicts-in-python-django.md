Title: Multi-dimensional dicts in Python  Django?
Date: 2010-04-05 10:24
Author: slacy
Category: General
Tags: context, default, dict, django, python
Status: published

The code I'm working on frequently uses multi-dimensional dicts in
Python.  There is a bunch of code that seems to be always doing this:

    # a,b, and c have come from some external data source, QuerySet, etc. 
    a = 'axis_1'
    b = 'axis_2'
    c = 'axis_3'
    d = 'value'
    if a not in context:
      context[a] = {}
    if b not in context:
      context[a][b] = {}
    if c not in context:
      context[a][b][c] = value

Or some variant thereof. Is there a better pattern for multi-dimensional
(arbitrary) dicts in Python/Django? The setdefault() method doesn't have
the right semantics for this operation, and I'm not sure that it would
actually work right for multi-dimensional arrays anyway.
