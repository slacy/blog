Title: Image Spam, Spamassasin, spamcop.net, Yahoo & You.
Date: 2006-09-15 13:43
Author: slacy
Category: Linux Stuff
Status: published

To try to compat all this image-spam thats been coming through lately, I
boosted up a bunch of my spamassassin rule values to try to filter
things out. The only rule that the image spam was hitting were a bunch
of the different "blacklist" and "black hole" servers that spamassassin
can use. So, when a message slipped through, I see which rules it
matches, and I boost things up so that the next one like that will be
considered spam. The resultant rules look like this:

> \# score RCVD\_IN\_XBL 0 3.114 0 3.897  
> score RCVD\_IN\_XBL 0 15.000 0 15.000  
> score RECV\_IN\_SORBS\_WEB 0 1.236 0 1.456  
> score RCVD\_IN\_SORBS\_SOCKS 0 1.823 0 2.159  
> \# score RCVD\_IN\_NJABL\_DUL 0 1.713 0 1.946  
> score RCVD\_IN\_NJABL\_DUL 0 8.0 0 8.0  
> score RCVD\_IN\_NJABL\_PROXY 0 0.327 0 0.721  
> \# score RCVD\_IN\_SORBS\_DUL 0 1.988 0 2.046  
> score RCVD\_IN\_SORBS\_DUL 0 5.000 0 5.000  
> score HTML\_IMAGE\_ONLY\_24 1.316 0.930 1.771 1.841  
> score HELO\_DYNAMIC\_SPLIT\_IP 2.880 2.880 3.330 2.191
>
> \# score RCVD\_IN\_BL\_SPAMCOP\_NET 0 1.332 0 1.558  
> score RCVD\_IN\_BL\_SPAMCOP\_NET 0 8.000 0 8.000

But here's the problem: All mail from yahoo.com (Yahoo mail, yahoo
groups & mailing lists) comes from an IP address at yahoo that makes it
match the RCVD\_IN\_BL\_SPAMCOP\_NET rule. Arg! So, I get a valid
message that has the following spamassin rules:

> \* 0.1 RCVD\_BY\_IP Received by mail server with no name  
> \* 0.0 URI\_REDIRECTOR Message has HTTP redirector URI  
> \* 0.1 HTML\_80\_90 BODY: Message is 80% to 90% HTML  
> \* -2.6 BAYES\_00 BODY: Bayesian spam probability is 0 to 1%  
> \* \[score: 0.0000\]  
> \* 0.0 HTML\_MESSAGE BODY: HTML included in message  
> \* 0.0 HTML\_NONELEMENT\_00\_10 BODY: 0% to 10% of HTML elements are
> non-standard  
> \* 8.0 RCVD\_IN\_BL\_SPAMCOP\_NET RBL: Received via a relay in
> bl.spamcop.net

Grrrr! Why is yahoo listed in the spamcop.net black hole list? Why don't
they fix this?! (By trimming down the amount of outbound spam coming
from these domains). This is \*really\* annoying. I may have to find
that image OCR spamassassin plugin and see if I can get it working. I'm
really hesitant to tweak out my virtually vanilla spamassassin configs,
though. Its just more work later when I have to upgrade...
