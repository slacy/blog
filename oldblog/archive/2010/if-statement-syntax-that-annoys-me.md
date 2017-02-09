Title: if-statement syntax that annoys me.
Date: 2010-06-18 13:50
Author: slacy
Category: General
Status: published

Sometimes people like to write their if statements like this:

    result = "foo"
    if condition:
      result = "bar"

I assume they're thinking that it's faster to not have an else clasuse
or something, but in fact, the double assignment that occurs is much
slower than the else clause, which is basically free. I'd much rather
see:

    if condition:
      result = "bar"
    else:
      result = "foo"

Is there any valid reason to prefer the first syntax over the second?
