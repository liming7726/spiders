# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class QchachaSpider(scrapy.Spider):
    name = 'QChaCha'
    allowed_domains = ['www.qichacha.com']
    start_urls = ['https://www.qichacha.com/g_AH.html/']
    BASE_URL = 'https://www.qichacha.com'

    def parse(self, response):
        # 获取所有地区的企业列表
        if response.url == 'https://www.qichacha.com/g_AH.html/':
            area_list = response.css('.pills-after')[0].xpath('./a/text()')
            for p_url in area_list:
                yield Request(self.BASE_URL + p_url, priority=10)
        # 获取当前页面的企业详情页面的url
        for tr_ in response.css('.m_srchList tr'):
            info_url = tr_.css('a::attr("href")').get()
            yield Request(self.BASE_URL + info_url, callback=self.parse_detail, priority=100)

        # 获取下一页的url
        next_page = response.css('.next::attr("href")').get()
        yield Request(self.BASE_URL + next_page, priority=50)

    def parse_detail(self, response):
        #企业名称，电话，地址，运营状态，成立时间。纳税人识别号，经营者，统一社会信用代码，所属地区，经营范围



        pass

