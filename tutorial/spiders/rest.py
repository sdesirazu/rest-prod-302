import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class RestSpider(CrawlSpider):
    name = 'rest'
    allowed_domains = ['rest.com.au']
    start_urls = ['https://rest.com.au/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        redirect_url_list = response.meta.get('redirect_urls')
        self.logger.debug("-------------------srinivas-----------------")
        if redirect_url_list:
            item = {
                'orig' : redirect_url_list,
                'new' : response.request.url
            }
            print(response.request.url)
            print(redirect_url_list)
            yield item
