# -*- coding: utf-8 -*-

# Scrapy settings for taxi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'taxi'

SPIDER_MODULES = ['taxi.spiders']
NEWSPIDER_MODULE = 'taxi.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'taxi behavior research project'

# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 50,
        'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
        # Fix path to this module
        'taxi.randomproxy.RandomProxy': 100,
        'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#        'taxi.filter.Filter': 80,
#        'taxi.httpcache.HttpCacheMiddleware': 900,
        'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 800,
}

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
PROXY_LIST = '/home/xd/Developer/data/taxi/2Query/proxylist.txt'
FILE_LIST = '/home/xd/Developer/data/taxi/2Query/filelisttest.txt'


# Cache Part
HTTPCACHE_ENABLED = True
#HTTPCACHE_STORAGE = 'scrapy.contrib.httpcache.FilesystemCacheStorage'
#HTTPCACHE_STORAGE = 'scrapy.contrib.httpcache.DbmCacheStorage'
HTTPCACHE_STORAGE = 'scrapy.contrib.httpcache.LeveldbCacheStorage'
HTTPCACHE_DIR = '/home/xd/Developer/data/taxi/2Query/'
HTTPCACHE_POLICY = 'scrapy.contrib.httpcache.DummyPolicy'
HTTPCACHE_IGNORE_HTTP_CODES = ['301', '302', '404', '405', '501', '502']


# MISC
LOG_LEVEL = 'INFO'
#LOG_FILE = '/home/xd/Developer/data/taxi/2Query/log.txt'
#LOG_STDOUT = True

