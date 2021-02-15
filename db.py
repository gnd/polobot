import MySQLdb

class db_class():
    def __init__(self, db_host, db_user, db_pass, db_name):
        self.db_host = db_host
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name

    def open_db(self):
        self.db = MySQLdb.connect(host=self.db_host, user=self.db_user, passwd=self.db_pass, db=self.db_name)
        self.cur = self.db.cursor()

    def close_db(self):
        self.db.close()

    def insert_pair_data(self, pair_name, pair_data):
        query = "INSERT INTO {} VALUES(0, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', NOW())".format(
        'basic_ticker',
        pair_name, 
        pair_data['id'], 
        pair_data['last'], 
        pair_data['last_position'], 
        pair_data['lowestAsk'],
        pair_data['highestBid'],
        pair_data['percentChange'],
        pair_data['baseVolume'],
        pair_data['quoteVolume'],
        pair_data['isFrozen'],
        pair_data['low24hr'],
        pair_data['high24hr']
        )
        self.cur.execute(query)
        self.db.commit()