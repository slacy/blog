Title: Is it safe to rm files from /var/spool/mqueue?
Date: 2010-04-08 10:06
Author: slacy
Category: General
Tags: /var/spool/mqueue, linux, rm, sendmail
Status: published

Is it safe to just remove messages that are failing to be delivered, or
is there some other special sendmail "cancel delivery" command that I
can execute to remove these from the queue?  Is it necessary to stop
sendmail if I touch /var/spool/mqueue, or can I just rm the queued
message files there while sendmail is still running?

(FYI this is on Ubuntu 8.04.4 LTS)
