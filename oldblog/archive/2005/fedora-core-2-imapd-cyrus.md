Title: Fedora Core 2, imapd & cyrus
Date: 2005-04-22 07:00
Author: slacy
Category: Linux Stuff
Status: published

So, I upgraded my system to Fedora Core 2 last weekend, and there was a
big surprise:

The U of W imap server isn't supported or distributed anymore, so I had
to switch to using the new (and only) imap server: cyrus.

Cyrus is okay, but administration is a pain in the ass.

So, I had to update all my mbox mail into cyrus, and couldn't really
find any good instructions on the web, so I'll post some here.

In general, its a 3-step process:

1\. Create mail folders using <span
style="font-weight: bold;">cyradm</span>  
2. Use <span style="font-weight: bold;">formail</span> and <span
style="font-weight: bold;">cpmsg.pl</span> (see below) to translate mbox
file into cyrus messages  
3. Run <span style="font-weight: bold;">reconstruct</span> on the cyrus
folders.

  

### Step 1: Use cyradm to create mailboxes

This is fairly easy. If you're not familiar with cyradm, here are the
things that you need to know:

You should know that all the mailboxes in cyrus are named things like  
"user.username" where "username" is the IMAP user name. So, you want  
to do something like this:

<span style="font-family: courier new,courier,monospace;">cyradm -U
cyrus localhost</span>  
  
<span style="font-family: courier new,courier,monospace;">IMAP
Password:</span>  
  
<span style="font-family: courier new,courier,monospace;">cm
user.username.MigratedMessages</span>  
  
<span style="font-family: courier new,courier,monospace;">cm
user.username.MigratedMessages.foldername</span>

etc. once for each folder that you are going to migrate.

### Step 2: Use formail and cpmsg.pl to translate mbox files into cyrus messages

Formail is a unix program that will parse mbox formatted messages and  
do things with them. What you want to do is turn each message into a  
cyrus-style message file in the right directory.

Here's the text of cpmsg.pl that I stole from another site. Basically,  
it names the file correctly, and puts some extra newlines on the end:  
  
  
<span
style="font-family: courier new,courier,monospace;">\#!/usr/bin/perl
-w</span>  
  
<span style="font-family: courier new,courier,monospace;">\#</span>  
  
<span style="font-family: courier new,courier,monospace;">\# Usage: cat
mailbox.txt | formail -s cpmsg.pl</span>  
  
<span style="font-family: courier new,courier,monospace;">\#</span>  
  
<span style="font-family: courier new,courier,monospace;">\# where
'cpmsg.pl' is the name of this script</span>  
  
<span style="font-family: courier new,courier,monospace;">\#</span>  
  
<span style="font-family: courier new,courier,monospace;">\# Purpose:
Called by formail once for each mail message in a Berkeley-</span>  
  
<span style="font-family: courier new,courier,monospace;">\# format
mailbox</span>  
  
<span style="font-family: courier new,courier,monospace;">\#</span>  
  
<span style="font-family: courier new,courier,monospace;"></span>  
  
<span style="font-family: courier new,courier,monospace;">\$maildir =
"\$ARGV\[0\]";</span>  
  
<span style="font-family: courier new,courier,monospace;">if
(!\$maildir) { die "Usage: \$0 \$maildir"; }</span>  
  
<span style="font-family: courier new,courier,monospace;"></span>  
  
<span style="font-family: courier new,courier,monospace;">\# Formail
increments this number for each message. The</span>  
  
<span style="font-family: courier new,courier,monospace;">\# leading
"0"'s must be removed (e.g. 001 becomes 1)</span>  
  
<span style="font-family: courier new,courier,monospace;"></span>  
  
<span style="font-family: courier new,courier,monospace;">\$filenum =
(\$ENV{FILENO} - 0) + 1;</span>  
  
<span style="font-family: courier new,courier,monospace;"></span>  
  
<span style="font-family: courier new,courier,monospace;">open
(OUTFILE,"&gt;\$maildir/\$filenum.");</span>  
  
<span style="font-family: courier new,courier,monospace;"></span>  
  
<span style="font-family: courier new,courier,monospace;">while
(<stdin>) {</stdin></span>  
  
<span style="font-family: courier new,courier,monospace;">
chomp;</span>  
  
<span style="font-family: courier new,courier,monospace;"></span>  
  
<span style="font-family: courier new,courier,monospace;"> print OUTFILE
"\$\_

</span>Take the above source code, past it into a scrpt called cpmsg.pl,
and save it.  You're now ready to start converting the mailboxes. 
Basically, you want to do this:

cat mbox\_filename | formail -s ./cpmsg.pl
/var/spool/imap/u/user/username/MigratedMessages/foldername

That will take the mbox\_filename listed, and call cpmsg.pl once for
each message in the file, placing them in the named folder.  Then
cpmsg.pl does some very simple formatting, and saves out the individual
files with the filenames that cyrus expects to see.  <span
style="font-weight: bold;">NOTE: DO NOT RUN THIS ON A CYRUS MAILBOX THAT
ALREADY HAS MESSAGES IN IT.  IT WILL OVERWRITE THE EXISTING
MESSAGES.</span>  You have been warned.

### Step 3: Run reconstruct on all the toplevel mailboxes

This step is fairly straightforward. You just have to run the cyrus
command "reconstruct" for each user mailbox. This process creates the
required indices and database entries for each e-mail message. The
syntax is as follows: (for Fedora Core 2 Systems)

<span style="font-family: courier new,courier,monospace;">\# su -
cyrus</span>  
<span style="font-family: courier new,courier,monospace;">\#
/usr/lib/cyrus-imapd/reconstruct -r user.username</span>

Thats it! You should be good to go with all your mailboxes migrated
safely.
