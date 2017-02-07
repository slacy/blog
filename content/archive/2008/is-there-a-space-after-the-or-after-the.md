Title: Is there a space after the *, or after the &?
Date: 2008-01-11 20:40
Author: slacy
Category: General
Tags: c++, declarations, pointers, style, types
Status: published

No, there is not a space after the \*. Take a look at this example:

    value = *pointer; 

Note how there's not a space after the asterisk. Also note how the type
of "value" and the type of "\*pointer" are the same.

Thus, when you declare these variables, you should do it like this:

    Type value;
    Type *pointer;

    value = *pointer; 

Why would you ever want to put the asterisk next to the type name? Why
would that **ever** make sense? I just don't get it!
