# -*- coding: utf-8 -*-

BOT_NAME = 'brooks'

SPIDER_MODULES = ['brooks.spiders']
NEWSPIDER_MODULE = 'brooks.spiders'

USER_AGENT = 'pitch-fx fanatic (+https://github.com/mattdennewitz/mlb-brooks-pitch-importer)'

# go easy
CONCURRENT_REQUESTS = 8
