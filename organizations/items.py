# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OrganizationItem(scrapy.Item):
    name = scrapy.Field()
    phone = scrapy.Field()
    address = scrapy.Field()
    rating = scrapy.Field()
