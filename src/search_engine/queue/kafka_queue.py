from .abstract_queue import AbstractQueue

from kafka import KafkaConsumer, KafkaProducer

class KafkaQueue(AbstractQueue):
    def __init__(self):
        self.producers = {}
        self.consumers = {}

    def add_producer(self, ip, port, topic):
        pass

    def add_subscriber(self, topic, servers : list[str] = ["localhost:9092"]):
        if topic in self.consumer:
            print("{topic} is already created")
            return

        self.consumers[topic] = KafkaConsumer(topic, bootstrap_servers=servers)

    def del_subscriber(self, topic):
    def connect(self, ip, port):
        # KafkaProducer and KafkaConsumer handles the connection
        pass

    def disconnect(self):
        pass

    def push(self, topic, data):
        try:
            print(f"Pushing to {self.push_topic}")
            future = self.producer.send(f"{self.push_topic}", data)
            response = future.get(timeout=5)
            print(f"Response info: {response}")
        except Exception as ex:
            print(f"Could not push to Kafka queue: {ex}")

    def pull(self):
        try:
            data = self.consumer.poll(timeout_ms=5000)
            return data
        except Exception as ex:
            print(f"Exception trying to pull from Kafka queue: {ex}")

    def __del__(self):
        self.producer.close()
        self.consumer.close()