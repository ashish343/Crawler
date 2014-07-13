# -*- coding: utf-8 -*-
import scrapy
from scrapy import log
from scrapy.selector import Selector
from scrapy.spider import Spider

file_name='seller_asin_list';

class AmazonListSpider(Spider):
    name = "amazon_list"
    allowed_domains = ["www.amazon.in"]

    def __init__(self):

	self.start_urls = []
        for ix in range(20):
	    self.start_urls.append('http://www.amazon.in/gp/aag/ajax/productWidget.html?seller=AZL93SHLUWFMN&currentPage=' + str(ix+1));
		
    def parse(self, response):
	
	sel = Selector(response)
        asins = sel.xpath('//*[@id="AAGProductWidgetButtonWrapper"]/div/ul/li/ul/li')

        f = open('seller_asin_list', 'a')
        for asin in asins:
            link = asin.xpath('a/@href').extract()
	    if link and link[0]:
   	        f.write(link[0] + "\n")
        f.close()
