Title: methodpickle: A Python library for pickling function invocations.
Date: 2011-02-11 15:37
Author: slacy
Category: General
Tags: celery, mongodb, python, queue
Status: published

Have you ever wanted to say "I'd like to call this function, but later"?

I've seen people using [Celery](http://celeryproject.org) for this
purpose, and it's very well respected, but the setup is far from easy.
 It has several fairly large dependencies, including RabbitMQ, or you
have to use one of their "ghetto queue" solutions.  I tried the ghetto
queue for MongoDB, and it furiously polled the database.  That's not
cool.

I was also finding that it had somewhat unpredictable behavior, and I
actually wanted something more simple.  I wanted to use a flow like:

-   Take any arbitrary function or method call, and "pickle it"
-   Stick the pickled calls into a database (mongodb in my case)
-   Pull out items from the DB and execute them.

Simple polling met my needs, and writing a queue in MongoDB is actually
pretty simple, since they have atomic test-and-set primitives.

So, the only missing component was something that let me pickle method
calls, and thus, I wrote a simple library to do it.  It's called
[methodpickle](http://github.com/slacy/methodpickle) and it's on github.
 Here's a brief example of what it lets you do:

    from methodpickle.defer import defer 

    def factorial(x): 
        if x == 1: return 1
        return x * factorial(x-1)

    if __name__ == '__main__':
        deferred = defer(factorial, 123)
        deferred_str = pickle.dumps(deferred)

        # Now, take deferred_str, store it to a db, read it back again, whatever. 
        call = pickle.loads(deferred_str)
        print call.run()

And, it even works with class methods, as long as 'self' is pickle-able.
Cool!
