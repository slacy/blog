Title: What am I doing wrong?
Date: 2011-03-01 19:28
Author: slacy
Category: General
Status: published

You know, it's very obvious that some python modules are high quality,
and others are utter crap. Please tell me what I'm doing wrong:

    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Hello")

Produces no output on console. Oh? Maybe I need to specify a stream
handler? Tried that, with sys.stderr, and still nothing. Maybe I need to
set a file handler? Tried that.

Also, behavior is different in an interactive shell versus saved to a
file and invoked by commandline python. Jeebus I hate stuff like this.
