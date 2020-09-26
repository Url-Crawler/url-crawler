import pymongo
from helpers.config_helper import *

class MongoConnectionHelper:
    __instance = None

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if MongoConnectionHelper.__instance == None:
            MongoConnectionHelper()
        return MongoConnectionHelper.__instance
        
    def __init__(self):
        """ Virtually private constructor. """
        if MongoConnectionHelper.__instance == None:
            MongoConnectionHelper.__instance = pymongo.MongoClient(get_value_from_name('mongodb_client'))

monglo_client = MongoConnectionHelper.getInstance()

connected_db = monglo_client['UrlCrawler']

Crawl_Links = connected_db["Crawl_Links"]

Crawl_Detail = connected_db["Crawl_Detail"]


    

