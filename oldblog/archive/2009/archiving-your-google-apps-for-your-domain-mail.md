Title: Archiving your Google Apps for your domain mail.
Date: 2009-07-29 17:12
Author: slacy
Category: General
Tags: backup, fetchmail, gmail, google apps, google apps for your domain, mail backup
Status: published

There are many guides to using fetchmail to backup your gmail account,
but I use Google Apps For Your Domain to host my mail.  So, I needed to
craft up a slightly modified version of the fetchmail commandline:

> \$ fetchmail --ssl -p pop3 -vk --user slacy@slacy.com pop.gmail.com

The funny thing is that within a few minutes of running this script, I
got e-mails from my friends saying "Hey, did you mean to send this to
me" and "I got this weird message about delivery failure from you".

Reading the fetchmail man page in more detail, it says that after
fetching the mail, it delivers it via the local delivery agent.  In my
case, I suspect that what's happening is that it's going to my local
SMTP server, which is set up to forward back to GMail, and I think that
somehow created the re-sending.

If you have any other ideas how or why a fetchmail run would re-send old
messages to other recipeients, let me know.  I'm going to have to do a
fair amount of digging before I re-run the script.
