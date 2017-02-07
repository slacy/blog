Title: Both production  development settings using zc.buildout  djangorecipe
Date: 2010-10-01 14:56
Author: slacy
Category: General
Tags: development, django, production, python, recipe, zc.buildout
Status: published

It took me a while to figure this out, so I'm writing it down.

What I wanted was to have my django.wsgi script use the production
settings and to have bin/django use the development settings.  Sounds
easy, right?  It's not obvious what the right way to accomplish this is,
but here's what I've come up with for my zc.buildout script:

    [buildout]
    parts = django djangoprod

    [django]
    recipe = djangorecipe
    version = 1.2
    settings = development
    project = project 

    [djangoprod]
    recipe = djangorecipe
    version = ${django:version}
    settings = production
    wsgi = true
    project = ${django:project}

By specifying 2 different djangorecipe based rules, we can create both
bin/django and bin/djangoprod.wsgi.  djangoprod.wsgi will use production
settings, and bin/django will use development settings, which is in
general, what you want for a develop & deploy buildout script.
