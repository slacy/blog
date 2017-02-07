Title: Thoughts on a Flash-based TiVo User Interface
Date: 2010-03-03 11:04
Author: slacy
Category: General
Tags: adobe, flash, premiere, tivo, xl, youtube
Status: published

Okay, huge disclaimers here.  I used to work at TiVo, and specifically
worked on several parts of the user interface framework, and I now work
at Google, and have worked on the YouTube backend infrastructure.

One big struggle at TiVo was always what the "next generation" UI
framework should be.  Straight C++? Java?  Networked remote display
protocol (HME)?  JavaScript + HTML? XML-driven layout with C++ logic?
Java + Comcast (take2)?  Flash?

So, now we know what actually shipped!   The new TiVo Premiere has been
announced, and the most interesting point is that the UI claims to be
implemented in **Flash**.  Yes, Adobe Flash.  I can sort of see the
appeal, since that means your designers can do mocks using their
favorite Adobe tools on a Macintosh and get pixel-accurate
representation on the set-top.  That's pretty cool, and hopefully will
make TiVo a lot more agile when it comes to UI innovation. The delay
cycle between UI design and implementation was usually 12+ months. 
Maybe now it'll be a little faster.

But, the use of Flash has some other possible ramifications that no one
seems to be picking up on:

**Can I connect my PC's browser to my TiVo Premiere box and see the full
Flash user interface on my desktop?**

That's a huge question!  Flash has the potential to deliver a
remote-display experience that's pixel-accurate from the set-top
experience, and do it in a cross-platform way!   If desktop flash itself
were upgraded to support ATSC-spec video formats (or if TiVo started
transcoding their video), then I can foresee being able to browse to my
TiVo and actually be able to play back the content, right in my
browser.  Although transcoding might sound far fetched, there are
hardware solutions provided by Broadcomm that could do exactly this: 
Transcode HD broadcast format from disk to Flash-capable MP4, in real
time.  I haven't checked the specs of the Premiere's internals to know
if their hardware is capable of this or not.

**Can I view flash-enabled websites on TiVo Premiere?**

If this is a full, Adobe-certified flash implementation, then if TiVo
integrates with WebKit or any other browser platform, then we can get
full Web+Flash on our TVs.  The interesting thing here?  That brings
access to [thedailyshow.com](http://thedailyshow.com),
[hulu.com](http://hulu.com), [tv.com](http://tv.com),
[vimeo.com](http://vimeo.com),
[collegehumor.com](http://collegehumor.com), and all the other niche
websites that are producing and/or delivering high quality content. 
They're currently only delivering that content to the desktop, because
that's the only place where "full Flash" has a foothold.  Existing TVs
with (for example) YouTube support use a Google-provided API to access
the metadata and content.  By putting Flash in the livingroom, we have
the possibility for accessing all that content with our friendly peanut
remotes.

**What about HTML5?**

Yeah, you wouldn't think that TiVo would be getting itself twisted up in
the HTML5 vs. Flash debates, but here we are.  For example, if YouTube
were to move to HTML5 for their playback UI, then TiVo would need to
make sure that their browser experience works with HTML5 as well, and
the Flash would "fall by the wayside" for the external video sources
mentioned above.  So, that would leave TiVo as an island of Flash
support floating in an HTML5 sea.  Certainly it'll take a long time for
all the above mentioned sites to switch over, so I suspect that TiVo has
a long time to react to this ongoing situation.  (But, they're
notoriously slow at reacting.  One could argue that this switch two
flash should have happened 4+ years ago for them to "stay with the
times")

I bet the TiVo Premiere hardware is capable of nearly everything
mentioned above.  The question is:  **Can TiVo get their act together
and ship more new innovative features for this platform?** I don't have
a lot of faith, since they've had a really hard time innovating in
feature-space in the past, but I'd love to see it happen!

**Are you sure you really want to abandon your existing userbase,
again?**

First there was the Series1 to Series2 transition.  Not a huge deal,
since there really weren't that many Series1 boxes out there, but from
an innovation standpoint, those users got orphaned.

Then, there was the Series2 to Series3 transition.  I'm not sure what
the numbers were, but there were *millions* of Series2 customers that
got left behind on this one.  This matters to TiVo if they're trying to
build a revenue stream with innovative software features.  If you're
dead-ending your existing customer base, then you can't ship them new
features that generate revenue.

Now, we have the Series3 to Series4 transition.  Is TiVo going to "bet
the bank" on this new platform, or are we going to see the "Premiere"
software stack ported back to S3 units?  Are they fast enough?  Do they
have enough RAM?  Are there other fundamental changes to the Premiere
software stack, like on-disk database formats, that make the upgrade
impossible?

I'm nervous that TiVo is again"betting the bank" on a new platform with
a zero-user install base.  Good luck to making that one work.

**Paying royalties to Adobe cuts into TiVo's bottom line.**

I presume that TiVo is using an Adobe-provided Flash implementation, and
that means they need to pay a licensing fee to Adobe for every unit
shipped.  This means it cuts into TiVo's bottom line revenue for every
unit sold.  Is this really what they want to be doing?   They must
expect that new revenue opportunities make the Premiere software
platform more profitable than the existing software base.  Time will
tell.

**What about DirecTV?**

If I remember right, a new TiVo + DirecTV box is due later this year. 
Is this going to be based on the Series4 platform?  What other changes
are we likely to see?  Was the move to Flash backed by DirecTV?

P.S.: Did you know that everySeries2 and beyond TiVo box is capable of
Picture-In-Graphics, and that it's just a "small matter of software" to
make it work in the TiVo UI?
