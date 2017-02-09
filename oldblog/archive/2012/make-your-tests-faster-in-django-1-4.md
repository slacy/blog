Title: Make your tests 7x faster in Django 1.4
Date: 2012-04-26 16:14
Author: slacy
Category: General
Status: published

In Django 1.4, the default password hasher has been switched to the
extremely secure PBKDF2 algorithm.

But, each encrypt and decrypt using PBKDF2 can take a pretty long time
(on my system, about 150ms for each hashing, which happens twice per
unit test that I'm writing). For your test cases, (that create users and
log them in & out, probably) this extra security is probably pointless,
and runtime is paramount.

So, create a custom settings.py for your test cases, and set the
PASSWORD\_HASHERS setting to exclude PBKDF2. You can also use this
technique to setup an inmemory sqlite2 database as your backend, which
also speeds things up quite a bit. Here's a snippet from my
settings\_test.p:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Not used with sqlite3.
            'PORT': '',                      # Not used with sqlite3.
        }
    }

    PASSWORD_HASHERS = (
        # 'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        # 'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        # 'django.contrib.auth.hashers.BCryptPasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
        'django.contrib.auth.hashers.MD5PasswordHasher',
        # 'django.contrib.auth.hashers.CryptPasswordHasher',
    )

Note that you have to have the sha1 algorithm enabled to allow the
django.contrib.auth tests work. You can use different settings for test
either get this by something like:

DJANGO\_SETTINGS\_MODULE='yourapp.settings\_test' django-admin.py test

(probably putting this in a Makefile or shell alias) or I've also seen
people put this at the top of their default settings:

    if 'test' in sys.argv:
        from settings_test import *

These 2 changes took my test run time from 15.5 seconds down to 2.0
seconds, an **improvement of about 7x**! Woot!
