# -*- coding: utf-8 -*-
# Author --- 百川 ---
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
import json
import re


class CnComJszbWwwSpider(scrapy.Spider):
	# 江苏省建设工程招标网

    name = "cn.com.jszb.www"
    allowed_domains = ["www.jszb.com.cn"]
    # start_urls = ['http://www.jszb.com.cn/jszb/YW_info/ZhaoBiaoGG/MoreInfo_ZBGG.aspx?categoryNum=012',]

    start_urls = ['http://www.jszb.com.cn/jszb']


    req_type = ["ZhaoBiaoGG/MoreInfo_ZBGG.aspx",
                "ZuiGaoXJ/MoreInfo_ZGXJ.aspx",
                "ZiGeYS/MoreInfo_ZGYS.aspx",
                "HouXuanRenGS/MoreInfo_HxrGS.aspx",
                "ZhongBiaoGS/MoreInfo_ZBGS.aspx",
                "OtherInfo/MoreInfo_Zjfb.aspx",
                "DBJieGuoGS/MoreInfo_DBJieGuoGS.aspx"]

    category = ["招标公告","最高限价公示","未入围公示","中标候选人公示","中标人公告","其他信息公告","评标、定标结果公示"]
    industry = ["房屋建筑施工","市政工程施工","单独装饰装修施工","园林绿化","工程监理","设计","材料设备采购","电力","水利","机电设备","其它","招标终止"]
    
    def start_requests(self):
        print('@___________________________________ start_requests fire ____________')
        for index,type_url in enumerate(self.req_type):
            # print('http://www.jszb.com.cn/jszb/YW_info/'+type_url+'?categoryNum=012')
            # print(index)
            # print(self.category[index])
            type = self.category[index]
            yield Request('http://www.jszb.com.cn/jszb/YW_info/'+type_url+'?categoryNum=012', callback=self.request_category,meta={"type":type})


    def request_category(self, response):
        # print('***************'+response.meta['type']+'***************')
        if response.meta['type']=='招标公告' or response.meta['type']=='未入围公示':
            for tr in response.xpath("/html/body/form[@id='form1']/table[@class='tab'][3]/tr/td[4]/table/tr[@id='show01']/td[@class='border2']/table[@id='MoreInfoList1_moreinfo']/tr[4]/td[@id='MoreInfoList1_tdcontent']/table[@id='MoreInfoList1_DataGrid1']/tr[@class='moreinfoline']").extract():
                # print(tr)
                # print('-------------')
                # Title
                title = Selector(text=tr).xpath('//td[2]/a/text()').extract()[0]
                title = title.split(']')[1]
                city = Selector(text=tr).xpath('//td[2]/a/text()').extract()[0]
                city = city.split(']')[0]
                city = city.split('[')[1]
                city = '江苏'+city
                # print(city)
                
                # Detail url
                onlickstr = Selector(text=tr).xpath('//td[2]/a/@onclick').extract()[0]
                onlickstr = onlickstr.split('..')[1]
                onlickstr = onlickstr.split('"')[0]
                detailurl = 'http://www.jszb.com.cn/jszb/YW_info'+onlickstr
                # Type
                type = response.meta['type']
                # Category
                category = Selector(text=tr).xpath('//td[3]/text()').extract()[0]
                # issue_at(发布时间)
                issue_at = Selector(text=tr).xpath('//td[4]/text()').extract()[0]
        
                yield Request(detailurl, callback=self.parse_item,meta={"title":title,"type":type,"category":category,"issue_at":issue_at,"city":city,"detailurl":detailurl})

        elif response.meta['type']=='最高限价公示':
            for tr in response.xpath("/html/body/table[@class='tab'][3]/tr/td[4]/table/tr[2]/td[@class='border2']/form[@id='ctl00']/table[@id='MoreInfoList1_moreinfo']/tr[4]/td[@id='MoreInfoList1_tdcontent']/table[@id='MoreInfoList1_DataGrid1']/tr[@class='moreinfoline']").extract():
                # Title
                title = Selector(text=tr).xpath('//td[2]/a/text()').extract()[0]
                title = title.split(']')[1]
                city = Selector(text=tr).xpath('//td[2]/a/text()').extract()[0]
                city = city.split(']')[0]
                city = city.split('[')[1]
                city = '江苏'+city
                # print(city)
                
                # Detail url
                onlickstr = Selector(text=tr).xpath('//td[2]/a/@onclick').extract()[0]
                onlickstr = onlickstr.split('..')[1]
                onlickstr = onlickstr.split('"')[0]
                detailurl = 'http://www.jszb.com.cn/jszb/YW_info'+onlickstr
                # Type
                type = response.meta['type']
                # Category
                category = Selector(text=tr).xpath('//td[3]/text()').extract()[0]
                # issue_at(发布时间)
                issue_at = Selector(text=tr).xpath('//td[4]/text()').extract()[0]
        
                yield Request(detailurl, callback=self.parse_item,meta={"title":title,"type":type,"category":category,"issue_at":issue_at,"city":city,"detailurl":detailurl})

        elif response.meta['type']=='中标候选人公示':
            for tr in response.xpath("/html/body/table[@class='tab'][3]/tr/td[4]/table/tr[2]/td[@class='border2']/form[@id='ctl00']/table[@id='MoreInfoList1_moreinfo']/tr[4]/td[@id='MoreInfoList1_tdcontent']/table[@id='MoreInfoList1_DataGrid1']/tr[@class='moreinfoline']").extract():
                # Title
                title = Selector(text=tr).xpath('//td[2]/a/text()').extract()[0]
                title = title.split(']')[1]
                city = Selector(text=tr).xpath('//td[2]/a/text()').extract()[0]
                city = city.split(']')[0]
                city = city.split('[')[1]
                city = '江苏'+city
                # print(city)
                
                # Detail url
                onlickstr = Selector(text=tr).xpath('//td[2]/a/@onclick').extract()[0]
                onlickstr = onlickstr.split('..')[1]
                onlickstr = onlickstr.split('"')[0]
                detailurl = 'http://www.jszb.com.cn/jszb/YW_info'+onlickstr
                # Type
                type = response.meta['type']
                # Category
                category = Selector(text=tr).xpath('//td[3]/text()').extract()[0]
                # issue_at(发布时间)
                issue_at = Selector(text=tr).xpath('//td[4]/text()').extract()[0]
        
                yield Request(detailurl, callback=self.parse_item,meta={"title":title,"type":type,"category":category,"issue_at":issue_at,"city":city,"detailurl":detailurl})



        elif response.meta['type']=='中标人公告':
            for tr in response.xpath("/html/body/table[@class='tab'][3]/tr/td[4]/table/tr[2]/td[@class='border2']/form[@id='ctl00']/table[@id='MoreInfoList1_moreinfo']/tr[4]/td[@id='MoreInfoList1_tdcontent']/table[@id='MoreInfoList1_DataGrid1']/tr[@class='moreinfoline']").extract():
                # Title
                title = Selector(text=tr).xpath('//td[2]/a/text()').extract()[0]
                title = title.split(']')[1]
                city = Selector(text=tr).xpath('//td[2]/a/text()').extract()[0]
                city = city.split(']')[0]
                city = city.split('[')[1]
                city = '江苏'+city
                # print(city)
                
                # Detail url
                onlickstr = Selector(text=tr).xpath('//td[2]/a/@onclick').extract()[0]
                onlickstr = onlickstr.split('..')[1]
                onlickstr = onlickstr.split('"')[0]
                detailurl = 'http://www.jszb.com.cn/jszb/YW_info'+onlickstr
                # Type
                type = response.meta['type']
                # Category
                category = Selector(text=tr).xpath('//td[3]/text()').extract()[0]
                # issue_at(发布时间)
                issue_at = Selector(text=tr).xpath('//td[4]/text()').extract()[0]
        
                yield Request(detailurl, callback=self.parse_item,meta={"title":title,"type":type,"category":category,"issue_at":issue_at,"city":city,"detailurl":detailurl})



        elif response.meta['type']=='其他信息公告':
            for tr in response.xpath("/html/body/table[@class='tab'][3]/tr/td[4]/table/tr[2]/td[@class='border2']/form[@id='ctl00']/table[@id='MoreInfoList1_moreinfo']/tr[4]/td[@id='MoreInfoList1_tdcontent']/table[@id='MoreInfoList1_DataGrid1']/tr[@class='moreinfoline']").extract():
                # Title
                title = Selector(text=tr).xpath('//td[2]/a/text()').extract()[0]
                title = title.split(']')[1]
                city = Selector(text=tr).xpath('//td[2]/a/text()').extract()[0]
                city = city.split(']')[0]
                city = city.split('[')[1]
                city = '江苏'+city
                # print(city)
                
                # Detail url
                onlickstr = Selector(text=tr).xpath('//td[2]/a/@onclick').extract()[0]
                onlickstr = onlickstr.split('..')[1]
                onlickstr = onlickstr.split('"')[0]
                detailurl = 'http://www.jszb.com.cn/jszb/YW_info'+onlickstr
                # Type
                type = response.meta['type']
                # Category
                category = Selector(text=tr).xpath('//td[3]/text()').extract()[0]
                # issue_at(发布时间)
                issue_at = Selector(text=tr).xpath('//td[4]/text()').extract()[0]
        
                yield Request(detailurl, callback=self.parse_item,meta={"title":title,"type":type,"category":category,"issue_at":issue_at,"city":city,"detailurl":detailurl})



        elif response.meta['type']=='评标、定标结果公示':
            for tr in response.xpath("/html/body/table[@class='tab'][3]/tr/td[4]/table/tr[2]/td[@class='border2']/form[@id='ctl00']/table[@id='MoreInfoList1_moreinfo']/tr[4]/td[@id='MoreInfoList1_tdcontent']/table[@id='MoreInfoList1_DataGrid1']/tr[@class='moreinfoline']").extract():
                # Title
                title = Selector(text=tr).xpath('//td[2]/a/text()').extract()[0]
                # City
                title = title.split(']')[1]
                city = Selector(text=tr).xpath('//td[2]/a/text()').extract()[0]
                city = city.split(']')[0]
                city = city.split('[')[1]
                city = '江苏'+city
                # print(city)
                
                # Detail url
                onlickstr = Selector(text=tr).xpath('//td[2]/a/@onclick').extract()[0]
                onlickstr = onlickstr.split('..')[1]
                onlickstr = onlickstr.split('"')[0]
                detailurl = 'http://www.jszb.com.cn/jszb/YW_info'+onlickstr
                # Type
                type = response.meta['type']
                # Category
                category = Selector(text=tr).xpath('//td[3]/text()').extract()[0]
                # issue_at(发布时间)
                issue_at = Selector(text=tr).xpath('//td[4]/text()').extract()[0]
        
                yield Request(detailurl, callback=self.parse_item,meta={"title":title,"type":type,"category":category,"issue_at":issue_at,"city":city,"detailurl":detailurl})


    def parse_item(self, response):
        # print("********************Detail*************************")
        data = {}
        data['title'] = response.meta['title']
        data['type'] = response.meta['type']
        data['category'] = re.sub(r'[\n\t]+','\n',response.meta['category']).strip()
        data['issue_at'] = re.sub(r'[\n\t]+','\n',response.meta['issue_at']).strip()

        data['city'] = response.meta['city']
        data['detailurl'] = response.meta['detailurl']

        
        # print(data)
        return data




