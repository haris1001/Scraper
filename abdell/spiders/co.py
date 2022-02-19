# -*- coding: utf-8 -*-
import scrapy


class CoSpider(scrapy.Spider):
    name = 'co'
    allowed_domains = ['coc.com']
    start_urls = ['https://freieheilpraktiker.com/verband/heilpraktiker-suche']

    def parse(self, response):
        for data in response.xpath('//div[@class="map_item"]/div'):
            yield{
                'First Name': (data.xpath('normalize-space(./h4/a/text()[1])').get()).split(',')[0],
                'Last Name': (data.xpath('normalize-space(./h4/a/text()[1])').get()).split(',')[1],
                'Profession': (data.xpath('normalize-space(./h4/a/small/text())').get()),
                'Street Address': (data.xpath('normalize-space(./p/span[1]/text())').get()),
                # 'Full':data.xpath('normalize-space(./p/span[2]/text())').get(),
                'Zip Code': (data.xpath('normalize-space(./p/span[2]/text())').get()).split('\xa0')[0],
                'Location': (data.xpath('normalize-space(./p/span[2]/text())').get()).split('\xa0')[1:],
                'Country': (data.xpath('normalize-space(./p/span[3]/text())').get()),
                'Telephone': (data.xpath('normalize-space(./table//tr/td[contains(.,"Telefon")]/following::td[1]/text())').get()),
                'Email': (data.xpath('normalize-space(./table//tr/td[contains(.,"E-Mail")]/following::td[1]/a/text())').get()),
                'Web': (data.xpath('normalize-space(./table//tr/td[contains(.,"Web")]/following::td[1]/a/text())').get()),
                'Focus': data.xpath('./p/span[@class="badge"]/text()').extract(),
                
                
            }
