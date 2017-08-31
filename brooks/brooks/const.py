import datetime


__all__ = ('M_YEARS', 'M_DATES', 'M_ALL',
           'SEASON_RANGES', 'MIN_SEASON', 'MAX_SEASON',
           'TAB_URL', )

M_YEARS = 'years'
M_DATES = 'dates'
M_ALL = 'all'

SEASON_RANGES = {
    2010: (datetime.datetime(2010, 4, 4),
           datetime.datetime(2010, 11, 1)),
    2011: (datetime.datetime(2011, 3, 31),
           datetime.datetime(2011, 10, 28)),
    2012: (datetime.datetime(2012, 3, 28),
           datetime.datetime(2012, 10, 28)),
    2013: (datetime.datetime(2013, 3, 31),
           datetime.datetime(2013, 10, 30)),
    2014: (datetime.datetime(2014, 3, 22),
           datetime.datetime(2014, 10, 29)),
    2015: (datetime.datetime(2015, 4, 5),
           datetime.datetime(2015, 11, 2)),
    2016: (datetime.datetime(2016, 4, 3),
           datetime.datetime(2016, 10, 2)),
    2017: (datetime.datetime(2017, 4, 2),
           datetime.datetime(2017, 10, 2))
}

MIN_SEASON = min(SEASON_RANGES)
MAX_SEASON = max(SEASON_RANGES)

TAB_URL = 'http://www.brooksbaseball.net/pfxVB/tabdel_expanded.php?pitchSel={pitcher}&game={game}&s_type=1'
