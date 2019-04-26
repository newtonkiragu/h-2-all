from handlers import SIM800L
from handlers import SimpleDataHandler,Valve,Waterflow
from handlers.utils import get_amount_and_name
from handlers import settings

data_handler=SimpleDataHandler()
valve=Valve()
waterflow=Waterflow()

class SimpleManager:

    def __init__(self,sim):
        self.sim=sim


    def validate_sms(self,sms):
        return True if type(sms)==list and len(sms)==4 else False

    def handle_sms(self):
        msg_id = self.sim.get_msgid()
        sms=self.sim.read_and_delete_all()
        if self.validate_sms(sms):
            # ['AFRICASTKNG', '19/04/26', '02:18:35+12', 'New Message: Hello STOP*456*9*5#\n']
            sender,message=sms[0],sms[3]
            if message.startswith("edit-price"):
                data_handler.edit_price(message)
                return 
            #to check if sender is safaricom in production
            d=get_amount_and_name(message)
            print(d, message)
            if d is not None:
                self.sim.send_sms(settings.SERVER_PHONE_NUMBER,message)
                litres=float(d["amount"].replace(',', ''))/data_handler.read_price()
                print(litres)
                valve.on()
                while waterflow.water_flow < litres:
                    print(waterflow.water_flow)
                valve.off()
                waterflow.count=0
            else: print(d)

if __name__=="__main__":
    sim=SIM800L()
    sim.setup()
    simple_manager=SimpleManager(sim)
    sim.callback_msg(simple_manager.handle_sms)
    while True:
        sim.check_incoming()


