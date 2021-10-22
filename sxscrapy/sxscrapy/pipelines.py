import sqlite3
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SxscrapyPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("myproducts.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS products_tb""")
        self.curr.execute("""create table products_tb(
                        name text,
                        ask integer,
                        bid integer
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into products_tb values (?,?,?)""",(
            item['product_name'][0],
            item['product_name'][0],
            item['product_name'][0]
        ))
        self.conn.commit()
