Title: parallel sorting in bash, revisited
Date: 2008-08-25 13:48
Author: slacy
Category: General
Status: published

After a brief conversation and thought today, I realized that my
previous efforts on parallel sorting on the bash commandline may have
fallen a bit short of their potential.

So, I started to craft a new implementation. This one would emulated a
parallel qsort algorithm, but using python, bash, and the standard UNIX
sort command.

The basis behind this design is that you can eliminate the final merging
step if you first 'pivot' the input file into pieces that don't overlap.
(I'm using qsorts 'pivot' term here). So, I wrote a short pivot program
in python:

` #!/usr/bin/python2.4 from sys import stdin, argv outputs = [] numargs = 0 buffer_size = 1024 * 64 for arg in argv[1:]: outputs.append(open(arg, 'a')) numargs += 1 pivot = stdin.readline(buffer_size) outputs[0].write(pivot) s = "empty" while s: s = stdin.readlines(buffer_size) for line in s: if line <= pivot: outputs[0].write(line) else: outputs[1].write(line)`

So, with that, one can 'pivot' an input file into 2 pieces that are
known to not overlap, sort them independently, and then just
**catenate** the final outputs together.  No post-merging is necessary,
and the pivot step is actually easier than merging (!).

So, here's an extremely simplified parallel sorting driver script, using
the 'pivot.py' quoted above:

` #!/bin/bash mkfifo a b c d cat $1 | pivot.py a b & sort a -o c & sort b -o d & cat c d`

And, I compared a script like this with the vanilla 'sort' UNIX sort
command on a file of 58 million random character strings.  This new
pivot-based sorter was 50% faster than the vanilla sort, completing the
task in 2 minutes, compared with 3 minutes for sort.

Of course, with any qsort implementation, choosing a good pivot is
important, and this algorithm greatly suffers from poor pivot choices
(which are derived from the first line in the file).
