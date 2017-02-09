Title: Holy crap locales!
Date: 2012-12-14 15:01
Author: slacy
Category: General
Status: published

Here's something fun to try.  Create a text file that looks like this
(Note: utf-8 encoded!):

    A
    ß
    C
    ßa
    ßz
    a
    B
    b
    c
    S
    s
    SS
    ss
    SA
    sa
    SZ
    sz

Just to be really clear, here are the exact bytes I'm talking about:

    $ hexdump -C  /tmp/foo.txt 
    00000000  41 0a c3 9f 0a 43 0a c3  9f 61 0a c3 9f 7a 0a 61  |A....C...a...z.a|
    00000010  0a 42 0a 62 0a 63 0a 53  0a 73 0a 53 53 0a 73 73  |.B.b.c.S.s.SS.ss|
    00000020  0a 53 41 0a 73 61 0a 53  5a 0a 73 7a 0a           |.SA.sa.SZ.sz.|
    0000002d
    $ md5sum /tmp/foo.txt
    ac2be5e453dd79c070da74d0e67aa6b2 /tmp/foo.txt

Now, compare the output of the following commands:

    $ sort /tmp/foo.txt
    $ LC_ALL='en_US' sort /tmp/foo.txt
    $ LC_ALL='en_US.utf8' sort /tmp/foo.txt
    $ LC_ALL='en_US.iso88591' sort /tmp/foo.txt
    $ LC_ALL='C' sort /tmp/foo.txt
    $ LC_ALL='de_DE.utf8' sort /tmp/foo.txt

How's that for rocking your world? So, the next time your friend says
"hey, can you return those results sorted for me?" then you'll have
something really fun to think about when you can't sleep at night.

And just when you thought "Oh, well great, at least all the UTF-8
versions sort the same" then comes along this little gem:

    $ LC_ALL="jp_JP.utf8" sort /tmp/foo.txt

Oh, and just when you thought "Well, I guess I'll be OK with en\_US.utf8
and at least English will sort the way I want worldwide!" then along
comes your friends to the North with this awesome zinger:

    $ LC_ALL="en_CA.utf8" sort /tmp/foo./txt
