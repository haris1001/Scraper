# -*- coding: utf-8 -*-
import scrapy

import json
class ShopSpider(scrapy.Spider):
    name = 'shop'
    allowed_domains = ['shop.com']
    start_urls = ['https://trooperapi.trooper.be/api/public/shops?filters.page=2&filters.pageSize=12&language=NL']
    def start_requests(self):
        h = {
            'Accept': 'application/json, text/plain, */*'
        }
        for i in range(1,36):
            u = f'https://trooperapi.trooper.be/api/public/shops?filters.page={i}&filters.pageSize=100&language=NL'
            yield scrapy.Request(url = u, callback=self.parse, headers=h, dont_filter= True)
    def parse(self, response):
        # print(response.body)
        ele = json.loads(response.body)


        for a in ele:
            yield{
                'Name': a['name'],
                'GEM': a['comission'],
                'Logo': a['croppedLogoUrl'],
            }