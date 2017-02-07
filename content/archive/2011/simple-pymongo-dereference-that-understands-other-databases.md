Title: Simple pymongo dereference that understands other databases.
Date: 2011-01-05 11:38
Author: slacy
Category: General
Tags: dereference, mongodb, pymongo, python
Status: published

Here's the code for a Python dereference function using pymongo that
understands cross-database references properly:

    import pymongo

    def dereference(ref):
        dbname = ref.database
        collname = ref.collection
        print ref
        return pymongo.Connection()[dbname][collname].find_one({'_id': ref.id})
