#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Ignacio Vergara Kausel"
SITENAME = "On data, programming, and technology"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "en"

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

STATIC_PATHS = ["images", "extra"]

# SITELOGO = 'images/terminal.svg'
# FAVICON = 'images/favicon.ico'


SUMMARY_MAX_LENGTH = None
TYPOGRIFY = True

# Social widget
SOCIAL = (
    ("twitter", "http://twitter.com/ivergarak"),
    ("linkedin", "https://www.linkedin.com/in/ignaciovergara/"),
    ("github", "http://github.com/ivergara"),
    (
        "stackoverflow",
        "https://stackoverflow.com/users/2244081/ignacio-vergara-kausel",
        "stack-overflow",
    ),
)

DEFAULT_PAGINATION = 10

THEME = "/home/ignacio/Documents/pelican-themes/pelican-bootstrap3"

BOOTSTRAP_THEME = "cosmo"

PLUGIN_PATHS = ["/home/ignacio/Documents/pelican-plugins"]
PLUGINS = ["i18n_subsites", "ipynb2pelican", "series"]
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Options
DISPLAY_SERIES_ON_SIDEBAR = True
USE_OPEN_GRAPH = False
CC_LICENSE = "CC-BY-NC-SA"

PYGMENTS_STYLE = "manni"
MARKUP = ("md", "ipynb")
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = True
IGNORE_FILES = [".ipynb_checkpoints"]

DEFAULT_METADATA = {"status": "draft"}


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.tables': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}