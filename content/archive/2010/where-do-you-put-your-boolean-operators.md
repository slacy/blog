Title: Where do you put your boolean operators?
Date: 2010-06-21 12:06
Author: slacy
Category: General
Status: published

When you have to insert a line break, do you put them like this:

    if (a > 3 && 
        b < 3) { 
      // body 
    } 

or do you put them like this:

    if (a < 3 
        && b > 3) { 
      // body 
    }

I find that in C++, I like doing in the first way, but that in Python, I
like doing it the second way. Weird.

In Python, it looks like this:

    if (a < 3 and 
        b > 3): 
      # body 

or

    if (a < 3 
        and b > 3): 
      # body 
