from twisted.internet import defer, reactor
from TinyScrapy.spider.Baidu import BaiduSpider
from TinyScrapy.engine import Engine


class CrawlerProcess(object):
    def __init__(self):
        self.start_requests = None
        self.crawlers = None
        self.engine = Engine()
        self.active = set()
        self._close = None

    def run(self, spider):
        self.start_requests = spider.start_requests()
        self._close = self.engine.open_spider(self.start_requests)
        self.crawlers = self.engine.crawl_request()
        self.active.add(self._close)
        self.active.add(self.crawlers)
        # 添加事件循环
        a = defer.DeferredList(self.active)
        a.addBoth(lambda _: reactor.stop())
        # 开始事件循环
        reactor.run()


if __name__ == '__main__':
    baidu = BaiduSpider()
    crawler = CrawlerProcess()
    crawler.run(baidu)
