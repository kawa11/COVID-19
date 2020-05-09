from pymongo import MongoClient


uri = 'mongodb://localhost:27017/'
client = MongoClient(uri)
db = client['2019-nCoV']


class DB:
    def __init__(self):
        self.db = db

    def insert(self, collection, data):
        self.db[collection].insert(data)

    def find_one(self, collection, data=None):
        return self.db[collection].find_one(data)