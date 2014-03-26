#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from scrapy.spider import Spider
from scrapy.selector import Selector

logging.basicConfig(level=logging.DEBUG,filename='spider.log')
logger = logging.getLogger('MAIN-SPIDER')
class DmoSpider(Spider):
    name = "demo"
    allowed_domains = ['qau.edu.cn']
    start_urls = [
        "http://news.qau.edu.cn/"
    ]

    def parse(self, response):
        logger.debug(response.url)
        sel = Selector(response)
        logger.debug('sel is %s'%sel)
        sites = sel.xpath('//title')
        logger.debug('sites is %s'%sites)
        for site in sites:
            title = site.xpath('a/@title').extract()
            link = site.xpath('a/@href').extract()
            print title,link
            logger.debug('title is %s, link is %s'%(title,link))
        # filename = response.url.split("/")[-1]
        # open(filename,'wb').write(response.body)
