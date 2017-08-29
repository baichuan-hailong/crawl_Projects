# -*- coding: utf-8 -*-
import scrapy


class CnComJszbWwwSpider(scrapy.Spider):
    name = "cn.com.jszb.www"
    allowed_domains = ["www.jszb.com.cn"]
    start_urls = ['http://www.jszb.com.cn/']
    # 江苏省建设工程招标网
    # 招标公告 最高限价公示 未入围公示 中标候选人公示 中标人公告  其他信息公告  评标、定标结果公示
    # 房屋建筑施工
    # 市政工程施工
    # 单独装饰装修施工
    # 园林绿化
    # 工程监理
    # 设计
    # 材料设备采购
    # 电力
    # 水利
    # 机电设备
    # 其它
    def parse(self, response):
        pass
