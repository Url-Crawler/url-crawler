import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.http import HtmlResponse
from datetime import datetime,timedelta
from urllib.parse import urlparse

from helpers.mongo_helper import Crawl_Links
from .helper.css_selector import CssSelector

class DetailUrlCrawler(scrapy.Spider):
    name = "DetailUrlCrawler"
    queryTypeValue = "Detail"
    result = []
    crawled = []
    counter = True
    handle_httpstatus_list = [404, 500]
    
    def parse(self, response):
        url = self.url_parse.scheme+"//"+self.url_parse.netloc
        pagination_href = response.css('[class^="pagination"] a::attr(href)').extract()

        response = str(response.body)
        start = response.find("</header>")
        end = response.find("<footer ")
        response = HtmlResponse(url=url, body=response[start:end], encoding='utf-8')

        css_selector = CssSelector()
        href = css_selector.extracting_href(response)
        href = href.extract()

        parts = self.url_parse.path.split('/')
        parts = ( ['/'.join(parts[:index+1]) for index in range(len(parts))])
        self.result.extend(list((set(href)-set(pagination_href))-set(parts)))
        
        if self.counter:
            self.crawled = self.result.copy()
            self.counter = False
        if self.crawled:
            next_page = "{}://{}{}".format(self.url_parse.scheme,self.url_parse.netloc,self.crawled.pop())
            yield response.follow(url=next_page, callback=self.parse)
        else:
            url = "{}://{}".format(self.url_parse.scheme,self.url_parse.netloc)
            href = set(self.result)
            for h in href:
                link={
                    "group_id":self.g_id,
                    "href":url+""+h if h[0] == '/' else url+"/"+h,
                    "date":(datetime.now()+timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                    "queryType": self.queryTypeValue
                }
                Crawl_Links.insert_one(link)
            self.result.clear()
            

    @staticmethod
    def work(url,g_id):
        process = CrawlerProcess()
        start_urls = [url]
        url_data = urlparse(url)
        process.crawl(DetailUrlCrawler,start_urls=start_urls,g_id=g_id,url_parse=url_data)
        process.start()
    