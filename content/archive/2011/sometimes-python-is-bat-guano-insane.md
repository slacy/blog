Title: Sometimes Python is bat-guano insane 
Date: 2011-02-17 11:17
Author: slacy
Category: General
Tags: dumps, loads, pickle, python
Status: published

Try this on for size:

    import pickle

    d = {'a': 1}

    s1 = pickle.dumps(d)
    s2 = unicode(s1)

    assert(s1 == s2)

    d1 = pickle.loads(s1)
    d2 = pickle.loads(s2)

    assert(d1 == d2)

So, what do you think happens here? Are s1 and s2 equal? Are d1 and d2?

Well, hold on to your hats. The code doesn't even execute through
pickle.loads(s2). It throws this crazy error:

    Traceback (most recent call last):
      File "/tmp/test.py", line 11, in <module>
        d2 = pickle.loads(s2)
      File "/usr/lib/python2.6/pickle.py", line 1374, in loads
        return Unpickler(file).load()
      File "/usr/lib/python2.6/pickle.py", line 858, in load
        dispatch[key](self)
    KeyError: '\x00'

So, how's that for totally insane unpredictable behavior?
