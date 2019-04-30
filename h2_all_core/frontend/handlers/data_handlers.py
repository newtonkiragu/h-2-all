from core.handlers import MongoDbStorageHandler

class BoreHoleMongoHandler:
    def __init__(self):
        self.mongo_handler=MongoDbStorageHandler()
        self.database="h2all"
        self.collection="boreholes"

    def borehole_schema(self):
        return {
            "phone_number":None,
            "location":None,
            "secret_key":None,
            "price_per_litre":None,
            "stats":[
            ]
        }

    def stats_schema(self):
        return {'time': None, 'amount': None, 
                'clientName': None, 'clientPhone': None, 
                'boreholeBalance': None, 'transactionCode': None}

    def fetch(self,query=None):
        if query==None:
            return self.mongo_handler.fetch_all(self.collection)
        else:
            return self.mongo_handler.database[self.collection].find(q,self.collection)

    def edit_price(self,phone_number,price):
        q={"phone_number":phone_number}
        n={ "$set": { "price_per_litre":price }}
        self.mongo_handler.database[self.collection].update_one(q,n)

