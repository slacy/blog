Title: How do you make change?
Date: 2008-01-30 15:31
Author: slacy
Category: General
Tags: c++, coinage, denominations
Status: published

I've always been fascinated by the denominations of money, and
specifically, which coin values different countries use. Here in the US,
we use the set of values {1,5,10,25}, and I've often wondered whether
this is the best set of values. The question is: How do you figure out
what 'best' is?

Previously, I wrote a program that, given a set like {1,5,10,25},
counted the number of coins needed to make every possible value between
1 and 99 cents. I thought that number would be a pretty good indication
of how good the set of values was. The best set for 4 coins was a tie
between {1, 5, 18, 29} and {1, 5, 18, 25}.

As I discussed this solution with my friends (long ago) they all
mentioned that this wasn't a very realistic or good measure of how well
a set of values performs in the real world. It was suggested that a
better metric would be to model real-world transactions, and the number
of coins needed.

So, I set off to write a new program. The algorithm would model a single
buyer and a number of 'purchases' between 0 and 99 cents. Then, I could
calculate the average number of coins in the virtual 'coin pocket'. This
average pocket size would be my measure for the 'best' set of coin
values. The pocket would contain an infinite number of dollar bills, so
it never runs out of money, and the bills aren't counted as 'coinage'.

But, an interesting question came into play: When making a purchase, the
program needs to decide how much to pay for the item, given the contents
of the pocket. I started off by implementing a fairly naive algorithm
that ended up preferring to use large coins. After looking at the
results, I found that the pocket was accumulating as many as 18 pennies
before spending them. Although this might be how I personally work, it
didn't seem to be how most people would do it, and it didn't seem like a
good model for the program. So, I pose the question to you, the reader!

If you've got 4 pennies and a bunch of dollar bills, do you usually put
down pennies to 'round up' your change? For example, would you pay
\$1.03 for an item that cost \$0.38?

Would you put down extra nickels and dimes to 'round up' to dimes and
quarters? How often? For example, would you pay \$1.08 or for an item
that cost \$0.38 to get back \$0.70? This case is particularly
interesting because you give up 4 coins (3 pennies and a nickel) to get
back 4 higher valued coins (2 quarters and 2 dimes). There's no
reduction in the coin count, but it 'feels right' to get higher valued
coins back.

How about \$1.13 to pay for \$0.38? In this case, you would get back
exactly \$0.75. What if the \$0.13 was made up of 13 pennies? Would you
still do it?

How about paying \$1.63 for \$0.88 to get back exactly \$0.75? What if
the \$1.63 were made up of an odd assortment of coins, like 5 quarters,
2 dimes, 2 nickels and 8 pennies? Would you still do it?

At some point (like in the previous example) we start to trade off our
own time needed to add and compose our purchase amount for the
convenience of just ending the transaction. I think we also consider the
cashier's time and patience, since they may not tolerate waiting as we
ponder and compose the 'perfect' amount. Not to mention the other people
in line behind us!

I think the solution here is going to be a rule-based system, with
things like:

If you have enough pennies to round up to the nearest \$0.05, then do
it.  
If you have enough dimes & nickels to round up to the nearest \$0.25,
then do it.  
Don't overpay for the item by more than \$0.50.  
Don't give the cashier more than N coins. (whats N?)

I've started to code up some of this stuff in C++, but I'm kind of
stymied by trying to come up with a good generalized solution to this
problem, especially since the rules conflict and overlap. (And note that
any solution has to work for arbitrary values of coins, like
{1,4,12,24})

How would you go about tackling this problem?
