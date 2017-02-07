Title: Removing smtp-amavis
Date: 2005-04-27 22:56
Author: slacy
Category: Linux Stuff
Status: published

Okay, with my new mail configuration, I've decided to move to a more
"standard" SPAM & virus setup, removing amavis.

I had a problem where even after removing all references to smtp-amavis
from my postfix configuration files (main.cf, master.cf) I could see in
/var/log/maillog that it was still trying to go through smtp-amavis. The
solution was found
[here](http://archives.neohapsis.com/archives/postfix/2004-01/2783.html)
where they say that you need to run:

    postsuper -r ALL

My main motivations for getting rid of Amavis-new are:

<li>
No support for more versions of amavis (they aren't quickly forthcoming)

</li>
<li>
I was never logging into amavis anyway, making it pretty much pointless,
although it was doing a good job of filtering

</li>
<li>
It didn't work with the "standard" RPM install of clamav, so I was
behind on that version as well

</li>
<li>
It does a lot more than I really need.

</li>
I'm going to be setting up two shared folders for "SPAM" and "Viruses"
and just use a standard filtering and training on those folders.
