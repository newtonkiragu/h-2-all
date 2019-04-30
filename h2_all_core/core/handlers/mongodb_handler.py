import sys
from typing import List,Dict
from pymongo import MongoClient
from decouple import config

class MongoConfig:
    uname = config('MONGO_INITDB_ROOT_USERNAME')
    dbpass = config('MONGO_INITDB_ROOT_PASSWORD')
    dbhost = config('MONGO_HOST')
    dbname=config('MONGO_DB_NAME')
    db_url = f'mongodb://{uname}:{dbpass}@{dbhost}:45700'


class MongoDbStorageHandler:

    def __init__(self, *args, **kwargs):
        self.config=MongoConfig()
        self.client=MongoClient(self.config.db_url)
        self.database=self.client[self.config.dbname]

    def write(self,collec,data:List[Dict]) -> bool:
        try:
            mongo_col=self.database[collec]
            ids=mongo_col.insert_many(data)
            return True

        except Exception as e:
            print(e)
            return False

    def read(self,collec) -> List[Dict]:
        pass

    def find(self,q,c):
        return self.database[c].find(q)

    def fetch_all(self,collec) -> List[Dict]:
        try:
            return [x for x in self.database[collec].find()]
        except Exception as e:
            self.logError(sys.exc_info(), e, True)
            return [{}]

