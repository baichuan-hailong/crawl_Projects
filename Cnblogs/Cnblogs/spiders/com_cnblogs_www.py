# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from Cnblogs.items import DocItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class ComCnblogsWwwSpider(scrapy.Spider):
    name = "com_cnblogs_www"
    allowed_domains = ["www.cnblogs.com"]
    start_urls = ['http://www.cnblogs.com/']

    

    def start_requests(self):
    	for i in range(1,200):
    		yield Request('http://www.cnblogs.com/'+'#p'+str(i), callback=self.parse_cate,dont_filter=True)
    		# print(i)
    		print('http://www.cnblogs.com/'+'#p'+str(i))


    def parse(self, response):
	    	print('###################################################################')
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
    		# data['title'] = Selector(text=div).xpath('//div/div/h3/a/@href').extract()[0]
    		# data['title'] = div.xpath('/div/div/h3/a/@href')
    		# data['title'] = response.xpath('/html/body/div[@id]/div[@id]/div[@id]/div[@class][1]/div[@class]/h3/a[@class]/text()').extract()[0]
    		data['title'] = Selector(text=div).xpath('//h3/a/text()').extract()
    		print(data)

            # data['detail_url'] = Selector(text=div).xpath('//div/@href').extract()[0]
            

            

        	
