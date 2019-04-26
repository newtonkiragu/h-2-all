from handlers import SIM800L
from handlers import SimpleDataHandler


data_handler=SimpleDataHandler()

class SimpleManager:

    def __init__(self,sim):
        self.sim=sim


    def validate_sms(self,sms):
        return True if type(sms)==list and len(sms)==4 else False

    def handle_sms(self):
        msg_id = phone.get_msgid()
        sms=phone.read_and_delete_all()
        if self.validate_sms(sms):
            # ['AFRICASTKNG', '19/04/26', '02:18:35+12', 'New Message: Hello STOP*456*9*5#\n']
            sender,message=sms[0],sms[3]
            if message.beginswith("edit-price"):
                data_handler.edit_price(message)

if __name__=="__main__":
    sim=SIM800L()
    sim.setup()
    simple_manager=SimpleManager(sim)
    sim.callback_msg(simple_manager.handle_sms)
    while True:
        sim.check_incoming()


