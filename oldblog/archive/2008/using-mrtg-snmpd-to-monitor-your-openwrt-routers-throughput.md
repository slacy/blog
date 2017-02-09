Title: Using mrtg & snmpd to monitor your OpenWRT router's throughput
Date: 2008-01-17 16:40
Author: admin
Category: General
Tags: ADSL, bandwidth graph, fedora, linux, mrtg, openwrt, router, snmpd
Status: published

I've looked around on the web for a while for easy instructions about
how to setup an mrtg installation to monitor my OpenWRT router's
throughput. Here are my easy instructions for getting this setup up and
running:

Note: At first, I didn't realize that mrtg would run on a remote
machine. I didn't try getting mrtg to run locally on the OpenWRT system,
although this is theoretically possible. I use a secondary machine to
pull data from the router.

1\. Install smtpd on the OpenWRT router. This is as easy as:

> \# ipkg install snmpd

Once the install has completed, you need to start up snmpd. I just did
this by hand, since my router has a pretty good uptime, and I was
messing around. To start it by hand, say:

> \# /etc/init.d/snmpd start

If you want it to start automatically, then you should rename
/etc/init.d/snmpd to something like /etc/init.d/S98snmpd.

2\. Install mrtg on your linux box. My main webserver is a Fedora box, so
this was as straightforward as:

> \# yum install mrtg

3\. Configure mrtg using "cfgmaker". mrtg comes with a default config,
but since router setups vary so much, this default config is pretty much
useless. So, I ran:

> \# cfgmaker --ifref=name public@192.168.1.1 &gt; /etc/mrtg/mrtg.cfg

This created a reasonable config file with a bunch of sections (one
section for each interface on the router). It needed a small tweak, and
that was to define the WorkDir directory to the right place for Fedora,
which is /var/www/mrtg. I then uncommented the bulk of the config
sections in the rest of the file.

4\. Manually run the mrtg collection scripts to bootstrap the system. You
can skip this step if you want to just wait 5 minutes. I looked in
/etc/cron.d/mrtg and just ran the command there, which was:

> LANG=C LC\_ALL=C /usr/bin/mrtg /etc/mrtg/mrtg.cfg --lock-file
> /var/lock/mrtg/mrtg\_l --confcache-file /var/lib/mrtg/mrtg.ok

I can this a couple of times until no error messages came out (the first
2 times may produce errors).

5\. Alias /mrtg to /var/www/mrtg in your apache configuration file. This
was necessary for me because I have a bunch of virtual hosts. People
without virtual hosts can skip this step.

6\. Create a simple /var/www/mrtg/index.html that links to the pages
generated my mrtg. There's one page per router interface, so I just made
a bunch of hardcoded links. You can look in /var/www/mrtg to see what
the filenames are.

6\. Done! Now you can view my router graphs on
[slacy.com/mrtg](http://slacy.com/mrtg). The interesting ones are:

[eth1](http://slacy.com/mrtg/192.168.1.1_3.html): Shows all traffic on
my wireless network.  
  
[vlan1](http://slacy.com/mrtg/192.168.1.1_6.html): Shows all traffic on
my external WAN port (in/out to the 'real world')  
  
Also note that I've configured them all to have logscale on the Y axis,
since my ADSL line has such a discrepancy between input and output
rates.

I haven't exactly figured out what the rest of the interfaces are, but I
can tell that vlan0 and vlan1 are inverse of each other.

![](http://slacy.com/mrtg/192.168.1.1_6-day.png)
