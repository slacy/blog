#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Steve Lacy'
SITENAME = u"Slacy's Blog"
SITEURL = 'https://slacy.github.io/blog'

PATH = 'content'
OUTPUT_PATH = 'docs'

TIMEZONE = 'America/Los_Angeles'

TYPOGRIFY = True 

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

THEME = 'medius' 

# Social widget
SOCIAL = (('Twitter @sklacy', 'https://twitter.com/sklacy'),
          ('Github', 'https://github.com/slacy'),)


PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["render_math"]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
