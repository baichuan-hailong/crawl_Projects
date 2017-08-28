# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest


class CnSxzfcgWwwSpider(scrapy.Spider):
    name = "cn.sxzfcg.www"
    allowed_domains = ["http://www.sxzfcg.cn"]
    start_urls = ['http://www.sxzfcg.cn/view.php?nav=61']
    # http://www.sxzfcg.cn/view.php?nav=61&page=1


    # 招标公告
    # http://www.sxzfcg.cn/view.php?nav=61

    # 补充变更公告
    # http://www.sxzfcg.cn/view.php?nav=64

    # 中标公告
    # http://www.sxzfcg.cn/view.php?nav=67


    def parse(self, response):
        print('-----------------------------------------------')
        # print(response.url)

        currentPage  = response.xpath("/html/body/table[1]/tr/td[2]/table/tr[1]/td[@class='c_pt']/table/tr[2]/td/div[@class='zt3']/div[@class='pager']/strong/font/text()").extract()[0]
        nextPage     = int(currentPage)+1
        print(currentPage)
        print(nextPage)


        totalPage    = response.xpath("/html/body/table[1]/tr/td[2]/table/tr[1]/td[@class='c_pt']/table/tr[2]/td/div[@class='zt3']/div[@class='pager']/a[text()='最后一页 »']/@href").extract()[0]
        totalPage    = totalPage.split('=', 2)[2]
        print('total---'+totalPage)


        next_url = response.url.split('=',2)[0]+'='+response.url.split('=',2)[1]+'&page='+str(nextPage)
        next_url = 'http://www.sxzfcg.cn/view.php?nav=61&page='+str(nextPage)
        print(next_url)
        print('-----------------------------------------------')

        

        if (int(nextPage) < int(totalPage)):
            yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)
        # pass
