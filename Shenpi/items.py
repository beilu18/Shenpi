# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShenpiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #民用爆炸物品进出口审批
    compay=scrapy.Field()   # 进出口申请企业
    carNo=scrapy.Field()    #合同编号
    data=scrapy.Field()     #申请日期
    state=scrapy.Field()    #工信部审核状态

    #民用爆炸物品生产许可
    management=scrapy.Field()   #行业管理
    time=scrapy.Field()     #时间

    #第二、三、四类验收
    compay_name=scrapy.Field()  #企业名称
    chemical_class=scrapy.Field()   #监控化学品类别
    chemical_name=scrapy.Field()    #监控化学品名称
    capacity=scrapy.Field()         #产能

    # 第二、三、四类生产许可
    name=scrapy.Field()     #企业名称
    compayNo=scrapy.Field() #企业代码
    province=scrapy.Field() #省份
    chemicalName = scrapy.Field()  # 监控化学品名称
    chemicalNo=scrapy.Field()       #生产特别许可证书编号

