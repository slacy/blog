Title: How to parallelize anything using xargs  bash
Date: 2008-06-06 14:47
Author: slacy
Category: General
Status: published

So, you've got a bunch of commands that you want to parallelize. For
example, imagine if you had a bunch of things like this:

> zcat file-01.txt.gz | sort | uniq -c | gzip &gt;
> file-01.sorted.txt.gz  
> zcat file-02.txt.gz | sort | uniq -c | gzip &gt;
> file-02.sorted.txt.gz  
> \[...\]

(NB: that could have been generated and stored in a file or directly on
the commandline using the 'for' builtin).

So, imagine there are 100 lines of that junk, and you've got a quad core
computer, so you want to run 4 at a time. How would you do it?

Well, assuming the commands are all in a file called "cmd.txt" you can
run:

> \# cat cmd.txt | xargs -d "\\n" -n1 -P4 bash -c

Which will spawn 4 bash processes at a time (-P4), and each one will get
one line from the input (-n1 and -d "\\n") and pass that to "bash -c"
which will execute it.

Voila. Instead of just doing one command at a time, you're now doing 4,
and it runs in a quarter the time!
