Title: Using xargs to parallelize just about anything.
Date: 2006-03-19 17:47
Author: slacy
Category: Linux Stuff
Status: published

The unix command "xargs" has a really cool argument that can be used to
parallelize just about any batch process that you can think of running.
The manual page describes this:

    --max-procs=max-procs, -P max-procs
    Run  up  to  max-procs processes at a time; the default is 1.  If max-procs is 0, xargs
    will run as many processes as possible at a time.  Use the -n option with -P; otherwise
    chances are that only one exec will be done.

So, by using that argument, we can run something that would usually be
serial, but run it in a parallel manner. For example, imagine that you
have a script that rotates an image, and you have 1000 images you want
to rotate, and you have multiple CPUs to work with (dual core,
hyperthreading, etc).

I used to always run a command like this:

    for file in *.jpg; do
    ./rotate $file
    done

or, more succintly:

    find . -iname "*.jpg" | xargs -n1 ./rotate

But, by adding just one simple addition, of "-P2" to the xargs command,
xargs will manage to keep 2 processes running at all times, and
amazingly, it coalesces the stdout and stderr's of the 2 different
processes into one stream, so you can then pipe and process that output.

For example, I was recently grepping through a bunch of files:

find . -iname "\*.html" | xargs -n10 -P2 fgrep --mmap -m 1 -i "

So, we've got a single threaded instance of find, piped to xargs
managing 2 grep processes, which then combines their stdout's, which
then gets piped to awk. Its really really cool, and is a huge timesaver.

Unfortunately, everything is disk-bound now. :)
