Title: Tips for setting up virtualenv?
Date: 2010-07-06 20:27
Author: slacy
Category: General
Status: published

I'm reading up on the Python virtualenv library, mostly for converting
my application's dependencies from system-wide to local.  My plan is to
put the virtualenv under source control (git) and distribute it to
several machines, running various flavors of UNIX.  Mainly, OSX 10.6.x,
Ubuntu 8.04.4 and Ubuntu 10.04.

I've got some questions that aren't really covered by the virtualenv
docs or blog posts that I've been reading thus far:

1.  Virtualenv clearly states that it won't make packages
    cross-platform, but I'd love to hear from people with experiences
    managing and moving env's from Mac to Linux.  Does this work in
    practice (assuming the packages don't have binary components).  If
    they **do** have binary components, (i.e. MySQLdb) what's the best
    way to manage these?  One env for each platform?  This feels
    laborious, and the effort involved in keeping them in sync might
    be substantial.
2.  Virtualenv docs also make it very clear that they can't be
    relocated (i.e. moved to another directory on the same or similar
    machine), although there is the --relocatable flag, but google
    searches have shown people have only moderate success with using it.
       So, do you put your virtualenv's in a global directory, like
    "/var/env" or something like that? (A path that can be the same
    across all UNIX platforms?)  Any good ideas for virtualenv paths
    would be appreciated.

And, any other thoughts/experiences and best practices on using
virtualenv for this kind of use would be greatly appreciated!
