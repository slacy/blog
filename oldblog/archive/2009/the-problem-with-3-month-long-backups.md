Title: The problem with 3-month long backups.
Date: 2009-03-17 13:24
Author: slacy
Category: General
Status: published

Here's the problem with having a backup strategy that takes 3 months: 
Your Linksys wireless router has an uptime &lt; 3 months, and when it
reboots, you lose your connection to the backup server, so you have to
restart the backup process.

Additionally, you don't actually realize that the initial backup that
had been running for the last 3 months wasn't quite right (the owner &
permissions were wrong on the backed up files).  So, although you
thought you'd be able to do delta incremental backups, that first try
doesn't count.  So, you pretty much have to back up the whole thing
again.

Oh, and since you got kinda screwed by using up 90% of your DSL line's
bandwidth, you throttle this one more aggressively, which means it's
going to take even more time to complete.  Oh well!
