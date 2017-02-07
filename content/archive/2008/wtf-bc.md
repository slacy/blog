Title: WTF, bc?!
Date: 2008-07-31 12:02
Author: slacy
Category: General
Status: published

I was just poking around with the UNIX command 'bc' and found some very
odd behavior. Check out this session. (I've marked my input with a
"-&gt;")

> \# bc  
> bc 1.06  
> Copyright 1991-1994, 1997, 1998, 2000 Free Software Foundation, Inc.  
> This is free software with ABSOLUTELY NO WARRANTY.  
> For details type \`warranty'.  
> -&gt;F  
> 15  
> -&gt;G  
> (standard\_in) 2: illegal character: G  
> -&gt;F+F  
> 30  
> F\*F  
> 225  
> F0+F  
> 105  
> -&gt;F0  
> 90

So, can you figure out whats going on without reading the man page for
'bc'? I had to dig through it to find this gem:

> Input numbers may contain the characters 0-9 and A-F. (Note: They must
> be capitals. Lower case letters are variable names.) Single digit
> numbers always have the value of the digit regardless of the value of
> ibase. (i.e. A = 10.) For multi-digit numbers, bc changes all input
> digits greater or equal to ibase to the value of ibase-1. This makes
> the number FFF always be the largest 3 digit number of the input base.

Dude, thats some seriously fucked up input behavior there. Seriously,
WTF!!?
