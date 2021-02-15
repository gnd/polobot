#!/usr/bin/env python3

from db import db_class
import urllib.request
import configparser
import json
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
API_PAIR = config.get('ticker', 'API_PAIR')

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if (operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def main():
    data = getResponse(API_URL)
    pair_data = data[API_PAIR]
    daily_range = float(pair_data['high24hr']) - float(pair_data['low24hr'])
    pair_data['last_position'] = (float(pair_data['last']) - float(pair_data['low24hr'])) / daily_range
    
    # insert pair_data into db
    db = db_class(DB_HOST, DB_USER, DB_PASS, DB_NAME)
    db.open_db()
    db.insert_pair_data(API_PAIR, pair_data)
    db.close_db()

if __name__ == '__main__':
    main()