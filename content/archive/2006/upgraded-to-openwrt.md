Title: Upgraded to OpenWRT
Date: 2006-07-22 17:51
Author: slacy
Category: Linux Stuff, Web
Status: published

Today (its hot!) my wife was complaining that she can't access our
internal website(s) from her internal computer. The problem is that the
external DNS resolution results in an external IP address, which routes
back inside our net, which the Sveasoft router just couldn't handle.

I had manually "fixed" this problem by editing my /etc/hosts, but doing
that for every computer in the house is a real pain.

Solution? Upgrade to [OpenWRT](http://openwrt.org)! Installation was
straightforward, although the documentation is a little lacking on the
web interface. Thankfully, everything is pretty straightforward.

After the install was complete, the OpenWRT firmware lets you put in
"manual" hostnames that end up in /etc/hosts on the router. I did that
for all my internal sites, and then changed all our computers to use the
router for a DNS server, and everything is up and running great!

I'm a lot happier with OpenWRT than the silly Sveasoft firmware that I
was running before. I briefly considered DD-WRT, but that guy looks like
he's going down the road of Sveasoft, and looking for funding. OpenWRT
never will need that.
