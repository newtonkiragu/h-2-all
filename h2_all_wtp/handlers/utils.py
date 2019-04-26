from re import search
def get_amount_and_name(message):
    regex = r'You have received Ksh(?P<amount>[,\d]+.\d+) from (?P<client_name>[A-Za-z 0-9]+) \d+ on'
    data = search(regex, message)
    if data:
        return data.groupdict()
    return None
