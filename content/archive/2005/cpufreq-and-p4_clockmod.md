Title: cpufreq and p4_clockmod
Date: 2005-10-07 00:24
Author: slacy
Category: Linux Stuff
Status: published

I just found out (as I was researching some of the newer AMD features)
that Fedora Core 4 supports the ability to dynamically adjust CPU
frequency for both AMD and Intel CPUs! ~~For some weird reason, you have
to manually modprobe the drivers (which is completely rediculous in my
opinion) but once you do,~~ you can set the CPU to automatically step
down to lower clock frequencies. The coolest thing is that you can set
an "ondemand" policy that makes the frequency adjust automatically and
respond fairly quickly.

I found a lot of the details
[here.](http://www.clasohm.com/blog/one-entry?entry_id=12858)

Here's what I had to do:

\#yum install cpufreq-utils cpuspeed  
~~  
\#modprobe cpufreq\_conservative  
\#modprobe cpufreq\_stats  
\#modprobe cpufreq\_powersave  
\#modprobe cpufreq\_ondemand  
\#modprobe p4\_clockmod  
~~

Edit /etc/cpuspeed.conf to say:  
DRIVER="p4-clockmod"

\#checkconfig cpuspeed on  
\#service cpuspeed start

<strike>  
And then you can say:

\#cpufreq-set -g ondemand  
</strike>

And then you can add a "CPU Frequency Scaling Monitor" to your panel,
and see what the current CPU frequency is all the time. Its pretty cool.
The one problem I see is that it tends to pick a frequency thats a bit
too low. What I want it to do is have some delay -- after I need the
CPU, keep the clock rate high for 30 seconds or so before stepping down
again.

I think this might be a good way to keep my new system cool and quiet
and energy efficient, all at the same time. Now, I just need to figure
out how to get my hard drives to power down... (its not the hardware
thats the problem, the question is about how do you keep a running
server and give the HDD's any chance to actually be idle for a few
minutes.)
