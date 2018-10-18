# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json, io, codecs, os
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals

class BeevaPipeline(object):

    def __init__(self):
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_opened(self, spider):
        self.filename = '%s_output.json' % "ecommerce"
        self.file = codecs.open(self.filename, 'w', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        if len(item['images']) > 0:
            line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
            self.file.write(line)
            return item
        else:
            return

    def spider_closed(self, spider):
        self.file.seek(-2, os.SEEK_END)
        self.file.truncate()
        self.file.write(']')
        self.file.close()


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
