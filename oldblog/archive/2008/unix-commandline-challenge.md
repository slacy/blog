Title: Unix commandline challenge
Date: 2008-06-10 23:08
Author: slacy
Category: General
Status: published

I've been spending a lot of my time at work sorting and grepping through
large multi-GB files, and have been amazed that the standard UNIX sort
and grep commands don't have support for SMP machines.

I decided that it should be fairly straightforward to come up with a
commandline that can use 2 or more CPUs to do a sort or grep of a single
file. But, I haven't yet been able to come up with a simple command line
to do this!

So I'll propose a challenge: Come up with a script (python, perl, bash,
etc.) or simple command line that can use 2 or more CPUs to process
(grep or sort) a single file in less time than the naive invocation of
the same command.

The input that I'm using for testing is about 5.2 million lines long,
and takes up about 60MB. Each line is made up of between 0 and 20 random
uppercase letters.[Here's a perl script that will generate a file full
of random words just like
this.](http://slacy.com/blog/wp-content/randwords.pl) Just run something
like "./randwords.pl | head -500m &gt; randwords"

Here are some of the approaches that I've tried thus far:

The awk co-processor approach
-----------------------------

gawk has support for what it calls "co-processors" which I would call
"pipes to child processes". It seems like a great feature. The way that
this works is that you can 'print' records to a piped co-processor and
use more than one in parallel to do your work. Here's an example
commandline:

> \# cat randwords | awk '{if (NR % 2 == 1)  
> { print \$0 | "egrep -i steve"} else {print \$0 | "egrep -i steve" }}'

You can imagine wrapping this up in a containing script to simplify its
usage. Upon running this script, you might notice that there aren't
actually 2 grep processes running. This is because awk is being too
smart and realizes that you're forking of the 'same' process to do work.
So, adding some dorky commandline switches to make them look different
is what you want:

> \# cat randwords | awk '{if (NR % 2 == 1)  
> { print \$0 | "egrep -i steve"} else {print \$0 | "egrep -a -i steve"
> }}'

The "-a" option means "process input as text" (duh!) which should have
no effect on the output, but after adding that flag, we can now see that
awk fires up 2 grep processes that run in parallel.

So, how did it perform? Well, awk takes up \~60% of the CPU, with about
18% being given to each grep process. So, its almost 100% of a single
core to do the work. Here's how the timings look:

> time cat smallrand | awk '{if (NR % 2 == 1) { print \$0 | "egrep -i
> steve"} else {print \$0 | "egrep -a -i steve" }}'  
> TPHOBQSTEVEOGIK  
> PHCYZMSTEVEDYZFF  
> USTEVENPP
>
> real 0m45.069s  
> user 0m18.545s  
> sys 0m25.793s
>
> \# time cat randwords | egrep -i steve  
> TPHOBQSTEVEOGIK  
> PHCYZMSTEVEDYZFF  
> USTEVENPP
>
> real 0m0.372s  
> user 0m0.165s  
> sys 0m0.166s

So, the awk solution is running more than 10 times slower than the
native grep. NEXT!

The perl "sharding" script
--------------------------

One could imagine that all you need to do to solve this problem is to
take alternating lines of the input text and shove them down the stdin
of 2 child processes. Seems easy, right? So, lets whip up a perl script
that does just that: (shortened for display here)

> \#!/usr/bin/perl  
> \$num = \$\#ARGV + 1;  
> for (\$i = 0; \$i &lt; \$num; \$i++) { open( \$files\[\$i\],
> "\$ARGV\[\$i\]") || die; }  
> \$line = 0;  
> while (<stdin>) { print { \$files\[\$line++ % \$num\] } \$\_; }  
> for (\$i = 0; \$i &lt; \$num; \$i++) { close \$files\[\$i\]; }

Seems like a good idea, right? We can even use perl's super funky "open"
syntax to fork of the child processes. Assuming that this is stored as
"shard.pl" we can invoke it like this:

> \# cat randomwords | ./shard.pl "| egrep -i steve" "|egrep -i steve"

How does this compare to the native grep?

> \# time cat randwords | ./shard.pl "|egrep -i steve" "|egrep -i
> steve"  
> TPHOBQSTEVEOGIK  
> PHCYZMSTEVEDYZFF  
> USTEVENPP
>
> real 0m6.625s  
> user 0m6.335s  
> sys 0m0.251s

So, its only about 20 times slower than the native grep. I guess we're
making progress? The script can actually be "optimized" to run in about
4 seconds, if you buffer up a few lines of input before calling 'print'.
I suspect that a few more gains of that nature can be had, but I don't
expect them to be huge.

The divide and conquer approach
-------------------------------

So, how about just splitting the file in half and then grepping the 2
sides in parallel? Well, to be fair, we're looking for a *script* to
solve this problem, so we'll need to write a 'split in half' script, and
go from there. Lets just see if its even remotely possible:

> \# wc -l randwords  
> 5242880 randwords  
> \# time (head -2621440 randwords &gt; top ; tail -2621440 randwords
> &gt; bottom ; echo top bottom | xargs -n1 -P2 egrep -i steve)  
> TPHOBQSTEVEOGIK  
> PHCYZMSTEVEDYZFF  
> USTEVENPP
>
> real 0m1.235s  
> user 0m0.514s  
> sys 0m0.728s

So, we're using 2x the disk space, and we're only taking about 6 times
longer than native grep. Maybe we can remove those temp files and speed
things up, like this:

> \# time (head -2621440 randwords | egrep -i steve & tail -2621440
> randwords | egrep -i steve)  
> TPHOBQSTEVEOGIK  
> PHCYZMSTEVEDYZFF  
> USTEVENPP
>
> real 0m0.446s  
> user 0m0.556s  
> sys 0m0.204s  
> \# time egrep -i steve randwords  
> TPHOBQSTEVEOGIK  
> PHCYZMSTEVEDYZFF  
> USTEVENPP
>
> real 0m0.209s  
> user 0m0.152s  
> sys 0m0.055s

Thats more like it! Now we're only running in 2x the time of the native
grep! Whopee! Unfortunately, a true 'script' of this sort would have to
include the time to count the lines, so we may as well add that in our
runtime too:

> \# time wc -l randwords  
> 5242880 randwords
>
> real 0m0.537s  
> user 0m0.432s  
> sys 0m0.062s

Which (surprisingly) takes about 3 times longer than the grep itself, so
thats never gonna really work out, is it?

Any other bright ideas?

</blockquote>

