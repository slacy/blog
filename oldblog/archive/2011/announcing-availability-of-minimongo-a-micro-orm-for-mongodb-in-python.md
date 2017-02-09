Title: Announcing availability of Minimongo, a Micro-ORM for MongoDB in Python
Date: 2011-01-10 18:19
Author: slacy
Category: General
Tags: minimongo, mongodb, nosql, orm, python
Status: published

[Minimongo](http://github.com/slacy/minimongo) is an extremely
lightweight, schemaless ORM for Python &
[MongoDB](http://www.mongodb.org/).

-   Minimongo delegates queries directly
    to [pymongo](http://api.mongodb.org/python/1.9%2B/index.html).
-   Minimongo is schemaless.  (No Schema validation at all.)
-   Minimongo manages database connections for you.
-   Minimongo offers many other conveniences on top of pymongo, but
    preserves the raw spirit and feel of pymongo.

I've been using MongoDB for my latest projects, and I absolutely love
it, and the freedom of application design it inspires.

But, I wasn't happy with the "ORM" solutions that currently existed for
MongoDB.  I
investigated [MongoEngine](http://mongoengine.org/docs/v0.4/) and
[MongoKit](http://bytebucket.org/namlook/mongokit/wiki/html/introduction.html),
but they both impart way too much structure for my tastes, and operate
too much like a traditional SQL ORM.  Because I'm developing from
scratch, I have no need for a complex ORM.  In addition, they both have
Schema validation, which is something that I'm trying to avoid in my
development, since I'm bringing in data from many external APIs into a
single object, and I know I'm going to be extending these in the future
(more sources, more unstructured data).

So, I decided to write my own ORM for Python & MongoDB.  ORM is too
strong of a word, since my goals were:

-   Keep the native pymongo query syntax.
-   No schema validation.
-   Map dict-based results from pymongo in a Python object.
-   Provide a direct interface layer to pymongo.
-   Manage pymongo connections automatically.
-   Provide helper functions for DBRef usage.
-   Provide helper functions for managing database & collection names.

If you're interested in this kind of stuff, *please* check out my
[Minimongo](http://github.com/slacy/minimongo) repository and let me
know what you think.
