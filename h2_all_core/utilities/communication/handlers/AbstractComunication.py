import abc


class AbstractCommunication(abc.ABC):

    def store_message(self):
        pass

    def receive_message(self, request) -> dict:
        return {}
