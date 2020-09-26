from tornado import ioloop, web

from handler.spider_handler import SpiderHandler
from handler.hello_crawler_handler import HelloCrawlerHandler


if __name__=="__main__":
    app = web.Application([

        (r'/', HelloCrawlerHandler),
        (r'.*', SpiderHandler),
    ])
    app.listen(port='8888')
    ioloop.IOLoop.current().start()

