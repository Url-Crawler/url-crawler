from multiprocessing import Pool

class CrawlManager:
    __pool = None

    def __init__(self, pool_size=6):
        if CrawlManager.__pool == None:
            self.__pool = Pool(processes=pool_size)

    def new_task(self, spider, args):
            self.__pool.apply_async(spider.work,args=args)
            self.__pool.close()
            self.__pool.join()