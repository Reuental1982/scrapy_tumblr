# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
import urllib
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

PROJECT_DIR= os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class TumblrVideoPipeline(object):
    def process_item(self, item, spider):
        resp = requests.get(item['url'],
                            stream=True,
                            timeout=50)
        file_dir = '%s/video/'%PROJECT_DIR 
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        file_name = '%s/%s' % (file_dir,item['url'].split('/')[-1])
        with open(file_name, 'wb') as fh:
            for chunk in resp.iter_content(chunk_size=1024):
                fh.write(chunk)
        return item
