Title: Problems with the Cyrus seen flag
Date: 2005-04-22 07:00
Author: slacy
Category: Linux Stuff
Status: published

After first installing (or actually, being  
forced to install cyrus) when I upgraded from Fedora Core 1 to Fedora  
Core 2, I had the following problem:

Messages that I had marked as read (seen) would not keep their  
status across restarts of the mail program that I am using  
(Thunderbird) Additionally, when I selected "Compact Folders" all  
messages would be marked unread.

I found the following page that describes a fix:

<http://asg.web.cmu.edu/archive/message.php?mailbox=archive.info-cyrus&msg=26945>  
<http://www.irbs.net/internet/info-cyrus/0401/0354.html>

I did it, and it worked great for me. Everything is (finally) fine.

  

Here are the contents from the original posts:

Yesterday I posted a question to this list regarding a problem I was  
having with the mailboxes for some users on cyrus 2.1.15; namely  
previously read messages were being marked as "unread" every time the  
mailbox listing was refreshed by the IMAP server. One thing I didn't
make  
clear was that this problem was independent of MUA: using pine  
directly on the mailhost was no better than using Thunderbird on a
Windows  
client; as soon as pine was quit and restarted, the "N" would reappear
on  
previously viewed messages.

In any case, I tried several things including

-   restarting the cyrus master daemon
-   checking ownership and permissions on all the cyrus database files
-   running ctl\_cyrusdb -r

None of this worked, and all the permissions/ownership on the database  
files was correct.

The only thing which worked was deleting this file
:   /var/lib/cyrus/user/t/this\_user/this\_user.seen

Steps:  
1. Stop cyrmaster  
2. rm /var/lib/cyrus/user/t/this\_user/this\_user.seen  
3. Start cyrmaster

the this\_user.seen db file was automatically recreated and read
messages  
stayed read between restarts of the MUA.

I suppose that a drawback of simply deleting the seen database file is  
that all information about which messages have been read is lost, but
it's  
not at all clear at this point that there was any alternative.
