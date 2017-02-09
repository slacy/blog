Title: Generating passwords that alternate hands
Date: 2008-11-20 15:29
Author: slacy
Category: General
Status: published

I wrote 2 script(s) that together will generate a set of 9 random
passwords that alternate hands on a Dvorak keyboard.  Modifying them for
QWERTY should be trivial.  Here they are:

    #!/bin/bash
    # Left hand:  12345pyaoeuiqjkx
    # Right hand: 67890fgcrldhtnsbmwvz
    LEFT="12345pyaoeuiqjkxPYAOEUIQJKX"
    RIGHT="67890fgcrldhtnsbmwvzGCRLDHTNSBMWVZ"
    for i in 1 2 3 4 5 6 7 8 9; do
    L=`/usr/bin/apg -n 1 -m 5 -x 5 -M NCL -t -a 1 -E $LEFT`
    R=`/usr/bin/apg -n 1 -m 5 -x 5 -M NCL -t -a 1 -E $RIGHT`
    ~/bin/zip.py $L $R
    done

And this is zip.py:

    #!/usr/bin/python
    import sys
    res=""
    for i in zip(sys.argv[1], sys.argv[2]):
      for j in i:
        res += j
    print res
