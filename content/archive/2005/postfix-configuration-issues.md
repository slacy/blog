Title: Postfix configuration issues.
Date: 2005-12-05 23:44
Author: slacy
Category: Linux Stuff
Status: published

I've had my new server running for a while, but mail that did not
qualify with a hostname was not being delivered correctly. For example
mail to "root" (without a domain name) was bouncing.

The /var/log/mailllog said:

` Dec  5 22:30:53 whisper postfix/smtp[28147]: F3D372618010: to=, relay=none, delay=1, status=bounced (Host or domain name not found. Name service error for name=whisper.slacy.com type=A: Host not found)`

I resolved the problem, and it was twofold.

First, postfix was not consulting the /etc/hosts file to resolve DNS
names. I had to add the following to my /etc/mail/main.cf file:

` smtp_host_lookup = native`

I'm not sure why the default for this is "dns" (which does not obey the
local host rules) but it is. Resolved.

The second issue was that I had somehow set myhostname to be the name of
my domain instead of my full hostname. This resulted in mail being
bounced with a "loops back to myself" error. So, setting myhostname to
be my complete hostname worked just fine.

Oh, and I had to make sure that /etc/hosts contained entries for
\$myhostname.

There's a lot of misinformation about this issue floating around on the
'net, so hopefully this will help out a couple of people.
