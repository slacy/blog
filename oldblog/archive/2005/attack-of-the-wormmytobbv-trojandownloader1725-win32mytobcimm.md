Title: Attack of the Worm.Mytob.BV (Trojan.DownLoader.1725, Win32.Mytob.CI@mm)
Date: 2005-05-22 23:41
Author: slacy
Category: Linux Stuff
Status: published

About a week ago, I started seeing these virus e-mail messages with
subjects like "Your email Account is suspended for security reasons" and
"Notice: \*\*Last Warning\*\*" coming through an open relay in the
Netherlands. Neither my virus scanner or SPAM filter recognized them as
malicious.

So, in the middle of last week, I submitted a sample to
[clamav.net](http://clamav.net) which is the virus scanner that I run,
and at almost the exact same time, the messages began to be marked as
SPAM because someone had added the source IP to the RBL, and the message
bodies to Pyzor, DCC, etc. They were coming in at about 10-20 per day,
and going into my SPAM folder.

I checked back with
[clamav.net](http://lurker.clamav.net/message/20050522.110718.c953273e.en.html),
and they have classified the virus as Worm.MyTob.BV.

Today, I got about 125 of these messages. I suspect its on the rise, and
this is the first time that I've seen a fair number of virus messages in
the early stages get through my filters.

In the future, when I see a virus or suspicious message that wasn't
classified by the scanners (even if it is caught as SPAM) I'm going to
immediately report it at clamav.net, and allow them to share the
information.

I fear that MyTob.BV is going to be a pretty big problem.

Interestingly enough, many of the messages contain a link that says
"your account has expired, click here to log in" with a link to the
domain that the e-mail is targeted to (in this case, that would be a
link to my own site at slacy.com). I find this very odd (what is their
gain? Why are they doing this?) but I've noticed almost no increase in
web traffic because of it.

Note: The first copy of this type of thing I got has been classified as
Worm.MyTob.BN-2. I recieved this first message on 5/11, and it was
classified on 5/17, so I could have been a great help in the cause.
Since then, its mutated through several versions, and BN seems to be the
one thats catching on.
