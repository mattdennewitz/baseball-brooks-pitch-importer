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
    2011: (datetime.datetime(2011, 03, 31),
           datetime.datetime(2011, 10, 28)),
    2012: (datetime.datetime(2012, 03, 28),
           datetime.datetime(2012, 10, 28)),
    2013: (datetime.datetime(2013, 03, 31),
           datetime.datetime(2013, 10, 30)),
    2014: (datetime.datetime(2014, 03, 22),
           datetime.datetime(2014, 10, 29)),
    2015: (datetime.datetime(2015, 04, 05),
           datetime.datetime(2015, 11, 02)),

    # 2016 season cannot get here soon enough
    # 2016: (datetime.datetime(2016, 4, 3),
    #        datetime.datetime(2016, 10, 2))
}

MIN_SEASON = min(SEASON_RANGES)
MAX_SEASON = max(SEASON_RANGES)

TAB_URL = 'http://www.brooksbaseball.net/pfxVB/tabdel_expanded.php?pitchSel={pitcher}&game={game}&s_type=1'
