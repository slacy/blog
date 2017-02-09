Title: gnuplot annoyance
Date: 2005-08-05 09:55
Author: slacy
Category: General
Status: published

From the gnuplot "help set terminal png" output:  
``  The size  is given in pixels---it defaults to 640x480.  The number of  pixels can be also modified by scaling with the `set size` command. [...] Examples: set terminal png font arial 14 size 800,600 ``

So, I type that into gnuplot, and I get:  
` gnuplot> set terminal png font arial 14 size 800,600 Terminal type set to 'png'                           ^          expecting: {small, medium, large},[no]transparent, or {monochrome, gray, color, [xRRGGBB] }`

From that usage statement, even though the gnuplot manual says that "set
terminal png..." supports setting a pixel size, its not actually
supported in the real code. What gives? It seems really silly to me to
be able to generate an image, but to not be able to set an absolute
pixel size. (yes, I know about "set size ...")

BTW, I'm using gnuplot-4.0.0-7
