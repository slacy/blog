Title: Getting firefox, thunderbird, liferea, etc. to have
Date: 2005-04-22 07:00
Author: slacy
Category: Linux Stuff
Status: published

Okay, so I downloaded the latest Firefox and Thunderbird, and they did
something that broke the "clickability" of links across these
applications (again!)

After reading the bug:
[246168](http://bugzilla.mozilla.org/show_bug.cgi?id=246168) at
mozilla.org, I realized that there was a new parameter that needs to be
passed to the "firefox -remote" command.

Anyway, the result is that you should say this:

firefox -a firefox -remote "openURL(%s)"

You can change that setting in liferea, and in your "Preferred
Applications" gnome or kde setting. But for some reason, Clicking on
links in thunderbird still goes to hoovers.com. I don't really
understand why. Its as if Gnome isn't turning the "%s" into the name of
the site that you're supposed to be going to. Man, this sort of sucks.  
  

