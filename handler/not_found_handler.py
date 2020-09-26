from tornado import web

class NotFoundHandler(web.RequestHandler):
    @staticmethod
    def not_found(self):
        raise web.HTTPError(
            status_code=404,
            reason="Invalid resource path."
        )