# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Hsi_tr_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Ranging = scrapy.Field()
    futuresQuan = scrapy.Field()

class w_Date_summary(scrapy.Item):
    BusiDate = scrapy.Field()
    DayClose = scrapy.Field()
    Ranging = scrapy.Field()
    futuresQuan = scrapy.Field()
