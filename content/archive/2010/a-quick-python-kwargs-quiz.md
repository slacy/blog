Title: A quick Python kwargs quiz
Date: 2010-07-12 13:12
Author: slacy
Category: General
Status: published

Here's some sample code:

    def printargs(**kwargs):
      print kwargs

    printargs(foo='bar')
    printargs(**dict(foo='bar'))
    printargs(**{'foo':'bar'})

Today's question is:  In what way are the 3 bottom lines different with
respect to their behavior?
