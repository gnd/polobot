#!/usr/bin/env python3

from polobot.db_class import db_class
from polobot.ticker_collector import ticker_collector
import configparser
import sys
import os

### load config
settings_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings_python')
config = configparser.ConfigParser()
config.read_file(open(settings_file))
DB_HOST = config.get('database', 'DB_HOST')
DB_USER = config.get('database', 'DB_USER')
DB_PASS = config.get('database', 'DB_PASS')
DB_NAME = config.get('database', 'DB_NAME')
API_URL = config.get('ticker', 'API_URL')
API_PAIRS = config.get('ticker', 'API_PAIRS')

def main():
    # initialize db
    db = db_class(DB_HOST, DB_USER, DB_PASS, DB_NAME)
    db.open_db()
    
    # get ticker data
    collector = ticker_collector(API_URL)
    data = collector.collect_basic_ticker()
    
    # process & store data
    for pair in API_PAIRS.split(','):
        pair_data = data[pair]
        daily_range = float(pair_data['high24hr']) - float(pair_data['low24hr'])
        pair_data['last_position'] = (float(pair_data['last']) - float(pair_data['low24hr'])) / daily_range
            
        # insert pair_data into db
        db.insert_pair_data(pair, pair_data)
    
    # close db
    db.close_db()
    
if __name__ == '__main__':
    main()