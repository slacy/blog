Title: pprinting the Django context object
Date: 2009-10-22 14:45
Author: slacy
Category: General
Tags: context, django, pprint, python
Status: published

This was non-obvious to me for quite some time, and I tried several
different approaches before settling on this one:

If you would like to pprint your Django Context (or RequestContext)
object from within a template itself, there are several approaches you
can take.  The easiest way I found is to say:

``` {.python name="code"}
context['context'] = context
```

in your view(s) that you want to display, and then in the template, you
can say:

``` {.html name="code"}
{% for c in context %}
<p>{{ c|pprint }}</p>
{% endfor %}
```

Or something along those lines.

The reason that the simple {{ context|pprint }} doesn't output what you
expect is because of the \_\_repr\_\_() method on the Context() object
in Django.  It constructs a big huge string for you, when what you want
is to let pprint do all the heavy lifting and indentation.
