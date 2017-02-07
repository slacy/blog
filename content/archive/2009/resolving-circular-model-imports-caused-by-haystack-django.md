Title: Resolving circular model imports caused by Haystack  Django
Date: 2009-11-19 11:22
Author: slacy
Category: General
Tags: circular import, django, haystack, python
Status: published

So, in converting our search to Haystack, I've found that some of my
standalone maintainence scripts no longer work.  They had an import
error trying to import some of the models.

The issue is that I've updated my models.py with some Haystack code. 
The code at hand is in the save() method of the model object, and
basically looks like this:

``` {.python name="code"}
[... other misc django imports above ... ]
from haystack import site

class MyModel(models.Model):
    [ ... fields of model, etc. ... ]
    def save(self, force_insert=False, force_update=False):
        super(MyModel, self).save(force_insert, force_update)
        if self.is_child_node():
            site.get_index(MyModel).update_object(self.parent)
```

The problem was that if I had a standalone script that said:

``` {.python name="code"}
from mysite.models import MyModel
```

Then I would get a circular import, because the "from haystack import
site" line ends up working it's way over to search\_sites.py that says
"haystack.autodiscover()" which ends up looking for all
search\_indexes.py, and one of these says "from myapp.models import
MyModel".  So, there's your circular reference.

The solution to this problem is to put a haystack import at the top of
my standalone script, before I import my model.  Adding "from haystack
import site" works, even though the code therein doesn't actually use
haystack.

I think the haystack code here:

    /usr/lib/python2.5/site-packages/haystack/__init__.py in autodiscover()
     88         # Step 3: import the app's search_index file. If this has errors we want them
     89         # to bubble up.
    ---> 90         __import__("%s.search_indexes" % app)
     91
     92 # Make sure the site gets loaded.

Should have a try/except block around it, and then this extra import
wouldn't be necessary. The funny thing is that looking at the source,
all the other imports there catch ImportError and don't pass it back up,
but this case does.

I was able to simply debug this in ipython my running "from myapp.models
import MyModel" and debugging, per above.  It was fairly clear that it's
a circular import.  I'm surprised (in general) that Python doesn't
handle circular imports any more gracefully than saying "&lt;type
'exceptions.ImportError'&gt;: cannot import name MyModel"
