# -*- coding: utf-8 -*-
import scrapy
from yjs_jobs.items import YjsJobsItem

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['www.yuanjisong.com']
    start_urls = ['https://www.yuanjisong.com/job/']

    def parse(self, response):
        # xpath //*[@id="db_adapt_id"]/div[3]
        # selector #db_adapt_id > div:nth-child(3)
        #db_adapt_id > div:nth-child(3) > a
        # name = scrapy.Field()
        # address = scrapy.Field()
        # detail = scrapy.Field()
        # employer = scrapy.Field()
        # daily_salary = scrapy.Field()
        # days = scrapy.Field()
        # total_salary = scrapy.Field()
        # appoint = scrapy.Field()
        # employee_num = scrapy.Field()
        jobs = response.css('div.weui_panel.margin-top-2')
        for job in jobs:
            item = YjsJobsItem()
            item['name'] = job.css('div.topic_title::text').extract_first()
            item['address'] = ' '.join(job.css('span.item_pos::text').extract())
            item['detail'] = job.css('.media_desc_content_adapt > p::text').extract_first()
            item['employer'] = job.css('h4.weui_media_title::text').extract_first()
            item['daily_salary'] = job.css('span.rixin-text-jobs::text').extract_first()
            #db_adapt_id > div:nth-child(3) > div:nth-child(6) > div > p > span:nth-child(2)
            item['days'] = job.css('div:nth-child(6) > div > p > span:nth-child(2)::text').extract_first()
            item['total_salary'] = job.css('div:nth-child(7) > div > p > span:nth-child(2)::text').extract_first()
            item['appoint'] = job.css('div.weui_panel_bd.appoint_div > a::text').extract_first()
            #i_post_num_101668
            post_num = job.css('i.i_post_num::text').extract_first()
            if post_num is None:
                item['employee_num'] = '-1'
            else:
                item['employee_num'] = job.css('i.i_post_num::text').extract_first()
            yield item
        next = response.xpath('/html/body/div[2]/div[1]/nav/ul/li[8]/a/@href').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
