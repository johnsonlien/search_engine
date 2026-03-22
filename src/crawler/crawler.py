from ..queue.abstract_queue import AbstractQueue
import time

class Crawler():
    def __init__(self, queue: AbstractQueue, depth: int = -1):
        self.queue = queue
        self.depth = depth

    def run(self):
        self.queue.pull()
        # # Stop when self.depth == 0
        # while self.depth == -1 or self.depth > 0:
        #     value = self.queue.pull()

        #     if(self.depth > 0):
        #         self.depth -= 1

        #     time.sleep(1)


