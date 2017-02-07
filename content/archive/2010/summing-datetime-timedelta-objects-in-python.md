Title: summing datetime.timedelta objects in Python
Date: 2010-02-09 16:19
Author: slacy
Category: General
Tags: datetime, python, summation
Status: published

Argh! The following snippet is totally broken:

    import datetime 

    times = [datetime.timedelta(hours=1), datetime.timedelta(minutes=30)]
    print sum(times)
    print min(times)
    print max(times)

It raises "TypeError: unsupported operand type(s) for +: 'int' and
'datetime.timedelta'"

The thing is, I want this function to be able to sum both a list of
floats, integers, or timedelta objects.  Other than doing a bunch of
type checking, or writing my own sum method, is there some easy way to
do this that I'm missing? I guess I could write:

    print datetime.timedelta(milliseconds=sum([d.milliseconds for d in times]))

Yuk.  That's not really type safe either, since I'd have to check the
type of times\[0\] before I started.
