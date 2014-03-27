from scrapy.spider import Spider

class ExampleSpider(Spider):
    name = "demo_2"
    allowed_domains = ["example.com"]
    start_urls = (
        'http://www.example.com/',
        )

    def parse(self, response):
        pass 
