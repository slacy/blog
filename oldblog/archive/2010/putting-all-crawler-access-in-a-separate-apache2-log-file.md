Title: Putting all crawler access in a separate apache2 log file? 
Date: 2010-04-27 09:17
Author: slacy
Category: General
Tags: apache2, apache2 crawlers, crawlers, logs
Status: published

Is there an easy way to configure apache2 so that all known crawler
accesses (googlebot, yahoo slurp, etc) all go into their own log file,
and everything else remains in the regular .log file?  I'm hoping for
something like "access.log", "crawl.log" and "error.log".    Seems like
it would have to have a well maintained list of known crawler user-agent
strings, and I'm not sure if this can be done without a custom apache2
module.
