Title: On mkfifo and doing the impossible.
Date: 2008-12-26 12:27
Author: slacy
Category: General
Status: published

In my experiements to make a fast commandline parallel sorting script,
I've been using the unix command 'mkfifo' more than I ever had before,
and I've learned lots of interesting things about how the bash shell
handles pipes and redirects.

On the surface, using mkfifo looks a lot like using pipes, but more
verbose. For exmaple, instead of:

> \# sort foo | uniq -c | sort -k1n &gt; frequencies

you can say:

> \# mkfifo a b  
> \# sort foo &gt; a &  
> \# uniq -c a &gt; b &  
> \# sort -k1n b &gt; frequencies  
> \# rm a b

On first inspection, this looks just like the pipe example, except a
*lot* more verbose. Is there any use to this verbose syntax? In general,
for simple pipes, there is no reason to use FIFOs instead, and in some
cases FIFOs cause some issues that are not obvious. I'll talk about
those later.

So, the question then becomes...

When is mkfifo useful?
----------------------

mkfifo is useful when you want to do something that the pipe syntax is
too limited to express. Take the following example:

> \# sort -k1n inventory &gt; sorted.by.price  
> \# sort -k2n inventory &gt; sorted.by.sales

In the above example, we have an inventory file, and it has 2 numeric
fields (price and sales) and we want to produce 2 sorted outputs. If the
input file is very large, we may not wish to read it from disk twice.
How can we produce 2 output files without reading the file from disk
twice? Well, the answer lies in mkfifo:

> \# mkfifo a b  
> \# cat foo | tee -a a b &  
> \# sort -k1n a &gt; sorted.by.price  
> \# sort -k2n b &gt; sorted.by.sales

But wait, if you're following along in your shell, you'll realize that
the first sort just sits there, not doing anything, and not sorting.
Whats going on? This is where things get a bit complicated...

FIFOs are bufferless
--------------------

The issue in the above example exposes one of the biggest limitations of
FIFOs. They have absolutely no buffering in them whatsoever. The exact
bytes that you write() to one FIFO are then read() again by the other.
They're never copied, they're never buffered. So, why is that sometimes
a problem? Well, it means that you can't write() to a FIFO when someone
isn't already read()ing from it.

So, what happens is that the tee program takes a chunk of bytes, writes
it to fifo 'a', and blocks. When the 1st sort comes along, it read()s
the first few bytes from tee, and then sits there waiting for more. tee
has woken up and issued a write() to FIFO 'b', but there's no one
reading from 'b', so it just blocks, and it doesn't send any more data
to 'a'. To make this work, we have to run at least one of the sorts in
the background:

> \# cat inventory | tee -a a b *&*  
> \# sort -k1n a *&*  
> \# sort -k2n b *&*

Now, the tee is writing to the FIFOs, and the sorts are reading from
them, and everyone is happy. We can produce our outputs in less time
than the naive example that just runs 2 sorts in parallel.

What else are FIFOs useful for?
-------------------------------

As we saw above, FIFOs can help us do work in parallel, and they can
help us express things that can't be expressed in bash. Here's a great
example:

Imagine you have to compressed files, monday.gz and tuesday.gz. You want
to sort them together, into one single file, and compress the output,
but you don't have enough free disk space to store any of the files
uncompressed. How do you do this? A naive use would say:

> \# zcat monday.gz tuesday.gz | sort | gzip &gt; twodays.gz

But you'll notice that on machine with more than 1 CPU, that this
commandline only uses 1 CPU! Thats because the pipeline specifies a
single flow of data, so there's never a way to do 2 things in parallel.
Here's the parallelized fifo example:

> \# mkfifo a b  
> \# zcat monday.gz | sort &gt; a &  
> \# zcat tuesday.gz | sort &gt; b &  
> \# sort -m a b | gzip &gt; twodays.gz

This will produce identical output, but can do it in *significantly*
less time, since its unzipping and sorting in *parallel* on your
multi-core desktop. The last phase, the 'sort -m' is a special trick
used to merge the 2 sorted outputs. What if monday.gz and tuesday.gz are
already sorted? Thats easy:

> \# mkfifo a b  
> \# zcat monday.gz &gt; a  
> \# zcat tuesday.gz &gt; b  
> \# sort -m a b | gzip &gt; twodays.gz

This runs even faster, and does both unzipping and merging in parallel,
never creates a temporary file, and re-compresses on the fly. Sweet!

The holy grail
--------------

As I've mentioned in the past, the holy grail of shell scripting is a
simple non-compiled script built of nothing but standard unix tools,
that does what you want, but faster. For example, we could consider the
Wide Finder challenge a good example of something that could be
parallelized on multi-core machines using mkfifo and the interleave.py
script I've previously mentioned. All the Wide Finder guys want to do is
quickly process an Apache HTTP log and show the most popular URLs. I've
always done this with a combination of sort & uniq, so I'll show that
simple case here:

> \# cat access.log | awk '{print \$7}' | sort | uniq -c | sort -k1n |
> head -100

But, we can do this faster using interleaving and parallel sorting:

> \# mkfifo a b c d e f g h  
> \# cat access.log | interleave.py a b &  
> \# cat a | awk '{print \$7}' | sort &gt; c &  
> \# cat b | awk '{print \$7}' | sort &gt; d &  
> \# sort -m c d | uniq -c | interleave.py e f &  
> \# sort -k1n e &gt; g &  
> \# sort -k1n f &gt; h &  
> \# sort -m g h | head -100

***Author's Note:  This post ends here -- I found this old draft sitting
around in my WordPress, so I decided to just publish it as is, even
though its not actually done.  I thought it was still a good interesting
article on mkfifo.  So, there ya go.***
