import Modules.spider as spiderModule


class CrawlerFactory:

    def _get_mapped_crawler(self, request_path):
        if request_path == '/crawl':
            return spiderModule.general
        elif request_path == '/crawldetail':
            return spiderModule.detail
        else:
            return "SpiderNotFound"
