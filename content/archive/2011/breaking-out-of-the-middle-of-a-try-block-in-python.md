Title: Breaking out of the middle of a try block in Python
Date: 2011-03-16 10:34
Author: slacy
Category: General
Tags: block, except, looping, python, try
Status: published

I had some code where I wanted to break out of a try block in Python.
The code looked something like this:

        try:
            print "First"
            if some_condition:
                # What do I put here to break out of the try block?
            print "Second"
        except Exception as e:
            if e:
                print "Exception"
        print "Last"

(If some\_condition is true, I want the output to print "First" and
"Last")

Neither break or continue works as expected, since "try" isn't a loop. I
could put the body of the try block in a function, and then at the "if
some\_condition" section, I could just return, but that seemed messy. I
never found a clean enough solution, but one possibility is this wonky
syntax:

    for _ in [True]:
        try:
            print "First"
            if some_condition:
                # Now, since we're in a loop, we can break out of it. 
                break
            print "Second"
        except Exception as e:
            if e:
                print "Exception"
                print type(e)

    print "Last"

But, it's kind of ugly, and not clear what's going on, so I decided not
to do it that way.

I'm really surprised that there isn't a standard syntax for this.
Something like "raise" but that isn't an exception. I guess I could
raise a special value and handle it specially in th except block, but
that seems messy as well.
