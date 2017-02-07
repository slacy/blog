Title: 10 things programmers need to stop saying.
Date: 2010-06-18 09:01
Author: slacy
Category: General
Status: published

### I made a new X, whose features are based on open source project Y, which of course you're familiar with.  But, we didn't use any of the existing code from Y, and we've added lots of special-purpose features, and we've eliminated the really bad stuff you don't like or use anyway.

This is usually done with very good intentions.  Open source projects
and libraries (memcached, mysql, dbm, malloc, filesystems, etc.) usually
have really great ideas, but difficulties arise when trying to integrate
them into an existing large system.  So, the developer has the "great
idea" to make a special-purpose version of something that's "not quite
like what's already out there".  There are tons of reasons why this is a
bad idea.  First, if it's not a Y, it's not a Y and you shouldn't call
it that.  For example, if you have a partial implementation of SQL, you
shouldn't call it SQL, (or TQL, UQL, VQL, WQL, etc.)  Either use the
existing code/packages, or don't, but don't try to emulate and
re-implement them.  You'll cause a whole host of headaches for both you
and your users.

### I know this way is a little more confusing, but it saves RAM and CPU.

This is usually a simple case of premature optimization.  Here's a
conversation I've had many times:

"I know this looks a little confusing, but it really saves a lot of
RAM."  
"That's interesting.  How many instances of this object are there in
your system?"  
"Ooooh, yeah, well, probably several thousand, maybe more!"  
"And you save how many bytes on each one?"  
"Up to 16!"  
"So, you made the code hard to read and debug so that you could save
about 16kB?"  
"Ummmmmmmm...."  
"Even if you instantiated a million of these, you would be saving
16MB."  
"Oh, yeah, well, it runs faster too!"

### My requirements are different than what's already provided, so I decided to implement another version of it.

Yeah.  You were too lazy to figure out the existing code, so you just
reimplemented the whole thing, introducing new bugs, duplicating code,
and you'll move on and forget to maintain this going forward too.

### I just wanted a few simple configuration parameters, so I wrote a parser and a new language for the config files.

Your own custom language is never the right answer.  XML would be ok.
Configuration in any other existing syntax is a always a better idea
than inventing your own language and parser.  Always.  When in doubt,
just use environment variables for configuration parameters, and make a
shell script that sets them before running your program.

### We needed to specify that in a machine-independent way, so we wrote our own structure definition language for ease of use.

Funny, byte-ordering and machine-dependencies used to be a pretty big
deal, like 20 years ago.  Now, virtually every machine you'll be talking
to is an Intel machine, and likely has the same binary representation of
pretty much everything.  What is this magical nonstandard machine you're
talking to?

### I think the right thing to do here is to auto-generate the code for these cases instead of writing them out by hand every time.

Ah, auto code generation, one of my favorites.  Makes code hard or
impossible to debug, vastly increases compile time, and gives you lots
of other things to debug and maintain (the code generation scripts
themselves.).  If you have this thought, you're probably approaching the
problem wrong.  For parameter passing, just use what your language
provides (varargs in C/C++, kwargs in Python, etc.) Less typing (for
your end users) isn't always a good thing.

### The network is way too slow, so I'm going to cache this on disk.

Really?  This shows a fundamental lack of understanding of both network
and disk performance.

### I decided not to use the version of this provided by the standard library because it didn't have the features I wanted.

Yeah, so your wrote your own.  Examples include date & time classes,
string classes, malloc and memory allocation in general, etc.

If you're so smart, and you can do such a great job at it, then why not
just fix the existing version instead of duplicating code and making an
api-alike version?

### The existing system is far too complex, so I just re-wrote a simple, less complicated version that meets just my needs.

"I didn't bother to read it."

### I'm doing it this way because you can't trust the values that are returned by this function.

Things that "can't be trusted" include date & time, memory allocation,
error codes (in general), etc.  If you can't trust your clock, then fix
your clock.  If you can't trust your allocator, then something's really
wrong.

Don't code for the exception case.  Assume it'll work, and when it
breaks, it'll do so catastrophically, instead of having some subtle and
hard to find & fix bugs.
