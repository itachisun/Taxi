distributed crawler
    multi-thread

Crawler  
    Scrapy http://scrapy.org/ 

Task Queue
    Celery http://www.celeryproject.org/

HTTP proxy scheduler
    proxy list
        http://www.xici.net.co/nt/
        http://www.kuaidaili.com/free/intr/

strawman
    just send out task, and choose random proxy to use, retry if timeout
    (imbalance overhead possible)
    not too small granularity, each worker process full record of a single vehicle
    (about 100KB)
  
Reference
----
* Scrapy
    * Random proxy middleware for Scrapy [aivarsk/scrapy-proxies](https://github.com/aivarsk/scrapy-proxies)
    * [python - Setting Scrapy proxy middleware to rotate on each request - Stack Overflow](http://stackoverflow.com/questions/20792152/setting-scrapy-proxy-middleware-to-rotate-on-each-request)
    * [Jobs: pausing and resuming crawls — Scrapy 0.24.4 documentation](http://doc.scrapy.org/en/latest/topics/jobs.html)
\
* Timeout / Retry
    * [[Python]网络爬虫（五）：urllib2的使用细节与抓站技巧 - 汪海的实验室 - 博客频道 - CSDN.NET](http://blog.csdn.net/pleasecallmewhy/article/details/8925978)
        * [urllib2 - The Missing Manual](http://www.voidspace.org.uk/python/articles/urllib2.shtml#openers-and-handlers)
    * [How to retry after exception in python? - Stack Overflow](http://stackoverflow.com/questions/2083987/how-to-retry-after-exception-in-python)
* General
    * [用Python抓网页的注意事项 | 飞熊在天](http://blog.raphaelzhang.com/2012/03/issues-in-python-crawler/)
    * [Python网页解析 | 飞熊在天](http://blog.raphaelzhang.com/2012/03/python-html-parsing/)
        * 我现在使用的是lxml，它是基于C语言开发的libxml2与libxslt库的。经我个人测试，速度比BeautifulSoup 3平均要快10倍。
    * [用python爬虫抓站的一些技巧总结 zz [Python俱乐部]](http://www.pythonclub.org/python-network-application/observer-spider)
    * [使用python编写简单网络爬虫技巧总结 | armsword的涅槃之地](http://armsword.com/2014/03/31/python-in-crawler.html)

Log
----
total 6569857 rides

test1 finish 83774 in 14 min
