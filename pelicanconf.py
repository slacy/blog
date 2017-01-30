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
LINKS = ()

THEME = 'medius'

# Social widget
SOCIAL = (('Twitter @sklacy', 'https://twitter.com/sklacy'),
          ('Github', 'https://github.com/slacy'),)
GITHUB_URL = "https://github.com/slacy"
TWITTER_USERNAME = "sklacy"

STATIC_PATHS = ['images',]

MEDIUS_CATEGORIES = {
    'TensorFlow From The Ground Up': {
        'description': '',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/NGC_3923_Elliptical_Shell_Galaxy.jpg/220px-NGC_3923_Elliptical_Shell_Galaxy.jpg'
    }
}


MEDIUS_AUTHORS = {
    'slacy': {
        'description': """                    """,
        'cover': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Milky_Way_Arch.jpg/1920px-Milky_Way_Arch.jpg',
        'image': '/images/ygg.png',
        'links': (('github', 'https://github.com/slacy'),
                  ('twitter-square', 'https://twitter.com/sklacy')),
    }
}



PLUGIN_PATHS = ["plugins"]
PLUGINS = ["render_math"]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
