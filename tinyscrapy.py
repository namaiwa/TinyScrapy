

class Request(object):
    def __init__(self, url, callback):
        self.url = url
        self.callback = callback


class Response(object):
    def __init__(self, content, request):
        self.content = content
        self.request = request
        self.url = self.request.url
