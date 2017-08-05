#-*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.cookies import CookieJar
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
from tumblr_picture.items import TumblrPictureItem
from scrapy.linkextractors import LinkExtractor as sle
import random
import requests
import json
import re
import datetime
import time
import urlparse



class PictureSpider(CrawlSpider) :
    name = "picture"
    allowed_domains = ["tumblr.com"]
    start_urls = [
        "https://nanue1.tumblr.com/",
    ]
    rules = [
        #Rule(sle(allow=(r"/likes")),callback='parse_likes',follow = True),
        #Rule(sle(allow=(r"/likes")),callback='parse_likes'),
        Rule(sle(allow=(r"/following")),callback='parse_following',follow = True),
        Rule(sle(allow=(r"/archive")),callback='parse_archive',follow=True),
    ]

    def get_archive_post_pic(self, response):
        print "Parse archive post page for pic......"
        #pic_page_urls=re.findall('https://\d+.media.tumblr.com/\S+/\S+_\d+.jpg',response.body)
        pic_page_urls=re.findall('https://\d+.media.tumblr.com/\S+/\S+_1280.jpg',response.body)
        if pic_page_urls :
            item = TumblrPictureItem()
            for pic_page_url in pic_page_urls :
                print pic_page_url
                item['url'] = [urlparse.urljoin(response.url, pic_page_url)]
                yield item

    def parse_archive(self, response):
        print "Parse archive......"
        print response.url
        archive_post_urls = response.xpath('//*[@class="hover"]/@href').extract()
        for archive_post_url  in archive_post_urls:
            req = Request(archive_post_url,dont_filter=True, callback = self.get_archive_post_pic)
            yield req
    def parse_following(self, response):
        print "Parse following user......"
        follows_blog_urls = response.xpath('//*[@class="blog-name"]/@href').extract()
        for follow_blog_url in follows_blog_urls:
            req = Request(follow_blog_url,dont_filter=True)
            print follow_blog_url
            yield req
