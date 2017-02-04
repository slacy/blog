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

THEME = 'slacy-medius'

# Social widget
SOCIAL = (('Twitter @sklacy', 'https://twitter.com/sklacy'),
          ('Github', 'https://github.com/slacy'),)
GITHUB_URL = "https://github.com/slacy"
TWITTER_USERNAME = "sklacy"
GOOGLE_ANALYTICS = "UA-85612-4"

STATIC_PATHS = ['images',]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.admonition': {}
    },
    'output_format': 'html5',

}

MEDIUS_CATEGORIES = {
    'TensorFlow From The Ground Up': {
        'description': '',
        'thumbnail': 'https://slacy.github.io/blog/images/tf_logo.png',
    }
}


MEDIUS_AUTHORS = {
    'slacy': {
        'description': """                    """,
        'cover': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Milky_Way_Arch.jpg/1920px-Milky_Way_Arch.jpg',
        'image': 'https://slacy.github.io/blog/images/ygg.png',
        'links': (('github', 'https://github.com/slacy'),
                  ('twitter-square', 'https://twitter.com/sklacy')),
    }
}



PLUGIN_PATHS = ["plugins"]
PLUGINS = ["render_math"]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
