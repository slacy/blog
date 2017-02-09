Title: PHP Warnings from Squirrelmail
Date: 2005-11-19 19:24
Author: slacy
Category: Linux Stuff, Web
Status: published

While setting up my new server, I had some trouble getting Squirrelmail
to work. I'm trying to do a "staged" switch from one machine to the
other, and the first to get moved is the web frontends. So, my mail
backends are still on the old server, which means that squirrelmail
needs to talk to the remote machine. Configuring for a remote IMAP
server was showing me a "permission denied" error. The error that was
showing up in my http error log was:

\[client xxx.xxx.xxx.xxx\] PHP Warning: fsockopen()
\[[function.fsockopen](function.fsockopen)\]: unable to connect to
xxx.xxx.xxx.xxx:25 (Permission denied) in \[...\]/configtest.php on line
266

The issue was the selinux permissions on the web server -- what I was
trying to do violated the selinux permissions scheme that was currently
in place. I ran "system-config-securitylevel" and under the SElinux tab,
selected the HTTPD permissions, and checked the box that says "Allow
HTTPD scripts to connect to the network". This then allowed PHP scripts
on the new machine to talk to the mail server on the old machine.

It seems to me that the error message should be a little more
appropriate -- "SElinux policy violation" would have been just fine.
Instead, I got a generic "Permission Denied" which could mean virtually
anything.
