# Scrapy settings for mega_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mega_spider'

SPIDER_MODULES = ['mega_spider.spiders']
NEWSPIDER_MODULE = 'mega_spider.spiders'

ITEM_PIPELINES = {
        #'mymodules.pipelines.FilterWordsPipeline':543,
       'mega_spider.pipelines.DuplicatesPipeline':500,
                    
}

DOWNLOAD_DELAY = 0
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True

SCHEDULER_ORDER = 'BFO'

DEPTH_PRIORITY = 0
DEPTH_LIMIT = 2
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mega_spider (+http://www.yourdomain.com)'

# setting mongodb args
DB_NAME = 'blog'
COLLECTION_NAME = 'siteTables'
