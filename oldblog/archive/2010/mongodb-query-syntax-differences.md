Title: MongoDB nested query syntax differences?
Date: 2010-12-16 16:09
Author: slacy
Category: General
Status: published

Can someone please explain the following behavior:

    use test
    switched to db test
    > db.foo.drop()
    true
    > db.foo.insert({x:{y:{z:1}}})
    > db.foo.insert({x:{y:{z:1, a:1}}})
    > db.foo.insert({x:{y:{z:1}, a:1}})
    > db.foo.insert({x:{y:{z:1}}, a:1})
    >
    > db.foo.find({x:{y:{z:1}}})
    { "_id" : ObjectId("4d0aad7b9132e04ab032e1c0"),
      "x" : { "y" : { "z" : 1 } } }
    { "_id" : ObjectId("4d0aad7b9132e04ab032e1c3"),
      "x" : { "y" : { "z" : 1 } }, "a" : 1 }
    >
    > db.foo.find({'x.y.z':1})
    { "_id" : ObjectId("4d0aad7b9132e04ab032e1c0"),
      "x" : { "y" : { "z" : 1 } } }
    { "_id" : ObjectId("4d0aad7b9132e04ab032e1c1"),
      "x" : { "y" : { "z" : 1, "a" : 1 } } }
    { "_id" : ObjectId("4d0aad7b9132e04ab032e1c2"),
      "x" : { "y" : { "z" : 1 }, "a" : 1 } }
    { "_id" : ObjectId("4d0aad7b9132e04ab032e1c3"),
      "x" : { "y" : { "z" : 1 } }, "a" : 1 }

Note that when the "a" field is present, then the second query doesn't
return any results. Why is this?
