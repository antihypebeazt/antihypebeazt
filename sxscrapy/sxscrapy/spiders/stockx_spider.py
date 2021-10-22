import os
import scrapy
from ..items import SxscrapyItem
from selenium import webdriver
import time
import re
from scrapy.crawler import CrawlerProcess
from scrapy import Spider, Request


class StockXSpider(scrapy.Spider):
    name = 'sx'
    start_urls = [
        'https://stockx.com/adidas-yeezy-boost-350-v2-cinder-reflective',
        # 'https://stockx.com/adidas-yeezy-boost-350-v2-linen'
    ]

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://accounts.stockx.com/login')
        time.sleep(4)
        self.driver.find_element_by_id("email-login").send_keys("gabiospi321@gmail.com")
        self.driver.find_element_by_id("password-login").send_keys("LitMari757")
        self.driver.find_element_by_id("btn-login").click()
        time.sleep(5)

    def parse(self, response):
        self.driver.get(response.url)
        res = response.replace(body=self.driver.page_source)
        time.sleep(6)

        items = SxscrapyItem()
        all_div_blanks = res.css('div.product-header-media')

        for blanks in all_div_blanks:
            product_name = res.css('div.col-md-12').xpath('//h1/text()')[0].extract()
            lowest_ask = res.css('div.en-us.stat-value.stat-small::text')[0].extract()
            highest_bid = res.css('div.en-us.stat-value.stat-small::text')[1].extract()
            number_of_sales = res.css('div.gauge-value::text')[0].extract()
            release_date = res.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/span/div[2]/div[4]/div/div[4]/span/text()')[0].extract()
            pixel_height = res.css('rect.highcharts-plot-background::attr(height)')[0].extract()
            chart_height = res.xpath('//text[@y=-9999]/text()').get()
            data = res.css('path.highcharts-area::attr(d)')[0].extract()

            ph1 = float(pixel_height)
            ch1 = float(chart_height)
            data2 = self.cvar(ph1, ch1, data)

            items['product_name'] = product_name
            items['lowest_ask'] = lowest_ask
            items['highest_bid'] = highest_bid
            items['number_of_sales'] = number_of_sales
            items['release_date'] = release_date
            items['pixel_height'] = pixel_height
            items['chart_height'] = chart_height
            items['data'] = data2

            yield items

    def cvar(self, ph, ch, dt):
        pattern = re.compile(r"[A-Z] (\d*\.?\d*) (\d*\.?\d*) ")

        matches = re.findall(pattern, dt)

        coordinates = list()
        for x, y in matches:
            y = (ch - (ch / ph)*float(y))
            x = float(x)
            coordinates.append((x, y))

        return coordinates
