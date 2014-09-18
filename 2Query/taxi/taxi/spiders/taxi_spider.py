#! /usr/bin/env python
#################################################################################
#     File Name           :     taxi_spider.py
#     Created By          :     xd
#     Creation Date       :     [2014-09-07 16:43]
#     Last Modified       :     [2014-09-18 09:59]
#     Description         :     
#################################################################################

import scrapy
from scrapy import log
from scrapy.exceptions import CloseSpider
import json

class TaxiSpider(scrapy.Spider):
    name = 'TaxiSpider'
    start_urls = []
    def __init__(self, *args, **kwargs):
        super(TaxiSpider, self).__init__(*args, **kwargs)
    def start_requests(self): 
        # not working in Spider file_list = scrapy.settings.Settings.get('FILE_LIST')
        file_list = "/home/xd/Developer/data/taxi/2Query/filelist.txt"
        files = fin = open(file_list).readlines()
        for f in files:
            rides = open(f[:-1]).readlines()
            for idx, ride in enumerate(rides):
                t = ride.split(',')
                origin = str(t[4])+','+str(t[3])
                dest = str(t[6])+','+str(t[5])
                # tactics 11
                url = "http://api.map.baidu.com/direction/v1?mode=driving&destination="+dest+"&origin="+origin+"&origin_region=%E5%8D%97%E4%BA%AC&destination_region=%E5%8D%97%E4%BA%AC&output=json&ak=pGTvmCA8hEjPfACDwUYA5aFG&tactics=11"
                # tactics 12
                # url = "http://api.map.baidu.com/direction/v1?mode=driving&destination="+dest+"&origin="+origin+"&origin_region=%E5%8D%97%E4%BA%AC&destination_region=%E5%8D%97%E4%BA%AC&output=json&ak=pGTvmCA8hEjPfACDwUYA5aFG&tactics=12"
                # tactics 10
                # url = "http://api.map.baidu.com/direction/v1?mode=driving&destination="+dest+"&origin="+origin+"&origin_region=%E5%8D%97%E4%BA%AC&destination_region=%E5%8D%97%E4%BA%AC&output=json&ak=pGTvmCA8hEjPfACDwUYA5aFG&tactics=10"
                request = scrapy.Request(url, callback=self.parse)
                request.meta['carNo'] = int(t[0])
                request.meta['rideNo'] = int(idx)
                yield request
                # self.start_urls.append(url)
        return
    def parse(self, response):
    # [webapi/direction-api - Wiki](http://developer.baidu.com/map/index.php?title=webapi/direction-api)
        js = json.loads(response.body)
        if js["status"]:
            # 0 is ok, 2 is parameter problem, 5 is quota problem
            self.log('Status is %d' % js["status"] , level=log.WARNING)
            log.msg(format="Retrying %(request)s (API error please check)",
                    level=log.DEBUG, spider=spider, request=request)
            retryreq = response.request.copy()
            retryreq.meta['_force_update'] = True
            retryreq.dont_filter = True
            retryreq.priority = request.priority + self.priority_adjust
            yield retryreq
            raise CloseSpider('Quota Exceeded')
