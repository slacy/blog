Title: Identity mapper  reducer for MongoDB
Date: 2010-12-01 17:02
Author: slacy
Category: General
Tags: mapreduce, mongodb, pymongo, python
Status: published

This code for doing an identity map & identity reduce in MongoDB.
Mostly, this is useful for debugging and testing. This code is written
in Python, and using the pymongo driver.

    from pymongo.code import Code

    connection = pymongo.Connection()
    # You'll need to get your DB and your Collection here.   
    # From here on, we assume 'collection' is the what
    # you're running the mapreduce against. 

    identity_mapper = Code(
    """
      function() {
        emit(this._id, this);
      }
    """)

    identity_reducer = Code(
    """
      function(key, values) {
        return(values[0]);
      }
    """)

    result = collection.map_reduce(identity_mapper, identity_reducer)
    for i in result.find():
        print i
