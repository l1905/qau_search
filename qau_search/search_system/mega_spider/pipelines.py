import os

from pybloomfilter import BloomFilter
from pymongo import Connection

from scrapy.exceptions import DropItem

class MegaSpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline(object):
    def __init__(self):
        self.conn = Connection()
        self.db = self.conn.blog
        self.siteTables = self.db.siteTables 
        self.bf = BloomFilter(100000000, 0.01, 'filter.bloom')
        self.f_write = open('visitedsites','w')

    def process_item(self, item, spider):
        print '***********%d pages visited! *********'%len(self.bf)
        if self.bf.add(item['web_urls']):
            raise DropItem("Duplicate item found: %s"%item)
        else:
            self.save_to_visited(item['web_urls'], item['title'], item['content'])
            return item

    def save_to_visited(self, url, utitle,content):
        self.siteTables.insert({"url":url,"title":utitle.encode('utf-8'), "content": content.encode('utf-8')})
        self.f_write.write(url)
        self.f_write.write('\t')
        self.f_write.write(utitle.encode('utf-8'))
        self.f_write.write('\n')
    def __del__(self):
        self.f_write.close()

