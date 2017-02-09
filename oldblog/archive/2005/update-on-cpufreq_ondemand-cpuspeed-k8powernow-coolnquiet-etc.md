Title: Update on cpufreq_ondemand, cpuspeed k8powernow, Cool'n'Quiet, etc.
Date: 2005-11-20 23:57
Author: slacy
Category: Linux Stuff
Status: published

Okay, so here's the scoop:

I took a look at the source code for cpuspeed, and its basically brain
dead. I don't think its a really "useful" piece of software. I had
originally recommended it, because it seemed to modprobe for the right
drivers automatically. Thats true, but its about the only useful thing
that it does. The biggest drawback of cpuspeed is that its response time
was way too slow. The "ondemand" policy is much simpler and really works
great.

So, my new recommendation is to add the following 2 lines to your
/etc/rc.d/rc.local:  
` modprobe cpufreq_ondemand cpufreq-set -g ondemand`  
And thats it, easy as pie.
