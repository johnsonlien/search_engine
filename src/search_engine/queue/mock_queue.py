from .abstract_queue import AbstractQueue

class MockQueue(AbstractQueue):
    def __init__(self, ip, port):
        print("Mock Queue")
        self.connect(ip, port)

    def connect(self, ip, port):
        print(f"Connecting to queue at {ip}:{port}")

    def disconnect(self):
        print("Disconnecting from queue")

    def push(self, topic, data):
        print(f"Pushing {data} to topic {topic}")

    def pull(self):
        print("Pulling from the top of the queue")
        return 1