Title: How to set session variables in Django unit tests.
Date: 2012-01-12 16:24
Author: slacy
Category: General
Tags: django, linux, python, Web
Status: published

This was super non-obvious, and I lifted code from a couple of different
places.

If you've got Django view code that gets & sets session values, you'll
want to test it properly, and the standard "self.client" from Django's
TestCase doesn't really give you a usable session.  So, here's the
method I'm using:

    def stuff_session(client, dictionary):
        """Given a client (self.client in a unit test TestCase) set the session to the contents of
        the dictionary given"""
        from django.conf import settings
        from django.utils.importlib import import_module
        engine = import_module(settings.SESSION_ENGINE)
        store = engine.SessionStore()
        store.save()  # we need to make load() work, or the cookie isworthless
        client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key
        session = client.session
        session.update(dictionary)
        session.save()
        # and now remember to re-login!

So, in my setUp() methods, I just call stuff\_session(self.client,
{'key': 'value'}) and it all works out great.
