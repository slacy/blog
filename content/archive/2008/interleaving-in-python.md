Title: Interleaving in Python
Date: 2008-06-12 21:30
Author: slacy
Category: General
Status: published

Just in case you were wondering... The interleaver that I posted below
can be easily implemented in Python. The result looks like this:

    #!/usr/bin/python
    import sys
    outputs = []
    numargs = 0
    for arg in sys.argv[1:]:
      outputs.append(open(arg, 'a'))
      numargs += 1

    s = "empty"
    counter = 0
    while s:
      s = sys.stdin.readlines( 4096 * 8 )
      outputs[counter % numargs].writelines(s)
      counter += 1

But, its signicantly slower than the native C version. The C version can
do about 1GB in 3 seconds. The Python version takes 24s to do the same
thing. (8 times slower).

Granted, I didn't try very hard to optimize the Python (yet!)
