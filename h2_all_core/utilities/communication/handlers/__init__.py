from .SMSCommunication import SMSCommunicationHandler

default_handler = SMSCommunicationHandler

__all__ = [
    'default_handler',
    'SMSCommunication'
]
