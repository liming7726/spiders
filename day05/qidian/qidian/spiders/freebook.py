# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse


class FreebookSpider(scrapy.Spider):
    name = 'freebook'
    allowed_domains = ['www.qidian.com']
    start_urls = ['https://www.qidian.com/free/all']

    def parse(self, response : HtmlResponse):
        #解析start_urls页面的数据,response的类型为HtmlResponse
        if response.status == 200:
            with open('qidian.html','w') as f :
                f.write(response.text)
                li_nodes= response.css('.all-img-list li')  #list列表中的selector的类
                for li in li_nodes:
                    item = {}
                    item['name'] = li.css('h4 a').xpath('./text()').extract_first()
                    item['author'] = li.css('.name').xpath('./text()').get()
                    info_url = li.css('.book-img-box a::attr("href")').get()
                    item['info_url'],item['img_url'] = li.css('.book-img-box a').xpath('./@href | ./img/@src').extract()
                    # item['type'] = li.css('.go-sub-type').extract_first()
                    item['type'],item['stype'],item['sstype'] = li.css('.author').xpath('./a[position()>1]/text() | ./span/text()').extract()
                    item['intro'] =  li.css('.intro::text').extract_first()


                    print(item)
                    yield item
                    next_page = response.css('.lbf-pagination-next::attr("href")')
                    yield Request('https:'+next_page,dont_filter=True)



    def parse_detail(self):
        pass

