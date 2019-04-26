from dateutil.parser import parse
from .AbstractComunication import AbstractCommunication
import africastalking
from re import search
from decouple import config


def parse_store_message(text_data):
    data_regex = r'(?P<code>[A-Z0-9]+) Confirmed.' \
           r'You have received Ksh(?P<amount>[,\d]+.\d+) from (?P<client_name>[A-Za-z 0-9]+) ' \
           r'(?P<client_number>\d+) on (?P<datetime>\d{1,2}/\d{1,2}/\d{1,2} ' \
           r'at \d{1,2}:\d{1,2}) (?P<meridiem>AM|PM)  ?' \
           r'New M-PESA balance is Ksh(?P<balance>[,\d]+.\d+)'

    info = search(data_regex, text_data['text'])
    if info:
        data = info.groupdict()
        transaction_time = parse(data['datetime'])
        full_data = {
            'clientName': data['client_name'],
            'clientPhone': data['client_number'],
            'amount': float(data['amount'].replace(',', '')),
            'transactionCode': data['code'],
            'boreholeBalance': float(data['balance'].replace(',', '')),
            'time': transaction_time.isoformat()
        }
        print(full_data)
    else:
        print("Unable to fetch data from text, %s" % text_data)


class SMSCommunicationHandler(AbstractCommunication):

    def __init__(self):
        super().__init__()
        self.username = config('AFRICASTALKING_USERNAME')
        self.api_key = config('AFRICASTALKING_APIKEY')
        self.sender_id = config('AFRICASTALKING_SENDER', None)

        africastalking.initialize(self.username, self.api_key)

        self.sms = africastalking.SMS

    def send_message(self, message, recipient):
        try:
            response = self.sms.send(message, [recipient, ], self.sender_id)
            print(response)
            return response
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))
            return False

    def receive_message(self, request):
        parse_store_message(request.data)
        return {"Status": "OK"}
