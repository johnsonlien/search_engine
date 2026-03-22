from abc import ABC, abstractmethod


class AbstractQueue(ABC):
    def __init__(self):
        pass

    def push(self, topic, data):
        pass

    def pull(self):
        pass

    def connect(self, ip, port):
        pass

    def disconnect(self):
        pass