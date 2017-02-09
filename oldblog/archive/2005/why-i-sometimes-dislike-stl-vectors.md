Title: Why I sometimes dislike STL <vector>s.
Date: 2005-12-15 21:07
Author: slacy
Category: General
Status: published

In general, I like using
[STL](http://www.sgi.com/tech/stl/table_of_contents.html) classes,
because in general, they make life easier. But, for the last few days,
they've been making my life a living hell. I want to do something like
this:

` void RemoveEvenElements(vector<int> *elements) {   vector<int>::iterator iter;   for (iter = elements->begin(); iter != elements->end(); ++iter) {     if (*iter % 2 == 0) elements->erase(iter);   } }`

But of course, that code crashes horribly because of this one tiny
"detail" in the STL description:

> inserting or deleting an element in the middle of a vector invalidates
> all iterators that point to elements following the insertion or
> deletion point

So, I'm left with a shitty N\^2 algorithm to do something that should be
O(N), or I have to use some obscure
[STL](http://www.sgi.com/tech/stl/table_of_contents.html) construct,
like [transform](http://www.sgi.com/tech/stl/transform.html)
