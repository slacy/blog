Title: Wow, fabric for Python is pretty cool.
Date: 2010-07-06 20:14
Author: slacy
Category: General
Status: published

Today I played with the awesome [fabric](http://fabfile.org) library for
Python.

In short, it's a nice convenient layer around issuing remote ssh
commands, for things like starting and stopping remote servers, or even
copying files from the local machine to a remote machine.  I made a
simple script that goes out to my production web server, issues a "git
pull" to get the latest source, and then does an "apache2 force-reload"
to pull in the new configs & data.  It was really really easy.

This is why I love Python.
