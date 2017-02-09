Title: A quick lesson in how to subvert the democratic process.
Date: 2011-07-27 11:13
Author: slacy
Category: General
Status: published

Imagine that you wanted to subvert an election.  What do I mean by
"subvert"?  I mean, that you wanted everyone involved in the process to
think that it was a fair majority, but in fact, it was not.  Let's go
through some options on how to make this happen.

Here are some quick parameters for this thought experiment:

-   There will be exactly 9 people voting.
-   Each person gets to vote for either Option A, or Option B. These
    will simply be called "A" and "B".
-   Each person must continue to believe that their vote was counted,
    and was contributing to a majority of votes.
-   5 of the people will vote for "A"
-   4 of the people will vote for "B"

Algorithm 1: Simple majority
----------------------------

Let's just count all 9 votes together.

-   Count 5 people voting for "A"
-   Count 4 people voting for "B"
-   5/9 = 55.5% of people voted for A.

**We declare the winner to be "A".**

Algorithm 2: Representative majority.
-------------------------------------

Let's divide the 9 people into 3 possible groups of 3 people each. Call
these groups "P", "Q", and "R".

The voting algorithm is as follows:

-   Each group of 3 voters cast their votes, and a majority winner of
    that group is declared.
-   Then, each group acts as a "Virtual voter" and a second election
    is held.  Each "virtual voter" (one for each Group) votes strictly
    according to the majority of the actual voters in that group.
-   Whichever Option gets at least a 2/3rd simple majority across
    virtual votes from P,Q & R is declared the winner.

There are a few different options for the outcomes of the sub-votes in
P,Q, and R, and it's worth showing them here:

### Algorithm 2, Possibility 1:

People are divided into groups and votes are cast in each group as
follows:

-   Group P: A, A, A  (Winner: A)
-   Group Q: A, A, B (Winner: A)
-   Group R: B, B, B (Winner: B)

**"A" is declared the winner.**

### Algorithm 2, Possibility 2:

People are divided into groups and votes are cast in each group as
follows:

-   Group P: A, A, B (Winner: A)
-   Group Q: A, A, B (Winner: A)
-   Group R: A, B, B (Winner: B)

**"A" is declared the winner.**

### Algorithm 2, Option 3:

People are divided into groups and votes are cast in each group as
follows:

-   Group P: A, A, A  (Winner: A)
-   Group Q: A, B, B  (Winner: B)
-   Group R: A, B, B  (Winner: B)

<span style="background: #FFFF00">**"B" is declared the winner.**</span>

Conclusion
----------

As you can see, the Group selection process opens up a loophole in the
voting, where 1 out of the 3 possible outcomes does not follow an actual
voter majority.

If, prior to the group selection process, we can somehow know which
voters are going to vote for A, and which for B, we can control or
modify that process (which is likely opaque to the individual voters) in
a way that influences the final outcome significantly in favor of B.

The election has been subverted, because each individual voter thinks "I
voted, and in my group, a majority consensus was reached, and this
directly contributed to the final majority outcome."  Voters are lulled
into thinking that their votes are "representative" of their group, and
that the final outcome is "representative" of the majority of all votes.

This is how congressional redistricting and the electoral college voting
process works.
