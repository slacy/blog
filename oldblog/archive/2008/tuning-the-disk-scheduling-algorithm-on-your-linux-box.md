Title: Tuning the disk scheduling algorithm on your Linux box.
Date: 2008-04-18 14:35
Author: slacy
Category: General
Status: published

If you want to change the disk scheduling algorithm on your Linux box,
you can:

> \# echo /sys/block/\*/queue/scheduler; cat
> /sys/block/\*/queue/scheduler

The one with brackets around it is currently selected. Echo into
/sys/block/\*/queue/scheduler to set a new value. CFQ is the default on
newer kernels, and I think has the best performance, but both deadline
and anticipatory can offer better performance for some workloads.
