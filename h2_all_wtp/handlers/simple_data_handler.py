import json
import os
from handlers import settings

class SimpleDataHandler:

    def __init__(self,*args, **kwargs):
        pass

    def validate_secret_key(self,secret_key):
        return settings.SECRET_KEY==secret_key

    def read_price(self,*args, **kwargs):
        data=None
        with open(os.path.join(settings.BASE_DIR,"handlers/data.json"),"r") as jfile:
            data=json.load(jfile)
        return int(data["price_per_litre"])

    def edit_price(self,sms,*args, **kwargs):
        d=sms.replace("STOP*456*9*5#","").replace("\n","").split(":")
        if self.validate_secret_key(d[1]):
            jdata={"price_per_litre":int(d[-1]),"server_phone_number":settings.SERVER_PHONE_NUMBER}
            with open(os.path.join(settings.BASE_DIR,"handlers/data.json"),"w") as jfile:
                json.dump(jdata,jfile)
            return True
        return False

