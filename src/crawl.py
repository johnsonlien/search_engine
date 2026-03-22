from .crawler.crawler import Crawler
from .queue.mock_queue import MockQueue
from .queue.kafka_queue import KafkaQueue

if __name__ == "__main__":
    # q = MockQueue("127.0.0.1", 1234)
    q = KafkaQueue("127.0.0.1", 9092)

    crawler = Crawler(q, depth=2)
    crawler.run()