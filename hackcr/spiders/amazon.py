# -*- coding: utf-8 -*-
import scrapy
from scrapy import log

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["www.amazon.com"]
    start_urls = []

    def start_requests(self):
	return	

    def parse(self, response):
        pass
