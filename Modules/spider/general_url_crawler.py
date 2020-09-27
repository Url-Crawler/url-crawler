import scrapy
import pymongo
from helpers.mongo_helper import *
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from datetime import datetime,timedelta
from urllib.parse import urlparse

class GeneralUrlCrawler(scrapy.Spider):
    name = "GeneralUrlCrawler"
    queryTypeValue = "General"
    start_urls = []
    g_id = ""
    url_parse = ""
    def parse(self, response):
        url = self.url_parse.scheme+"://"+self.url_parse.netloc

        href = response.css('a:not([href^="http"])')
        href = href.css('a:not([href^="partners"])')
        href = href.css('a:not([href^="#"])')
        href = href.css('a:not([href="/mobil"])')
        href = href.css('a:not([href^="{"])')
        href = href.css('a:not([href^="//js"])')
        href = href.css('a:not([href^="/www"])')
        href = href.css('a:not([href^="//www"])')
        href = href.css('a:not([href=""])')
        href = href.css('a:not([href^="mailto:"])')
        href = href.css('a:not([href^="Javascript:"])')
        #href = href.xpath('//a[not(contains(@href, ":"))]')
        href = href.css('a:not([href^="//"])')
        href = href.css('a:not([href^="javascript"])::attr(href)').extract()

        href = set(href)
        for h in href:
            link={
                "group_id":self.g_id,
                "href":url+""+h if h[0] == '/' else url+"/"+h,
                "date":(datetime.now()+timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                "queryType" : self.queryTypeValue
            }
            Crawl_Links.insert_one(link)            

    @staticmethod
    def work(url,g_id):
        process = CrawlerProcess()

        start_urls = [url]
        url_parse = urlparse(url)

        process.crawl(GeneralUrlCrawler,start_urls=start_urls,g_id=g_id,url_parse=url_parse)
        process.start()