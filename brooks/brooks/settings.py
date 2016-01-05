# -*- coding: utf-8 -*-

BOT_NAME = 'brooks'

SPIDER_MODULES = ['brooks.spiders']
NEWSPIDER_MODULE = 'brooks.spiders'

USER_AGENT = 'pitch-fx fanatic (+https://github.com/mattdennewitz/mlb-brooks-pitch-importer)'

# go easy
CONCURRENT_REQUESTS = 8

FEED_EXPORT_FIELDS = [
    'date_stamp',
    'park_sv_id',
    'play_guid',
    'ab_total',
    'ab_count',
    'pitcher_id',
    'batter_id',
    'ab_id',
    'des',
    'type',
    'id',
    'sz_top',
    'sz_bot',
    'pfx_xdatafile',
    'pfx_zdatafile',
    'mlbam_pitch_name',
    'zone_location',
    'pitch_con',
    'stand',
    'strikes',
    'balls',
    'p_throws',
    'gid',
    'pdes',
    'spin',
    'norm_ht',
    'inning',
    'pitcher_team',
    'tstart',
    'vystart',
    'ftime',
    'pfx_x',
    'pfx_z',
    'uncorrected_pfx_x',
    'uncorrected_pfx_z',
    'x0',
    'y0',
    'z0',
    'vx0',
    'vy0',
    'vz0',
    'ax',
    'ay',
    'az',
    'start_speed',
    'px',
    'pz',
    'pxold',
    'pzold',
    'sb',
]
