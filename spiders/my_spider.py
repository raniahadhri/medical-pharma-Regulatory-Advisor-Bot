import scrapy
import os
import json

class GdprSpider(scrapy.Spider):
    name = "gdpr"
    allowed_domains = ["gdpr-info.eu"]
    start_urls = ["https://gdpr-info.eu/art-1-gdpr/"]

    def parse(self, response):
        article_title = response.css('h1::text').get()
        article_text = response.css('.entry-content p::text').getall()

        yield {
            "url": response.url,
            "title": article_title,
            "content": " ".join(article_text),
        }

        # Follow other article links
        for href in response.css('li a::attr(href)').getall():
            if "/art-" in href:
                yield response.follow(href, self.parse)
