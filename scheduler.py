from queue import Queue


class Scheduler(object):
    def __init__(self):
        self.q = Queue()

    def next_request(self):
        try:
            req = self.q.get(block=False)
        except Exception as e:
            req = None
        return req

    def enqueue_request(self, req):
        self.q.put(req)

    def size(self):
        return self.q._qsize()


