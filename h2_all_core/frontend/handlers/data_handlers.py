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
            return self.mongo_handler.database[self.collection].find(q)

    def edit_price(self,phone_number,price):
        q={"phone_number":phone_number}
        n={ "$set": { "price_per_litre":price }}
        self.mongo_handler.database[self.collection].update_one(q,n)

    def create_new_borehole(self,bh):
        mbh=self.borehole_schema()
        mbh["phone_number"]=bh.phone_number
        mbh["location"]=bh.location
        mbh["secret_key"]=bh.SECRET_KEY
        mbh["price_per_litre"]=bh.price.per_litre
        for s in bh.stats.all():
            mbh["stats"].append(s.data)
        self.mongo_handler.database[self.collection].insert_one(mbh)

    def add_statistics(self,phone_number,stats):
        q={"phone_number":phone_number}
        n={ "$set": { "stats":stats }}
        self.mongo_handler.database[self.collection].update_one(q,n)



    


