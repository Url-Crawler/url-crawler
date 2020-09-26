import json
import uuid
import urllib
from bson.json_util import dumps, loads
from bson import json_util
import multiprocessing as mp
from tornado import ioloop, web
from helpers.mongo_helper import *
from helpers.request_helper import execute_to_ping, request_validation, createResponse
import Modules.spider as spiderModule
from handler.not_found_handler import NotFoundHandler
from SpiderCreator.crawler_factory import *

class SpiderHandler(web.RequestHandler):

    def post(self):

        url = self.request.uri
        url.replace('//', '/')
        url = url if url[-1]!= '/' else url[:(len(url)-1)]
        url.lower()
        crawler_factory = CrawlerFactory()
        spider_content = crawler_factory._get_mapped_crawler(url)
        queryTypeValue = spider_content.queryTypeValue


        if(spider_content == "SpiderNotFound"):
            NotFoundHandler.not_found(self)

        data=json.loads(self.request.body)

        valid,message = request_validation(data)

        if(valid):
            max_request_count = 6
            g_id = str(uuid.uuid4())

            pool = mp.Pool(max_request_count)
            spider = spider_content()
            args = (data["url"],g_id)
            pool.apply_async(spider.work,args=args)
            pool.close()
            pool.join()

            execute_to_ping(data["status"],g_id,queryTypeValue)            
            
            result = loads(dumps(Crawl_Detail.find({"group_id" : g_id})))
            if(len(result)==0): message =  data["url"]+ " address does not contain any url of " + data["status"] + " status code."
            result =  createResponse(result,message,valid)
        else:
            result = []
            result =  createResponse(result,message,valid)

        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(result,default=json_util.default))