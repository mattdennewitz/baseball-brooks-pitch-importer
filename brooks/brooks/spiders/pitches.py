# -*- coding: utf-8 -*-

import datetime
import six

if six.PY3:
    from urllib import parse as urlparse
else:
    import urlparse

import scrapy
from scrapy.exceptions import CloseSpider

from ..items import Pitch
from ..const import * # fight me


def parse_years(years):
    years = map(int, years.split(','))
    return sorted(set([year for year in years if year in SEASON_RANGES]))


def parse_dates(dates):
    dates = dates.split(',')
    valid_dates = []

    for date in dates:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        season_range = SEASON_RANGES[date.year]
        if season_range[0] <= date <= season_range[1]:
            valid_dates.append(date)

    return sorted(set(valid_dates))


def parse_pitcher_ids(pitcher_ids):
    if pitcher_ids is not None:
        return pitcher_ids.split(',')
    return []


class PitchLogSpider(scrapy.Spider):
    name = 'pitches'
    allowed_domains = ['brooksbaseball.net']

    def __init__(self, years=None, dates=None, pitcher_ids=None, *a, **kw):
        super(PitchLogSpider, self).__init__(*a, **kw)

        if years is not None:
            self.mode = M_YEARS
            self.years = parse_years(years)
        elif dates is not None:
            self.mode = M_DATES
            self.dates = parse_dates(dates)
        else:
            self.mode = M_ALL
            self.years = range(MIN_SEASON, MAX_SEASON + 1)

        # select only the following pitchers
        self.pitcher_ids = parse_pitcher_ids(pitcher_ids)
        if self.pitcher_ids:
            self.logger.debug('Filtering to pitchers: {}'.format(
                              self.pitcher_ids))

        self.start_urls = list(self.get_start_urls())

    def get_start_urls(self):
        for date in self.get_date_range():
            date = date.strftime('%m/%d/%Y')
            yield 'http://www.brooksbaseball.net/dashboard.php?dts={}'.format(date)

    def get_date_range(self):
        if self.mode in (M_ALL, M_YEARS):
            # yield once for every date in every season
            for year in self.years:
                start_date, end_date = SEASON_RANGES[year]
                s_diff = (end_date - start_date).days
                for day_offset in range(s_diff + 1):
                    yield start_date + datetime.timedelta(days=day_offset)
        elif self.mode == M_DATES:
            # yield each specific date
            for date in self.dates:
                yield date
        else:
            raise CloseSpider('Did not understand input date range')

    def get_table_url(self, pitcher, game):
        return TAB_URL.format(pitcher=pitcher, game=game)

    def parse(self, response):
        log_links = response.xpath('//a[contains(., "Game Log")]/@href')

        for link in log_links.extract():
            bits = urlparse.urlparse(link)
            qs = urlparse.parse_qs(bits.query)

            pitcher = qs['pitchSel'][0].replace('.xml', '')
            game = qs['game'][0]

            if self.pitcher_ids and not pitcher in self.pitcher_ids:
                self.logger.debug('Skipping undesired pitcher: {}'.format(
                                  pitcher))
                continue

            yield scrapy.Request(self.get_table_url(pitcher, game),
                                 callback=self.parse_game_log)

    def parse_game_log(self, response):
        rows = response.css('tr')

        self.logger.debug('Found {} pitches at {}'.format(
                          len(rows), response.url))

        header = rows.pop(0)

        keys = [
            key.strip()
            for key in header.xpath('./th/text()').extract()
        ]

        for row in rows:
            values = []

            for cell in row.xpath('./td'):
                value = cell.xpath('text()').extract_first()
                if not value:
                    value = ''
                values.append(value)

            log = dict(zip(keys, values))

            # field naming normalization
            log['date_stamp'] = log.pop('dateStamp')
            log['pfx_xdatafile'] = log.pop('pfx_xDataFile')
            log['pfx_zdatafile'] = log.pop('pfx_zDataFile')

            yield Pitch(**log)
