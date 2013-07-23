#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Omwah'
SITENAME = u'SGVHAK'
SITESUBTITLE = 'San Gabriel Valley'
SITESUBSUBTITLE = 'Hardware Hackers Group'
SITELOGO = "/static/images/logo_01_cropped.png"
SITEURL = ''

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = "theme/sundown"

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = (['images'])

FILES_TO_COPY = (("favicon.png", "favicon.png"), ("CNAME","CNAME"),)
