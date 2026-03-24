from ..db.abstract_db import AbstractDB
from ..queue.abstract_queue import AbstractQueue

from opensearchpy import OpenSearch

import time
import requests

class Crawler():
    def __init__(self, queue: AbstractQueue, db: AbstractDB, depth: int = -1):
        self.queue = queue
        self.depth = depth
        # self.dlq = []       # Implement dead letter queue later
    def run(self):
        # self.queue.pull()
        # Stop when self.depth == 0
        while self.depth == -1 or self.depth > 0:
            # Pull() will use the queue.pull_topic()
            try:
                future = self.queue.pull()
                response = future.get(timeout=5)
                url = response.url
                fetch = requests.get(url)
                fetch.raise_for_status()

                if(self.depth > 0):
                    self.depth -= 1
            except requests.HTTPError as ex:
                print(f"Error trying to fetch {url}: {ex}")
                # Push to DLQ
            except Exception as ex:
                print(f"Exception occurred: {ex}")
            time.sleep(1)


