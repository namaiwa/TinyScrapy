from TinyScrapy.scheduler import Scheduler
from TinyScrapy.tinyscrapy import Response, Request
from twisted.internet import reactor, defer
from twisted.web.client import getPage
import types


class Engine(object):
    def __init__(self):
        self._close = None
        # 异步爬取时的最大并发数
        self.max = 5
        self.scheduler = Scheduler()
        self.crawling_no = 0

    # 将初始request添加到队列
    @defer.inlineCallbacks
    def open_spider(self, start_requests):
        self._close = defer.Deferred()
        for req in start_requests:
            self.scheduler.enqueue_request(req)
        yield self._close
        # reactor.callLater(0, self.crawl_request)

    # 异步下载
    @defer.inlineCallbacks
    def crawl_request(self, *args, **kvargs):
        if self.scheduler.size() == 0:
            if self.crawling_no == 0:
                self._close.callback(None)
            return

        while self.scheduler.size() != 0 and self.crawling_no < self.max:
            req = self.scheduler.next_request()
            if req:
                self.crawling_no += 1
                resp = getPage(req.url.encode('utf-8'))
                resp.addCallback(self.response_callback, req)
                resp.addCallback(self.crawl_request)
                yield

    # 回调函数，生成Response对象,调用parse处理Response
    def response_callback(self, content, request):
        self.crawling_no -= 1
        response = Response(content, request)
        result = request.callback(response)
        if isinstance(result, types.GeneratorType):
            for obj in result:
                if isinstance(obj, Request):
                    self.scheduler.enqueue_request(obj)




