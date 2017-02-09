Title: Upgrading Slimserver to 5.4 broke my Squeezebox (and then I fixed it)
Date: 2005-04-22 07:00
Author: slacy
Category: Linux Stuff
Status: published

![](http://slacy.com/blog/images/slim-svea.png)

Just in case anyone else has this problem, here's the deal:

If you're running Sveasoft's firmware on your Linksys WRT54G router, and
you upgrade to the latest version of the SlimServer from
slimdevices.com, your Squeezebox may stop working.  The problem is that
for some reason, the squeezebox and the slim server seem to all think
their IP addresses are 192.168.1.1 (the IP of the router itself).  This
was being caused by the setting "loopback" under the Administration
tab.  When I turned that off, it worked fine.  That said, I have no idea
why I had turned on Loopback in the first place.  Maybe it was the
default?  
  

