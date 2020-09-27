# url-crawl

##### Hey! Are there any url giving 404 on your page? Let's check it out!

- **ur-crawl**  finds whether the HTTP Status Code you specified for given url, exists and provides detailed reporting.

# Getting Started

## Clone This Repository

```
git clone https://github.com/Url-Crawler/url-crawler.git
```

## Requirements

- Python 3.8
- MongoDB 2.0 and up 


# How To Run
## 1.  Creating virtualenv

Create a virtualenv and activate it.

```
$ pip install virtualenv
$ virtualenv venv
```

- **Mac OS / Linux**
```
$ source venv/bin/activate
```

- **Windows**
```
$ cd venv
$ source Scripts/activate
```

**virtualenv** is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

## 2.  Installing Requirement Packages

```
$ pip install -r requirements.txt
```

You can use this command to be able to install necessary modules for python. There is a requirement text which includes the packages which have been used. The only thing you need to do is to run the given command for all packages you need.

## 3. Initial Point of Services
```
$ (venv) python url_crawler_services.py
```

After that, this application listen to 8888 port. You can change it if you want.

    app.listen(port='8888')

You can see initial message to default address as http://localhost:8888/

    {
       "message": "Hi ! This is Url Crawler. "
    }

------------

# Services

There are 2 Services; 
**-> /crawl**
**-> /crawldetail**

------------

**/crawl :** This endpoint gives all HTTP Status Codes and details of that code according to the starting value of the code **for only your url (1 Level Crawling )**. For example, 4xx gives you all status codes stating with 4 such as 400, 401, 403, 404, 416..


###### Sample Request
```
$ curl --location --request POST 'http://localhost:8888/crawl' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url" : "https://www.yourdomain.com/",
    "status": "4XX"
}'
```

------------


**/crawldetail :** This endpoint gives all HTTP Status Codes and details of that code according to the starting value of the code **for your url and urls in them. (2 Level Crawling ) **. For example, 4xx gives you all status codes stating with 5 such as 500, 501, 502, 503..


###### Sample Request
```
$ curl --location --request POST 'http://localhost:8888/crawldetail/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url" : "https://www.yourdomain.com/",
    "status" : "4XX"
}'
```
# Reporting
Each service call is recorded from MongoDB to your local server or any client you given.
In MongoDB, you can find Database whose name is UrlCrawler and 2 Collection such **Crawl_Links** and **Crawl_Detail**.


------------


**Crawl_Links :** It gives the data for summary of service call and generate Group ID for can query Crawl_Detail with it called group_id. 

```
    {
        "_id" : ObjectId("xxxx-xxxxx-xxxxxx"),  // auto-generated-id
        "group_id" : "yyyy-yyyyy-yyyyyy", // id for service referance call
        "href" : "https://www.yourdomain.com",  // url that you want to crawl
        "date" : "2020-10-25T20:27:13.000Z", // request date
        "queryType" : "General"  // /crawl --> General Type of Crawl
    }
```


**Crawl_Detail:** It gives the data for detail of service call by Group ID. You can see different url with the same group_id that means there are multiple HTTP codes you specified in your url.

```
{
    "_id" : ObjectId("xxxx-xxxxx-xxxxxx-1"),  // auto-generated-id
    "group_id" : "yyyy-yyyyy-yyyyyy", // id for service referance call
    "link" : "https://www.yourdomain.com/aboutme;", // one the link in your domain address
    "request_date" : "2020-10-25T20:27:13.000",
    "status" : 400, // https://www.yourdomain.com/aboutme gives you 400 (Bad Request)
    "headers" : {
        "Cache-Control" : "private",
        "Content-Length" : "11",
        "Content-Type" : "text/html",
        "Server" : "XXXX Web Servers",
        "Date" : "2020-10-25",
        "Set-Cookie" : "xxxxxxx"
    },
    "queryType" : "General"
}

{
    "_id" : ObjectId("xxxx-xxxxx-xxxxxx-2"),  // auto-generated-id
    "group_id" : "yyyy-yyyyy-yyyyyy", //id for service referance call
    "link" : "https://www.yourdomain.com/contactus;", // one the link in your domain address
    "request_date" : "2020-10-25T20:27:13.000",
    "status" : 404, // https://www.yourdomain.com/contactus gives you 404 (Not Found)
    "headers" : {
        "Cache-Control" : "private",
        "Content-Length" : "11",
        "Content-Type" : "text/html",
        "Server" : "XXXX Web Servers",
        "Date" : "2020-10-25",
        "Set-Cookie" : "xxxxxxx"
    },
    "queryType" : "General"
}
```
------------
## Contributors
<table style="width:100%">
  <tr>
    <td align="center"><a href="https://github.com/oktydag"><img src="https://avatars0.githubusercontent.com/u/22777355" width="100px;" alt=""/><br /><sub><b>Oktay Dağdelen </b></sub></a><br />
    </td>
    <td align="center"><a href="https://github.com/mertbilgic"><img src="https://avatars2.githubusercontent.com/u/34304850" width="100px;" alt=""/><br /><sub><b>Mert Bilgiç</b></sub></a><br />
    </td>
  </tr>
</table>
    
    
  
  

