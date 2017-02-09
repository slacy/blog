Title: Mitigating ongoing attacks to my web server.
Date: 2009-01-01 20:42
Author: slacy
Category: General
Tags: apache, deny from, exploit, httpd, mediawiki, pnphpbb2, probed the server, security
Status: published

I've been seeing messages like this one in my Logwatch e-mails for quite
some time:

> A total of 2 sites <span class="nfakPe">probed</span> <span
> class="nfakPe">the</span> <span class="nfakPe">server</span>  
> 203.246.75.102
>
> A total of 7 possible successful probes were detected (<span
> class="nfakPe">the</span> following URLs  
> contain strings that match one or more of a listing of strings that  
> indicate a possible exploit):
>
> /wiki/index.php/Talk:AVR\_GCC//index.php?name=PNphpBB2&file=viewtopic&t=8/viewtopic.php?p=15&sid=be4c914eb746ac7c96beea717fdfc692/&highlight=%27.include(\$\_GET\[a\]),exit.%27&a=../../../../../../../../../../../../../../../../../../../../../../../../proc/self/environ%00
> HTTP Response 200

So I decided to take a brief look at it.  I'm fairly certain that this
isn't an exploit in my MediaWiki install -- I think they're looking for
an exploit in a package "PNphpBB2" which I don't have.  Anyway, I did
some grepping of my logs to find the bad IPs and created a simple conf.d
file that contains all the IP addresses that are bad.  The greps that I
did look like this:

zgrep "w00tw00t" /var/log/httpd/\*.gz | perl -p -e
"s/\^.\*\[\^0-9\](\[0-9\]+\\.\[0-9\]+\\.\[0-9\]+\\.\[0-9\]+)\[\^0-9\].\*\$/\\1/g"
| sort | uniq  
zgrep "\\.\\./\\.\\./\\.\\./\\.\\./\\.\\." /var/log/httpd/\*.gz | perl
-p -e
"s/\^.\*\[\^0-9\](\[0-9\]+\\.\[0-9\]+\\.\[0-9\]+\\.\[0-9\]+)\[\^0-9\].\*\$/\\1/g"
| sort | uniq  
zgrep "PNphpBB2" \*.gz | perl -p -e
"s/\^.\*\[\^0-9\](\[0-9\]+\\.\[0-9\]+\\.\[0-9\]+\\.\[0-9\]+)\[\^0-9\].\*\$/\\1/g"
| sort | uniq

And then I put those all in a file under /etc/httpd/conf.d called
"global\_deny.conf" that looks like this:

&lt;DirectoryMatch .\*&gt;  
Order Allow,Deny  
allow from all  
deny from \[...\]  
deny from \[...\]  
&lt;/DirectoryMatch&gt;

With one IP address on each "deny from" line. Hopefully this should shut
out a lot of the people that are trying to find exploits on my site.
There were 845 unique IP addresses that had hit such URLs.

Does anyone know of an automated solution for doing stuff like this?
What I'd like to be able to is to have a regexp of URLs that if you ever
hit them, then you automatically end up in a set of denied IP addresses.
Maybe it would show a special "you're an abuser" webpage for the first
few hits after that, and then just begin 404ing.
