Title: 30 second tutorial for ipython, pylab, numpy and matplotlib
Date: 2008-01-30 21:24
Author: slacy
Category: General
Tags: gnuplot, ipython, matplotlib, numpy, pylab
Status: published

[ipython](http://ipython.scipy.org/moin/) &
[pylab](http://matplotlib.sourceforge.net/pylab_commands.html),
especially when you include [numpy](http://numpy.scipy.org/) and
[matplotlib](http://matplotlib.sourceforge.net), make a fantastic
replacement for [gnuplot](http://www.gnuplot.info/). Imagine if you had
the plotting capabilities of [Mathematica](http://www.wolfram.com), but
the ease of use of [Python](http://www.python.org/). Thats what this
combo gives you.

First, you need to install all the right bits. I've got links above, and
each link should have a good install tutorial. For linux distributions,
this is particularly easy. Just use yum or apt-get.

Start off by running the interactive ipython shell in pylab mode:

> \# ipython -pylab

Then, once you're there, lets do a simple plot:

> &gt;&gt; your\_data = load("./datafile")  
> &gt;&gt; plot(your\_data);  
> &gt;&gt; legend()

The file 'datafile' could look something like this:

> 1 2 3  
> 2 3 4  
> 3 2 3  
> 4 1 2  
> 5 0 1  
> 6 1 0  
> 7 2 1  
> 8 3 2  
> 9 2 3

The plot() function will pop up a window that looks like this:  
![](http://slacy.com/blog/wp-content/matplotlib.png)

Pretty easy, huh?

The great part about this combination is the number of other
transformations that you can do on the data. So, any sort of other data
analysis that you'd like to do (sorting, contour, histogramming, etc.)
is all built in to either matplotlib, numpy, or pylab. Excellent!
