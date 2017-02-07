Title: What Larry Page really needs to do to return Google to its startup roots
Date: 2011-03-24 10:57
Author: slacy
Category: General
Tags: development, engineering, google, incubator, roots, scale, startup
Status: published

I worked at Google from 2005-2010, and saw the company go through many
changes, and a huge increase in staff.  Most importantly, I saw the
company go from a place where engineers were seen as violent disruptors
and innovators, to a place where doing things "The Google Way" was king,
and where thinking outside the box was discouraged and even chastised.
 So, here's a quick list of things I think Larry could do to bring the
startup feel back to Google:

Let engineers do what they do best, and forget the rest.
--------------------------------------------------------

This is probably the most important single point.  Engineers at Google
spend way too much time fussing about with everything other than
engineering and product design.  Focusing on shipping great, innovative
products needs to be put before *all* else.  Here's a quick rundown of
engineering frustrations at Google when I left:

-   **Compiling & fixing other people's code.** This is a huge problem
    for the C++ developers at Google.  They spend massive amounts of
    time compiling (and bug fixing) "the world" to make their
    project work.  This needs to end.  Put an end to source-code
    distributions for cross-team dependencies.  Make teams (bigtable,
    GFS, Stubby, Chubby, etc.) deliver binaries & headers in some
    reasonable format.
-   <span style="color: #000000;">**Machine Resource Requests**</span>
    for products in the "less than a petabyte" class. Just hand out the
    resources pro-bono, track usage, and if they exceed some very high
    limit, then start charging.  Why is this a struggle?
-   **LCE & SRE "blockers"**.  Having support for Launch Coordination &
    Site Reliability is great, but when these people say "you can't
    launch unless..." then you know they're being a hindrance, and not
    a help.
-   **Meetings**.  Seriously, people are drenched in "status update" and
    "team" meetings. If your company has to have "No meetings Thursday"
    then you're doing it wrong. How about "No meetings except
    for Thursday".  That would make for a productive engineering team,
    not the other way around.
-   **Weekly Snippets, perf, etc.** I was continually amazed by the
    amount of "extra cruft work" that goes on.  I know it sounds
    important, but engineers should be coding & designing.
-   **Perf, Interviews & lengthly interview feedback.** The old
    fashioned model of getting together in a room to discuss a candidate
    is way more efficient.  Make sure that every single engineer in the
    building is participating in the interview process to spread the
    load more evenly.  Don't let the internal recruiters pick engineers
    for interviews, as they have favoritism and are
    improperly motivated.   Limit to 1 interview per week, maximum.  
    Make a simple system for "I can't make this interview" and "I think
    this resume looks shitty and don't want to talk to this candidate."
-   **Discourage of open source software.** There is so much innovation
    going on in the open source world: Hadoop, MongoDB, Redis,
    Cassandra, memcached, Ruby on Rails, Django, Tornado (web
    framework), and many, many other products put Google infrastructure
    to shame when it comes to ease-of-use and product focus.  Engineers
    are discouraged from using these systems, to the point where they're
    chastised for even thinking of using anything other than
    Bigtable/Spanner and GFS/Colossus for their products.

Get rid of the proprietary cluster management system.
-----------------------------------------------------

Yes, seriously.  What they have is a glorified batch-scheduling system
that makes modern datacenters feel like antiquated mainframes.
 Dedicated machines and resources are what startups have, so give them
to your best engineers, and they'll do great things. You should have
learned this from the teragoogle team.  Start building a better, Virtual
Machine based system where engineers can own & manage machine images
themselves, all the way down to the operating system, dependencies, etc.
 If more structure is needed, use existing open source packages or
develop new systems in house, and open source those.  Build new
"non-standard" data centers that don't use the old system, and that
every engineer can use.

The cluster management system's fatal flaw is that it requires too large
of an ecosystem, and pidgeon-holes running jobs into a far too
restrictive container.  It doesn't allow persistent local disk storage,
since jobs can be terminated and relocated at any time.  Services
running there are then cajoled into using Bigtable and/or Colossus for
their persistent storage, which rules out virtually all other external
database systems (MySQL, etc.).   This is an antiquated and overly
constrained model for job allocation.

Switch to team-based distributed source control.
------------------------------------------------

Teams or large related teams should manage their own source code.
 Provide git-based hosting, and nothing else.  Cross-team deliverables
should be done at the binary release level, not at the source code
level.  Hard Makefile-type dependencies between teams need to be
abolished.

[Be the Bazaar, not the
Cathedral.](http://www.catb.org/~esr/writings/cathedral-bazaar/)

Rethink the "lots of redundant, unreliable hardware" mantra.
------------------------------------------------------------

Having to launch a simple service in multiple datacenters around the
world, and having to deal with near-weekly datacenter maintenance
shutdowns is unacceptable for an agile startup.  Startups need to focus
on product, not process and infrastructure.  One persistent Amazon EC2
instance is much more valuable than a 100 batch scheduled jobs in a
cluster that goes down for maintenance every week. Stop doing that.

Eliminate NIH-syndrome
----------------------

Google has a very, very strong NIH (Not Invented Here) syndrome.
 Alternate solutions (Hadoop, MongoDB, Redis, Cassandra, MySQL,
RabbitMQ, etc.) are all seen as technically inferior and poorly
engineered systems.  Google needs to get off it's high horse, and look
at what's happening outside of it's organization.  Hugely scalable
services like Twitter are built on almost entirely open source stack,
and they're doing it really efficiently.  Open source solutions have a
product-focus that's missing from much of Google's infrastructure for
infrastructure's sake engineering endeavors.  Focusing on the product
first, and using any available solution is the agile way to experiment
in new spaces.

Additionally, by eliminating the NIH syndrome, Google needs to allow
these open systems into it's production environment.  Amazon and
RackSpace have nailed this with reliable, virtual hosting solutions, and
this is allowing services built on those platforms to be portable,
efficient, and agile.

Remember that small, special-purpose is more agile than big, general-purpose.
-----------------------------------------------------------------------------

Google is famously good at building huge pieces of infrastructure that
solve big, important problems. GFS & Colossus for file storage,
Bigtable, Blobstore and Spanner for structured data storage, Caffeine
for document storage and indexing.

But, when faced with a new problem or new requirements, projects are
expected to pidgeon-hole their needs into one of these systems, or be
chastised for "doing it wrong". Additionally, when your application
needs inevitably don't fit or grow out of existing infrastructure
capabilities, requests for improvement or enhancement are lost in the
noise. This means small teams are crippled by the lack of agility of
these monstrous systems.

Google's engineers need to think & act like startup founders. Only
develop what's absolutely necessary to get your job done. Simplicity
counts. Complex systems are hard to learn, debug, and maintain. Keep it
small and focused.

Implement an in-house incubator.
--------------------------------

Do this right now.  When a current employee comes to you and submits
their resignation letter, and says they're joining a startup, you should
immediately respond with "Oh! Well, let me tell you about our in-house
startup incubator..."

Put smart people together in a room, let them think freely about
products and infrastructure, and good things will come of it.  In fact,
I might argue that every Staff level engineer or higher should "go on
sabbatical" to the in-house incubator for a period of a minimum of 6
months.   Rotate people in & out, and let them bring their incubator
learnings back on to the main campus.  Have one incubator per geography,
at a minimum, possibly more.  Let people choose their best
freinds/coworkers, and go off and do something great for 6 months.  No
managers, no meetings, no supervision.

Make it very clear that good, small ideas matter.
-------------------------------------------------

This is *so* important.  One of the things I heard over and over was "If
your product isn't a billion-dollar idea, then it's not worth Google's
time."  This message sucks.  What you're saying is "your great idea that
might make millions per year is less important than a small tweak to ads
or search".  Even if it's true, you need to foster innovation of much
lesser initial impact.

Google acquisitions of companies in the \$5-50mm range means that at
some level, small businesses *are* valued.  Make this very clear.  It
sucks to have someone say "your \$5mm idea isn't big enough" on the one
hand, and then watch Google buy up companies for \$5mm each. This is bad
precedent.

Eliminate internal language and framework cronyism.
---------------------------------------------------

By this, I mean: "Stop forcing people to do things The Google Way".  
There were several times where I had seen "unGoogly" system desgins get
shot down because they didn't use Bigtable, GFS, Colossus, Spanner,
MegaStore, BlobStore, or any of the other internal systems.

For example, languages like Python are shunned upon because they're "too
slow for web frontends".  Let teams use whatever tools and languages
they want, and are most efficient in. Don't pass judgement on
infrastructure, pass judgement on *Products*.  If someone launches a
great system based on Oracle and a bunch of Perl CGI scripts running on
Sun Sparc 5's, then you should praise them. If they're crushed under
load, then praise them even more for their success.

Engineers at Google spend huge amounts of their time being forced to
prematurely optimize their backend and frontend infrastructure.  Most of
the time, this benefits no one, as small products never get big enough
to need such heavyweight systems, and are bogged down with the cost of
multiple redundancy, and by using poorly behaved internal APIs that
don't meet direct product needs.

Make a general purpose cloud for internal use.
----------------------------------------------

Amazon EC2 is a better ecosystem for fast iteration and innovation than
Google's internal cluster management system.  EC2 gives me reliability,
and an easy way to start and stop entire services, not just individual
jobs.  Long-running processes and open source code are embraced by EC2,
running a replicated sharded MongoDB instance on EC2 is almost a breeze.
 Google should focus on making a system that works within the entire
Open Source ecosystem.

Acknowledge that 20% time is a lie.
-----------------------------------

Virtually no one I knew in my entire career there had an effective use
of 20% time.  There are stories about how some products are launched
exclusively via 20% time, and I've seen people use their 20% time to
effectively search for a new internal position, but for the vast
majority of engineers, 20% time is a myth.

I think it's a great idea, and it needs to be made effective.  1 day per
week isn't reasonable (you can't get enough done in just one day and
it's hard to carry momentum).  1 week per month would be great, but
doesn't do justice to your "main" project.  Something needs to budge
here, and engineers need to be encouraged to take large amounts of time
exploring new ideas and new directions.  Really fostering internal tools
and collaboration might be the right answer.  I'm not sure, maybe they
should just give up on it and give everyone a 20% raise.  Oh wait, they
did that already.

Repeat your mistakes.
---------------------

Engineers learn by doing, and learn by making mistakes.  Having rules
about system design puts unnecessary constraints on thinking and
products.  Having internal lore around things like "Google will never
let another thing like Orkut ever happen again" is blatantly wrong.
 Orkut was (and still is) a huge success, period.  None of the
infrastructure stuff matters.  Even recent mistakes (Wave, etc.) should
be praised and engineers should be encouraged to repeat those mistakes.

"Google Scale" is a myth.
-------------------------

Yes, I said it.

Google Search (the product) requires vast resources.  Almost nothing
else does, and yet is constrained and forced to run "at Google scale"
when it's completely unnecessary.

Giving engineers the freedom to think & design out of the box with
respect to infrastructure and systems means you'll be more efficient in
the long run.  Providing reliable platforms and data centers means
you'll have less redundancy, and be more efficient.

Given that a single machine can easily have 64GB of RAM, 10TB of disk,
and 8 CPUs, it's amazing that any product launch needs more than just a
couple of that class of machine.  Let engineers push the boundaries,
make mistakes, and run on the edge.

A small system that falls down under load is a huge success

A large system that's wasting resources and has only a few users is a
huge failure.
