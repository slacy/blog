Title: Programming challenge: Semi-sort a list of random numbers.
Date: 2012-10-05 15:44
Author: slacy
Category: General
Status: published

Here's a programming challenge / interview question that I like to think
about, and gives me that tingly feeling of "I think there's a really
clever, efficient algorithm for this" but I haven't been able to come up
with a really clever answer yet.  Here's the problem:

> Given a file containing N random positive integers less than N, write
> a program that runs on O(n) time and produces a collection of sorted
> files containing the input data, but where each file is itself in
> strictly sorted order.

Give it a try and send me the code and we can compare algorithms.  I've
been working with N=10000 and have a solution that produces about 200
unique sorted files, and can get as good as about 160 unique sorted
files if I allow a fixed constant sized space usage (i.e. a small
internal buffer).

I like to think of this operation as "semi-sorting".  The output is a
collection of sorted files, which can be merged together by a
traditional merge operation.
