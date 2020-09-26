import json
import requests
from helpers.mongo_helper import *
from multiprocessing import Pool
from datetime import datetime,timedelta
from functools import partial


def get_link_response_code(link_to_check):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    resp = requests.head(link_to_check,headers=headers)
    if resp.status_code == 405:
        resp = requests.get(link_to_check,headers=headers)
    return resp

def save_matched_urls(response_code,queryType,url):
    response = get_link_response_code(url["href"])
    
    if(response_code == str(response.status_code)):
        info={
        "group_id":url["group_id"],
        "link":url["href"],
        "request_date":(datetime.now()+timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "status":response.status_code,
        "headers":response.headers,
        "queryType" : queryType
        }
        try:
            Crawl_Detail.insert_one(info)
        except Exception as error:
            print(error)
    elif(response_code[:1] == str(response.status_code)[:1] and 'xx' in str(response_code).lower()):
        info={
        "group_id":url["group_id"],
        "link":url["href"],
        "request_date":(datetime.now()+timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "status":response.status_code,
        "headers":response.headers,
        "queryType" : queryType
        }

        try:
            Crawl_Detail.insert_one(info)
        except Exception as error:
            print(error)
    
     
        
def request_validation(data):
    if 'url' not in data:
        return False,"Please Enter a Valid Url."
    elif 'status' not in data:
        return False,"Please Enter Http Status Code into status field."
    try:
        r = get_link_response_code(data["url"])
    except requests.exceptions.Timeout:
        return False,"Timeout"
    except requests.exceptions.TooManyRedirects:
        return False,"TooManyRedirects"
    except requests.exceptions.RequestException as e:
        return False,"Invalid URL"
    except requests.exceptions.HTTPError as err:
        return False,"404 Client Error: Not Found for url"
    return True,"Success"

def execute_to_ping(response_code,g_id,queryTypeValue):
    concurrent = 10
    p = Pool(concurrent)
    crawlData = Crawl_Links.find({"group_id" : g_id})
    func = partial(save_matched_urls, response_code, queryTypeValue)
    p.map(func, crawlData)
    p.close

def createResponse(result,message,status):
    mesage_model = {
        'ResponseStatus':status,
        'Message': message,
        'Result':result
    }
    return mesage_model




