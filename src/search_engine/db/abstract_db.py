from abc import ABC

class AbstractDB(ABC):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port