Title: An extremely simple config pattern for Python
Date: 2011-03-03 10:44
Author: slacy
Category: General
Tags: configs, pattern, python, python config, simple config, web framework
Status: published

So, you're developing a Python application.  
And, you have needs for "production" versus "development" configs.

If you're using a web framework, you might have some support for doing
this, but what about your other modules that you'd like to configure in
a similar way?

What you sort of want to be able to say, anywhere, is something like
this:

    import config

    if config.MODULE['parameter'] == 'value': 
        # do something 
    else: 
        # do something else

And, you want "import config" to automatically decide (via some means)
if it's in production or development.

Great, here's a really simple pattern for you.

Make a directory named "config" put it somewhere on your python import
path. (It's okay if this is app.config or some\_module.config, whatever
you want.) Make the \_\_init\_\_ look like this:

    class Config(object): 
        pass

    if some_condition: 
        from config.production import ProductionConfig 
        config = ProductionConfig
    else:
        config = DevelopmentConfig

You need to write some\_condition yourself. You'll probably do something
like check for existance of a file, check the hostname, look at an
environment variable, whatever.

Then, create config/production.py and config/development.py and make
them look pretty much like this:

    from config import Config 
    class DevelopmentConfig(Config): 
        MODULE = { 'param': 'value' }
        OTHER_MODULE = { 'other_param': 'other_value' }
        # etc.

Make sure that production and development configs both specify the same
arguments. If you have shared things you want to configure, then you can
make "base.py" or "shared.py" and derive from that.

Happy hacking!
