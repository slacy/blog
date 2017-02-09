Title: C++ weirdness
Date: 2005-05-03 18:49
Author: slacy
Category: Linux Stuff
Status: published

Think about this:

`static const int a = 5; static const int b = '6'; static const int c = "7"[0];`{lang="cpp"}

and then, think about this code:

`printf("%d %d %d\n", a, b, c); `{lang="cpp"}

And then, think about this code:

</code>`switch(value) {     case a: printf("A!"); break;     case b: printf("B!"); break;     case c: printf("C!"); break; }`

You should try typing this into your compiler, and see what happens, and
try to figure out why. I'll give you a hint: One of the 3 things above
doesn't compile, and the others do. I think I know why, and I think its
pretty bogus.
