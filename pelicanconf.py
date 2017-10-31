#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ignacio Vergara Kausel'
SITENAME = 'On data, programming, and technology'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (
#     ('Pelican', 'http://getpelican.com/'),
#     ('Python.org', 'http://python.org/'),
#     ('Jinja2', 'http://jinja.pocoo.org/'),
# )

# Social widget
SOCIAL = (
    ('twitter', 'http://twitter.com/ivergarak'),
    ('linkedin', 'https://www.linkedin.com/in/ignaciovergara/'),
    ('github', 'http://github.com/ivergara'),
    ('stackoverflow',
     'https://stackoverflow.com/users/2244081/ignacio-vergara-kausel',
     'stack-overflow'),
)

DEFAULT_PAGINATION = 10

THEME = '/home/ignacio/Documents/pelican-themes/pelican-bootstrap3'

BOOTSTRAP_THEME = 'paper'

PLUGIN_PATHS = ['/home/ignacio/Documents/pelican-plugins']
PLUGINS = ['i18n_subsites', 'ipynb2pelican']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Options

PYGMENTS_STYLE = 'solarizedlight'
MARKUP = ('md', 'ipynb')
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = True
IGNORE_FILES = ['.ipynb_checkpoints']

DEFAULT_METADATA = {
    'status': 'draft',
}
