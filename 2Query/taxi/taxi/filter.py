from scrapy import log
import json

class Filter(object):
    def __init__(self):
        pass
    def process_response(self, request, response, spider):
        js = json.loads(response.body)
        if js["status"]:
            # 0 is ok, 2 is parameter problem, 5 is quota problem
            self.log('Status is %d' % js["status"] , level=log.WARNING)
            log.msg(format="Retrying %(request)s (API error please check)",
                    level=log.DEBUG, spider=spider, request=request)
            retryreq = request.copy()
            retryreq.meta['_force_update'] = True
            retryreq.dont_filter = True
            retryreq.priority = request.priority + self.priority_adjust
            return retryreq
