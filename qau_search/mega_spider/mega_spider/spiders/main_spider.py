#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import urllib
import re

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from mega_spider.items import MegaSpiderItem

logging.basicConfig(level=logging.DEBUG,filename='spider.log')
logger = logging.getLogger('MAIN-SPIDER')
class DmoSpider(Spider):
    name = "demo"
    # allowed_domains = ['qau.edu.cn']
    # start_urls = [
    #     "http://www.qau.edu.cn/"
    # ]
    allowed_domains = ['qust.edu.cn']
    start_urls = [
        "http://www.qust.edu.cn/"
    ]

    def parse(self, response):
        sel = Selector(response)
        # sites = sel.xpath('//dd/li/a')
        # items = []
        # # for site in sites:
        # #     item = MegaSpiderItem()

        # #     item['title'] = [one.encode('utf-8') for one in site.xpath('@title').extract()]
        # #     # item['title'] = site.xpath('a/@title').extract()
        # #     item['link'] = site.xpath('@href').extract()
        # #     items.append(item)
        # # return items

        # for title,link in zip(sel.xpath('//dd/li/a/@title').extract(),sel.xpath('//dd/li/a/@href').extract()):
        #     item = MegaSpiderItem()
        #     item['title'] = title.encode('utf-8')
        #     item['link'] = link.encode('utf-8')
        #     items.append(item)
        # return items
        # # filename = response.url.split("/")[-1]
        # # open(filename,'wb').write(response.body)

        ex_links = sel.xpath('//@href').extract()
        item = MegaSpiderItem()
        item['web_urls'] = response.url
        item['title'] = '0'
        if len(sel.xpath('/html/head/title/text()').extract()):
            item['title'] = sel.xpath('/html/head/title/text()').extract()[0]

        content = ''
        resp_text = sel.xpath('/html/body//*/text()').extract()
        for one in resp_text:
            content += one.strip() 
            content += ''
        item['content'] = content

        yield item

        for link in ex_links:
            utf8_url = link.encode('utf-8')
            postfix = re.compile(r'.+\.((jpg)|(ico)|(rar)|(zip)|(doc)|(ppt)|(xls)|(css)|(exe)|(pdf))x?$')
            prefix = re.compile(r'^((javascript:)|(openapi)).+')

            if postfix.match(utf8_url):
                continue
            if prefix.match(utf8_url):
                continue
            if not utf8_url.startswith('http://'):
                link = 'http://'+self.get_hostname(response.url)+'/'+link
            link = re.sub(r'/\.\./\.\./',r'/',link)
            link = re.sub(r'/\.\./',r'/',link)

            yield Request(link,callback=self.parse)

    def get_hostname(self,resp_url):

        proto, rest = urllib.splittype(resp_url)
        host, rest = urllib.splithost(rest)
        return host


