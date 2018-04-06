from TinyScrapy.tinyscrapy import Request

class BaiduSpider():
    name = "zhihu"
    start_url = ['http://www.baidu.com', 'http://www.bing.com']

    def start_requests(self):
        for url in self.start_url:
            yield Request(url, self.parse_user)

    def parse_user(self, response):
        print(response)
        yield Request('http://www.baidu.com', self.parse)
        yield Request('http://www.baidu.com', self.parse)
        yield Request('http://www.baidu.com', self.parse)
        yield Request('http://www.baidu.com', self.parse)
        yield Request('http://www.baidu.com', self.parse)
        yield Request('http://www.baidu.com', self.parse)
        yield Request('http://www.baidu.com', self.parse)

    def parse(self, response):
        print(response)
