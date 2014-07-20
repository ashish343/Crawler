# -*- coding: utf-8 -*-
import scrapy
from scrapy import log
from scrapy.selector import Selector
from scrapy.spider import Spider
import re

class AmazonSpider(Spider):
    name = "amazon" 
    allowed_domains = ["www.amazon.in"]
    
    def __init__(self):

        self.start_urls = []
	for ix in range(100):
   	    self.start_urls.append('http://www.amazon.in/gp/aag/ajax/paginatedFeedback.html?seller=AQWKOB3TGIWJN&currentPage=' + str(ix))

    def parse(self, response):
	sel = Selector(response)
	#asinRegex = re.match(".*asin=(.*)", response.url)
	#finalASIN = str(asinRegex.groups(1))[2:12]
	f  = open('customer_reviews', 'a')
	reviewsList = sel.xpath('/html/body/li')
	reviews = reviewsList.xpath('ul/li[2]//text()').extract()
	for review in reviews:
	 #   data = review.xpath('//text()').extract()
	    #print data
	  #  if data:
		#f.write("%s\n" % data[0])
	#	for item in data:
	     f.write("%s" % review)
	f.close()
