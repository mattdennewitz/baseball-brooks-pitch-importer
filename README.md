# mlb-brooks-pitch-importer

Import Pitch f/x logs corrected by Brooks Baseball

## Installation

1. Clone this repository, preferably into a fresh virtualenv
2. Install reqs w/ Pip:

```shell
$ pip install -r requirements.txt
```

## Usage

This spider has three modes of operation:

1. Crawl all games, all pitchers (:heavy_check_mark: default)
2. Crawl specific seasons (e.g., all games in 2011)
    using `-a years=<year>[,year...]`
3. Crawl specific dates (e.g., only games played on 2010-04-18)
    using `-a dates=<Y-m-d date>[,date...]`

Results may optionally be filtered to a specific pitcher or set of pitchers
using `-a pitcher_ids=<pitcher id>[,pitcher id...]`

## Support Brooks

This would not be possible without the hard work done by Brooks Baseball.
Read more about them [here](http://www.brooksbaseball.net/about.php).

## Examples

#### Import everything

To import all pitches across all time (presently 2010-2015) as write
to a CSV file named `all-seasons.csv`:

```shell
$ scrapy crawl pitches -t csv -o all-seasons.csv
```

Note the `-t csv`, which tells the crawler to CSV-format its output.

#### Import all of 2014 and 2015's pitches

To import all pitches thrown in the 2014 and 2015 seasons and
write to a JSON file named `seasons-2014-2015.json`:

```shell
$ scrapy crawl pitches -a years=2014,2015 -o seasons-2014-2015.json
```

#### Import a single pitcher's results from a single game

To import logs for player `462985` on Apr 18, 2010
and write results to a JSON file name `2010-04-18-462985.json`:

```shell
$ scrapy crawl pitches -a dates=2010-04-18 -a pitcher_ids=462985 -o 2010-04-18-462985.json
```
