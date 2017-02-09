Title: Using Django's widthratio template tag for multiplication  division.
Date: 2010-07-30 13:46
Author: slacy
Category: General
Status: published

I find it a bit odd that Django has a template filter for adding values,
but none for multiplication and division. It's fairly straightforward to
add your own math tags or filters, but why bother if you can use the
built-in one for what you need?

Take a closer look at the widthratio template tag. Given {% widthratio a
b c %} it computes (a/b)\*c

So, if you want to do multiplication, all you have to do is pass b=1,
and the result will be a\*c.

Of course, you can do division by passing c=1. (a=1 would also work, but
has possible rounding side effects)

Note: The results are rounded to an integer before returning, so this
may have marginal utility for many cases.

So, in summary:

to compute A\*B: {% widthratio A 1 B %}  
to compute A/B: {% widthratio A B 1 %}

And, since add is a filter and not a tag, you can always to crazy stuff
like:

compute A\^2: {% widthratio A 1 A %}  
compute (A+B)\^2: {% widthratio A|add:B 1 A|add:B %}  
compute (A+B) \* (C+D): {% widthratio A|add:B 1 C|add:D %}
