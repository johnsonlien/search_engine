from .abstract_queue import AbstractQueue

from kafka import KafkaConsumer, KafkaProducer

class KafkaQueue(AbstractQueue):
    def __init__(self, ip, port):
        self.producer = KafkaProducer(bootstrap_servers="localhost:9092")
        self.consumer = KafkaConsumer(isolation_level='read_committed')
        self.consumer.subscribe(['Johnson'])


    def connect(self, ip, port):
        pass
    def disconnect(self):
        pass

    def push(self, data):
        self.producer.send("Johnson", data)

    def pull(self):
        for msg in self.consumer:
            print(msg)