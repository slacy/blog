Title: MongoDB: Doing a findAndModify with a limit in Python. 
Date: 2010-12-16 15:45
Author: slacy
Category: General
Status: published

It's not really documented very well, but setting a limit on the mongodb
command findAndModify actually works the way you would expect. You can't
call limit(1), but you can programmaticly set a limit parameter.

I'm using pymongo, and I don't have the version of pymongo with the
builtin find\_and\_modify method on collections yet, so I have to do it
manually.  The example code looks like this:

    def get_and_update():
        item = db.command(
            'findAndModify',   # command
            'coll',            # collection name
            # args to findAndModify below
            allowable_errors=[no_obj_error],
            query={'some_param': some_value},
            update={'other_param': other_value},
            upsert=False,
            limit=1)

        if 'value' in item:
            return item['value']
        return None
