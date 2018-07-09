# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YjsJobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    detail = scrapy.Field()
    employer = scrapy.Field()
    daily_salary = scrapy.Field()
    days = scrapy.Field()
    total_salary = scrapy.Field()
    appoint = scrapy.Field()
    employee_num = scrapy.Field()

