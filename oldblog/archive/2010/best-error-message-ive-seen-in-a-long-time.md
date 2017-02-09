Title: Best error message I've seen in a long time.
Date: 2010-07-28 08:41
Author: slacy
Category: General
Status: published

This came from a Gnome-enabled program on by Ubuntu 10.04 system.  It
pretty much sums up what's wrong with "Linux on the desktop"

> <span
> style="font-family: Georgia, 'Bitstream Charter', serif; color: #444444;"><span
> style="line-height: 22px;">Error setting value: No database available
> to save your configuration: Unable to store a value at key
> '/desktop/gnome/url-handlers/unknown/command', as the configuration
> server has no writable databases. There are some common causes of this
> problem: 1) your configuration path file /etc/gconf/2/path doesn't
> contain any databases or wasn't found 2) somehow we mistakenly created
> two gconfd processes 3) your operating system is misconfigured so NFS
> file locking doesn't work in your home directory or 4) your NFS client
> machine crashed and didn't properly notify the server on reboot that
> file locks should be dropped. If you have two gconfd processes (or had
> two at the time the second was launched), logging out, killing all
> copies of gconfd, and logging back in may help. If you have stale
> locks, remove \~/.gconf\*/\*lock. Perhaps the problem is that you
> attempted to use GConf from two machines at once, and ORBit still has
> its default configuration that prevents remote CORBA connections - put
> "ORBIIOPIPv4=1" in /etc/orbitrc. As always, check the user.\* syslog
> for details on problems gconfd encountered. There can only be one
> gconfd per home directory, and it must own a lockfile in \~/.gconfd
> and also lockfiles in individual storage locations such as
> \~/.gconf</span></span>
