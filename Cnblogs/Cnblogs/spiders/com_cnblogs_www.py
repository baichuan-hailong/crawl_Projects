# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from Cnblogs.items import DocItem
from scrapy.selector import Selector


class ComCnblogsWwwSpider(scrapy.Spider):
    name = "com_cnblogs_www"
    allowed_domains = ["www.cnblogs.com"]
    start_urls = ['http://www.cnblogs.com/']

    


    def parse(self, response):
    	for i in range(1,200):
    		# print(i)
    		# print(response.url+'#p'+str(i))
    		yield Request(response.url+'#p'+str(i), callback=self.parse_cate,dont_filter=True)

	    	# print('###################################################################')
	    	# print(response.url)
	    	# print('###################################################################')
	    	# print(response.body)
    	
	    	# /html/body/div[@id='wrapper']/div[@id='main']/div[@id='post_list']/div[@class='post_item'][1]/div[@class='post_item_body']/h3/a[@class='titlelnk']
	        # pass

    # /div[@class='post_item'][1]/div[@class='post_item_body']/h3/a[@class='titlelnk']
    def parse_cate(self,response):
    	print('##################----------------######################################')
    	for div in response.xpath('/html/body/div[@id]/div[@id]/div[@id]/div[@class]').extract():
    		data = {}
    		print(data)
            # data['title'] = Selector(div).xpath('//div[1]/div[@class]/h3/a[@class]/text()').extract()[0]
            # data['detail_url'] = Selector(text=div).xpath('//div/@href').extract()[0]
            

        	
