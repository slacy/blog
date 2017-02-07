Title: strchr() Considered Harmful
Date: 2007-01-30 18:25
Author: slacy
Category: Linux Stuff
Status: published

You tell me whats wrong with the following, which is the standard
definition of the strchr() function:

> char \*strchr(const char \*s, int c);

Give up? Well, think about this code:

> void FunctionThatDoesntExpectItsArgumentsToChange(const char
> \*input\_string) {  
> char \*unconst = strchr(input\_string, input\_string\[0\]);  
> strcpy(unconst,"You've been pwned");  
> }

Do you know what just happened there? The compiler let me write on top
of a const string, without ever having a cast from const to non-const!
Take a look at all the string functions that have this hideous syntax:

strchr, strrchr, strchrnul, strpbrk, strstr.

I mean, what a huge list of suspects! This has got to be one of the
biggest holes I've ever seen. What a mess. I've lost all faith in the
designers of the standard C library. What a bunch of bozos.
