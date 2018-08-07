# -*- coding: utf-8 -*-
import scrapy
from Shenpi.items import ShenpiItem

#爬取民用爆炸物品进出口审批
class CivilSpider(scrapy.Spider):
    name = "civil"    #爬虫名称
    star_urls=('http://shenpi.miit.gov.cn/')    #爬虫网页地址

    def start_requests(self):   #定义函数，要爬取得多个页面
        reqs=[]

        for i in range(2,3): #页面总共208页
            req=scrapy.Request("http://shenpi.miit.gov.cn/resultSearch?wd=&categoryTreeId=321&categoryTreePid=&pagenow=%s"%i)
            reqs.append(req)

        return reqs

    def parse(self, response):  #对爬取得网页进行分析，提取想要的部分
        ip_list=response.xpath('//div[@class="col-md-9"]/table/tbody')
        trs=ip_list[0].xpath('tr')
        items=[]

        for cv in trs[0:]:
            pre_item=ShenpiItem()

            pre_item['compay']=cv.xpath('normalize-space(td[2]/text())').extract()
            pre_item['carNo']=cv.xpath('normalize-space(td[3]/text())').extract()
            pre_item['data']=cv.xpath('td[4]/text()').extract()
            pre_item['state']=cv.xpath('normalize-space(td[5]/text())').extract()

            items.append(pre_item)
        return items



