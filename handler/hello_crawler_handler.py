from tornado import web

class HelloCrawlerHandler(web.RequestHandler):
  def get(self):
    self.write({'message': 'Hi ! This is Url Crawler. '})