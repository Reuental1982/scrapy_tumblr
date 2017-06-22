# -*- coding: utf-8 -*-

# Scrapy settings for tumblr_video project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tumblr_video'

SPIDER_MODULES = ['tumblr_video.spiders']
NEWSPIDER_MODULE = 'tumblr_video.spiders'


USER_AGENTS = [
 "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36",
 "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0)"
]
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

RETRY_TIMES = 3

DOWNLOAD_DELAY = 0.5


AUTOTHROTTLE_START_DELAY =3

DOWNLOADER_MIDDLEWARES = {
    'tumblr_video.middlewares.RandomUserAgent': 1,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 20,
}

ITEM_PIPELINES = {
   'tumblr_video.pipelines.TumblrVideoPipeline': 300,
}


