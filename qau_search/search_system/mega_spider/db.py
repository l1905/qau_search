#!usr/bin/env python
# encoding:utf-8

from pymongo import Connection

from settings import DB_NAME, COLLECTION_NAME

class MongoDB(object):
    def __init__(self):
        self.database = DB_NAME
        self.collection = COLLECTION_NAME
        self.connection = Connection();
        self.database = self.connection[self.database]
        self.collection = self.database[self.collection]

    def insert(self, data):

        return self.collection.insert(data)

    def find(self, query_data=None):
        if query_data:
            return self.collection.find(query_data)
        return self.collection.find()

    def find_one(self, query_data=None):
        if query_data:
            return self.collection.find_one(query_data)
        return self.collection.find()