import scrapy
import json  

class Spider(scrapy.Spider):
    name = "gdpr"
    allowed_domains = ["gdpr-info.eu"]
    start_urls = ["https://gdpr-info.eu/art-1-gdpr/"]

    def parse(self, response):
        title = response.css('h1.entry-title > span::text').getall()
        list_items = response.css('div.entry-content > ol > li::text').getall()

        yield {
            'url': response.url,
            'article_title': " ".join(title),
            'content': " ".join(list_items)
        }
