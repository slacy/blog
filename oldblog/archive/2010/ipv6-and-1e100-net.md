Title: ipv6 and 1e100.net
Date: 2010-02-10 16:46
Author: slacy
Category: General
Tags: 1e100, ipv6, reverse dns
Status: published

I saw this [weird article about
1e100.net](http://www.seroundtable.com/archives/021639.html) the other
day, and I was just poking around and realized how google.com traffic is
getting tracked as 1e100.net

It's via ipv6. Check this out:

    $ host ipv6.google.com
    ipv6.google.com is an alias for ipv6.l.google.com.
    ipv6.l.google.com has IPv6 address 2001:4860:b006::63
    ipv6.l.google.com has IPv6 address 2001:4860:b006::6a
    ipv6.l.google.com has IPv6 address 2001:4860:b006::69
    ipv6.l.google.com has IPv6 address 2001:4860:b006::68
    ipv6.l.google.com has IPv6 address 2001:4860:b006::67
    ipv6.l.google.com has IPv6 address 2001:4860:b006::93
    $ host 2001:4860:b006::63
    7.6.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.6.0.0.b.0.6.8.4.1.0.0.2.ip6.arpa domain name pointer pv-in-x67.1e100.net.

So, if you're on an IPv6 enabled connection (as maybe some corporations
are, and then they NAT to IPv4 or something) anyway, if you hit
ipv6.google.com, then someone will see traffic to the IPv6 addrs listed
above, whose reverse-DNS points back at 1e100.net instead of back at
google.com.

I'm guessing that this is really just because of legitimate IPv6 users
hitting ipv6.google.com.
