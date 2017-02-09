Title: A simple pattern for short URLs for objects in MongoDB.
Date: 2011-02-23 14:07
Author: slacy
Category: General
Tags: mongodb, short url, shortener
Status: published

So, you need short URLs for your pages, and pages are objects in your
MongoDB database. How do you generate these short ids?

The pattern I'm using is quite simple, but requires that you create a
unique index on a field called "short\_id."   Since I'm using
[minimongo](http://github.com/slacy/minimongo), it's easy to declare
these Indexes programatically, and I can override the save() method on
an object to do "extra stuff", like set the short\_id and retry if
there's a conflict.  Here's how the code came out:

    import random
    import string
    from pymongo.errors import DuplicateKeyError
    from minimongo import Model, Index, MongoCollection

    class TestModel(Model):
        mongo = MongoCollection(database='test', 
                                collection='test_model')
        indices = [Index('short_id', unique=True)]

        def save(self, *args, **kwargs):
            short_id_length = 3
            retry_count = 0
            short_chars = string.letters + string.digits
            if hasattr(self, 'short_id'):
                return super(Model, self).save(*args, **kwargs)
            while True:
                try:
                    self.short_id = ''.join(
                        [random.choice(short_chars) for x in 
                         xrange(short_id_length)])
                    kwargs['safe'] = True
                    super(Model, self).save(*args, **kwargs)
                    return
                except DuplicateKeyError, e:
                    retry_count += 1
                    if retry_count > 3:
                        short_id_length += 1
                        retry_count = 0

Then, when I create a TestModel and save it, the short\_id field is
filled in automatically, and I can use that in my URL generation.

It's this exact kind of use case that made me want to write
[minimongo](http://github.com/slacy/minimongo).  Simple method overrides
for behavior like this can be really powerful.  Also note how the unique
index on the short\_id field is automatically created.  Sweet!
