Title: Set operations (intersection, union, difference) in bash
Date: 2008-09-11 10:21
Author: slacy
Category: General
Status: published

[This post has a great description of how to do set operations on files
in bash.](http://wordaligned.org/articles/shell-script-sets)

The thing left out is how to do set operations on variable values in
bash.  The trick is to use FIFOs, which is a surprisngly common theme in
my bash usage these days.  Here's something I was just working on:

> ALL\_DIRS=\`find . -type d\`
>
> EMPTY\_DIRS=\`find . -type d -empty\`

So, how about the non-empty directories?  That would be:

> TEMP\_A=\`mktemp -u\`  
> mkfifo \$TEMP\_A  
> TEMP\_B=\`mktemp -u\`  
> mkfifo \$TEMP\_B
>
> function clean\_up {  
> rm -f \$TEMP\_A \$TEMP\_B  
> exit 1  
> }
>
> trap clean\_up SIGHUP SIGINT SIGTERM
>
> DIRS=\`find . -type d\`
>
> EMPTY\_DIRS=\`find . -type d -empty\`
>
> echo \$DIRS | fmt -1 | sort &gt; \$TEMP\_A &
>
> echo \$EMPTY\_DIRS | fmt -1 | sort &gt; \$TEMP\_B &
>
> NON\_EMPTY\_DIRS=\`comm -23 \$TEMP\_A \$TEMP\_B\`
>
> clean\_up

Voila!

NB: I could have just used a temp file here instead of a temporary FIFO,
but this way is so much cooler!

NB2: I had never used the UNIX command 'comm' before.  "man comm" for
more details.
