Title: A fast(er) Python interleaver, and a simple parallel sorting script.
Date: 2008-07-10 12:43
Author: slacy
Category: General
Status: published

Take a look at this short python script:

    #!/usr/bin/python

    from sys import stdin, argv

    outputs = []
    numargs = 0
    for arg in argv[1:]:
      outputs.append(open(arg, 'a'))
      numargs += 1

    s = "str"
    counter = 0
    p = 0
    while len(s) > 0:
      s = stdin.read(32 * 1024)
      p = s.rfind('\n') + 1
      if p > 0:
        outputs[counter % numargs].write(s[:p])
        counter += 1
        outputs[counter % numargs].write(s[p:])
      else:
        outputs[counter % numargs].write(s)
        counter += 1

It does the file interleaving task that I've talked about previously,
and does it reasonably fast. Its a reasonable replacement for the C++
version, and can rip through a \~600MB file in about 0.75s.

I've been playing with a simple wrapper script for executing parallel
sorts, like this:

    #!/bin/bash
    rm     a b c d e f g h i j
    mkfifo a b c d e f g h i j

    cat $1 | interleave.py a b c d &

    sort -S 25% a -o e &
    sort -S 25% b -o f &
    sort -S 25% c -o g &
    sort -S 25% d -o h &

    sort -m e f -o i &
    sort -m g h -o j &
    sort -m i j

Which does a 4-way parallel sort, and then a 3-way parallel merge of the
resultant sorted data. (Yes, doing a parallel merge actually makes
things a little faster). It uses unix FIFOs instead of keeping the
temporary files on disk, which saves a lot of I/O of writing and reading
the temporary files.

This code can sort a \~600MB file in 25.1s, whereas a vanilla unix
'sort' command on the same data takes 34.7s, so I've got a speedup of
about 35%. That's pretty good, when you think that the maximum possible
speedup is 50%.
