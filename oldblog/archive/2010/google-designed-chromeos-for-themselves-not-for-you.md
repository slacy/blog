Title: Google designed ChromeOS for themselves, not for you. 
Date: 2010-12-17 21:14
Author: slacy
Category: General
Tags: chromeos, cr-48, google
Status: published

I've been using my Cr-48 for about a week, and just the other day, it
hit me.  I understand how and why they're developing ChromeOS.

It's easy.  They're doing it for themselves, not for you as an end user.
 You see, internally, Google has almost completely switched to Google
Apps.  There's very little need for Office, Word, Photoshop, Powerpoint,
Execl, and the usual array of other desktop apps.  In fact, if you're
sending out attached .XLS files, you're pretty much guaranteed to be
made fun of.

Even within Engineering, most Googlers do their development on their
desktop machines, and use their laptop for meetings, note-taking, and
lightweight working at home.  Those that use laptops for development are
actually just connecting to remote machines and doing the heavy lifting
there.  You don't develop Google-scale applications in a standalone
laptop environment, that's for sure.

In the aftermath of the Google China hacks, the obvious first step was
to transition as many machines away from Windows as possible.  The
second step, of course, is to make a laptop that's completely impervious
to hackers.  A machine that has no maintainence costs.  No upstream
distributions to follow.  No stored ssh keys.  No local storage
whatsoever.  In other words, what they wanted was ChromeOS, and they
wanted for themselves.

There's tons of internal precedent for this kind of action.  When Google
first started, they were buying commodity motherboards and racking them
up into makeshift server farms.  Now, the story is different.  At
today's scale, they have the luxury of building entire buildings to
house completely customized end-to-end hardware systems.  They must have
realized that they were at a tipping point of desktop end-user systems
as well.  At their current size, it became cost effective to develop and
deploy their own portable computer.

So, Google designed ChromeOS for their employees, and for their own
specialized internal use cases.  It's a totally selfish move.  It's
meant to make a totally bulletproof system that works anywhere for a
100% Google Apps user.  The Cr-48?  It's their internal trial machine.
 They made it so that they can start switching their internal employees
over to ChromeOS for their primary portable system, and so that they can
ditch the heavy, high-maintenance security holes that are the existing
Windows and Ubuntu laptop base.  And, if you're going to do a production
run of hardware like the Cr-48, the cost difference between 10,000
machines and 100,000 machines is probably almost in the noise, so why
not make bunch, give them away, and see how they're accepted in the
outside world?

But the key point is:  Google doesn't care at all what the outside world
thinks.  What matters is whether or not this works internally as a
productive laptop for Googlers.  If this works, then maybe they'll try
to figure out what market they can capture with this thing, and go after
that.
