# -*- coding: utf-8 -*-

# Scrapy settings for tumblr_picture project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os

PROJECT_DIR= os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

BOT_NAME = 'tumblr_picture'

SPIDER_MODULES = ['tumblr_picture.spiders']
NEWSPIDER_MODULE = 'tumblr_picture.spiders'


USER_AGENTS = [
 "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36",
 "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0)"
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

RETRY_TIMES = 3

DOWNLOAD_DELAY = 1


DOWNLOADER_MIDDLEWARES = {
    'tumblr_picture.middlewares.RandomUserAgent': 1,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 20,
}

ITEM_PIPELINES = {
   'tumblr_picture.pipelines.TumblrPicturePipeline': 300,
}
IMAGES_STORE='%s/picture' % PROJECT_DIR
IMAGES_MIN_HEIGHT = 500
IMAGES_MIN_WIDTH = 500


AUTOTHROTTLE_START_DELAY =3

