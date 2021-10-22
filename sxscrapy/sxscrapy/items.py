# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SxscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    lowest_ask = scrapy.Field()
    highest_bid = scrapy.Field()
    number_of_sales = scrapy.Field()
    release_date = scrapy.Field()
    pixel_height = scrapy.Field()
    chart_height = scrapy.Field()
    data = scrapy.Field()