#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from scrapy.spider import Spider
from scrapy.selector import Selector

from mega_spider.items import MegaSpiderItem

logging.basicConfig(level=logging.DEBUG,filename='spider.log')
logger = logging.getLogger('MAIN-SPIDER')
class DmoSpider(Spider):
    name = "demo"
    allowed_domains = ['qau.edu.cn']
    start_urls = [
        "http://www.qau.edu.cn/"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//dd/li/a')
        items = []
        # for site in sites:
        #     item = MegaSpiderItem()

        #     item['title'] = [one.encode('utf-8') for one in site.xpath('@title').extract()]
        #     # item['title'] = site.xpath('a/@title').extract()
        #     item['link'] = site.xpath('@href').extract()
        #     items.append(item)
        # return items

        for title,link in zip(sel.xpath('//dd/li/a/@title').extract(),sel.xpath('//dd/li/a/@href').extract()):
            item = MegaSpiderItem()
            item['title'] = title.encode('utf-8')
            item['link'] = link.encode('utf-8')
            items.append(item)
        return items
        # filename = response.url.split("/")[-1]
        # open(filename,'wb').write(response.body)
