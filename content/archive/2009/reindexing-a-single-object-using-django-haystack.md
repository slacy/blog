Title: Reindexing a single object using Django  Haystack
Date: 2009-11-18 17:22
Author: slacy
Category: General
Status: published

If you're using Django & Haystack, and you want to reindex a single
object, you would dothe following:

        from haystack import site
        site.get_index(YourModel).update_object(your_instance)

This is useful if you have objects that are related in some kind of
hierarchy, but you store them flattened in Haystack.  So, when you
update one of the leaf objects, you would need to reindex the root
object, and thus, the code above.

BTW, I'm pretty annoyed that haystack used the term "site".  I would
have preferred it to be something more haystack-specific.  Maybe
"haystack\_engine" or something?  I can always say "from haystack import
site as haystack\_engine" but that style seems to lead into a world of
incompatible code.
