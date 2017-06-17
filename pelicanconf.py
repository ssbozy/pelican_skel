#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'SB'
SITENAME = u'Pelican 101'
SITEURL = ''
THEME = 'bootstrap'
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_CATEGORY = 'General'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 10
DEFAULT_DATE_FORMAT = '%a %d %B %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#PATHS FOR CONTENT
STATIC_PATHS = ['images','extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'))

#Social
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'))