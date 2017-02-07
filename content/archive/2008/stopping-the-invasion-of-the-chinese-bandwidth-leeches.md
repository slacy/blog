Title: (stopping the) Invasion of the Chinese Bandwidth Leeches.
Date: 2008-01-26 10:25
Author: slacy
Category: General
Tags: bandwidth, chinese, connections, crawlers, leeches, mrtg, openwrt, robots.txt
Status: published

Ever since I [setup mrtg on my OpenWRT
router](http://slacy.com/blog/index.php/2008/01/17/using-mrtg-snmpd-to-monitor-your-openwrt-routers-throughput/),
I've been noticing that between 2pm and 8pm PST, there's a huge spike in
my outgoing bandwidth. I've been trying to track it down, and briefly
suspected it was my TiVoHD 'phoning home' and sending back megs and megs
of clickstream logs (but I don't watch that much, I swear!).

Yesterday, I did some more deeper digging, and with the help of some
freinds, got some good debugging information. So, here goes:

1\. To show the list of all open connections on your OpenWRT router, just
cat /proc/net/ip\_conntrack. Here's an example that shows everything
thats going on in my network right now:

> \# cat /proc/net/ip\_conntrack | grep -i ESTAB  
> tcp 6 86216 ESTABLISHED src=192.168.1.6 dst=64.81.79.70 sport=53336
> dport=80 src=64.81.79.70 dst=64.81.240.181 sport=80 dport=53336
> \[ASSURED\] use=1 mark=3 bytes=529536  
> tcp 6 86390 ESTABLISHED src=192.168.1.114 dst=208.73.181.192
> sport=33621 dport=5223 src=208.73.181.192 dst=64.81.240.181 sport=5223
> dport=33621 \[ASSURED\] use=1 mark=0 l7proto=unknown bytes=1006750  
> tcp 6 54180 ESTABLISHED src=192.168.1.6 dst=58.39.46.168 sport=80
> dport=43104 \[UNREPLIED\] src=58.39.46.168 dst=64.81.240.181
> sport=43104 dport=80 use=1 mark=3 bytes=1492  
> tcp 6 15431 ESTABLISHED src=192.168.1.6 dst=76.238.142.66 sport=80
> dport=14501 \[UNREPLIED\] src=76.238.142.66 dst=64.81.240.181
> sport=14501 dport=80 use=1 mark=3 bytes=6000  
> tcp 6 15471 ESTABLISHED src=192.168.1.6 dst=76.238.142.66 sport=80
> dport=14495 \[UNREPLIED\] src=76.238.142.66 dst=64.81.240.181
> sport=14495 dport=80 use=1 mark=3 bytes=6000  
> tcp 6 86399 ESTABLISHED src=192.168.1.6 dst=192.168.1.1 sport=45191
> dport=22 src=192.168.1.1 dst=192.168.1.6 sport=22 dport=45191
> \[ASSURED\] use=1 mark=0 bytes=12571  
> tcp 6 15392 ESTABLISHED src=192.168.1.6 dst=76.238.142.66 sport=80
> dport=14395 \[UNREPLIED\] src=76.238.142.66 dst=64.81.240.181
> sport=14395 dport=80 use=1 mark=3 bytes=4500  
> tcp 6 15445 ESTABLISHED src=192.168.1.6 dst=76.238.142.66 sport=80
> dport=14488 \[UNREPLIED\] src=76.238.142.66 dst=64.81.240.181
> sport=14488 dport=80 use=1 mark=3 bytes=6000  
> tcp 6 86239 ESTABLISHED src=192.168.1.6 dst=208.65.153.251 sport=53522
> dport=80 src=208.65.153.251 dst=64.81.240.181 sport=80 dport=53522
> \[ASSURED\] use=1 mark=3 bytes=4682  
> tcp 6 86375 ESTABLISHED src=192.168.1.109 dst=209.85.199.83
> sport=50741 dport=80 src=209.85.199.83 dst=64.81.240.181 sport=80
> dport=50741 \[ASSURED\] use=1 mark=3 bytes=4500  
> tcp 6 54191 ESTABLISHED src=192.168.1.6 dst=58.39.46.168 sport=80
> dport=43069 \[UNREPLIED\] src=58.39.46.168 dst=64.81.240.181
> sport=43069 dport=80 use=1 mark=3 bytes=1492  
> tcp 6 15442 ESTABLISHED src=192.168.1.6 dst=76.238.142.66 sport=80
> dport=14443 \[UNREPLIED\] src=76.238.142.66 dst=64.81.240.181
> sport=14443 dport=80 use=1 mark=3 bytes=6000  
> tcp 6 86399 ESTABLISHED src=192.168.1.6 dst=209.85.199.19 sport=51337
> dport=443 src=209.85.199.19 dst=64.81.240.181 sport=443 dport=51337
> \[ASSURED\] use=1 mark=3 bytes=4924

2\. Find offending users (note the bytes=XXX lines above) and figure out
who they are using 'whois'. I never knew you could 'whois' an IP
address, like this:

> \# whois 208.73.181.192  
> \[Querying whois.arin.net\]  
> \[whois.arin.net\]
>
> OrgName: TiVo, Inc.  
> OrgID: TIVOI  
> Address: 2160 Gold St.  
> City: Alviso  
> StateProv: CA  
> PostalCode: 95002  
> Country: US  
> \[...\]

3\. For the truly offensive users, if they're coming in on port 80, block
them using apache. I found that one culprit seems to be a chinese IP
address (202.108.23.56) thats issuing HEAD and GET requests for all the
avi files in my gallery. These files are all big, and it seems to be
downloading the same content every day at nearly the same time. So,
after grepping through my httpd logs, like this:

> \[root@whisper httpd\]\# zcat \*.gz | grep "HEAD.\*mvi\_" | awk
> '{print \$1}' | sort | uniq -c | sort -k1n  
> 2 220.181.38.188  
> 4 192.168.1.6  
> 8 61.135.162.52  
> 10 65.94.160.128  
> 30 220.181.5.102  
> 47 220.181.26.9  
> 59 66.249.70.51  
> 70 61.135.166.44  
> 83 66.249.73.57  
> 93 61.135.162.107  
> 173 220.181.3.54  
> 185 202.108.23.56  
> 290 66.249.73.153  
> 1100 66.249.70.220

And then filtering out Googlebot (the bottom 2 IP addresses) I found a
pretty good list of 'abusers'.

4\. Block 'weird' crawler bots in robots.txt. I added the following
entries:

> User-agent: Yeti  
> Disallow: /
>
> User-agent: Twiceler  
> Disallow: /
>
> User-agent: Baiduspider  
> Disallow: /
>
> User-agent: YodaoBot  
> Disallow: /
>
> User-agent: Gigabot/3.0  
> Disallow: /

5\. If there are other offenders, I could create some iptables rules that
blocked their incoming IP addresses completely. This might be the real
solution to blocking the Chinese robots. I could use iptables to block
entire subnets of incoming traffic, which is pretty much what I think
may be necessary, but I'm not an expert in iptables syntax (yet).

I'm going to be keeping an eye on my outgoing bandwidth, and making sure
that I don't see any other big abusers. The real issue here is that when
crawlers, spiders, and leeches use up all my bandwidth, it makes the
experience for the 'real' users (friends & family) that much worse.
Also, since I listen to all my music over the network, it was causing
some stuttering issues for me at work, which really sucks.
