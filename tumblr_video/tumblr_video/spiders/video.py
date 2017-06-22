# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.cookies import CookieJar
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
from tumblr_video.items import TumblrVideoItem
from scrapy.linkextractors import LinkExtractor as sle
import random
import requests
import json
import re
import datetime
import time
import urlparse


class VideoSpider(CrawlSpider) :
    name = "video"
    allowed_domains = ["tumblr.com"]
    start_urls = [
        "https://nanue1.tumblr.com/",
    ]
    rules = [
        #Rule(sle(allow=(r"/likes")),callback='parse_likes',follow = True),
        Rule(sle(allow=(r"/likes")),callback='parse_likes'),
        #Rule(sle(allow=(r"/following")),callback='parse_following',follow = True),
        #Rule(sle(allow=(r"/following")),callback='parse_following'),
        #Rule(sle(allow=(r"/archive")),callback='parse_archive',follow=True),
        #Rule(sle(allow=(r"/archive")),callback='parse_archive'),
    ]



    def get_video_url(self,response):
        print "Get video url ......"
        arg_url = response.xpath('//video/source/@src').extract()[0].split('/')
        item = TumblrVideoItem()
        if len(arg_url) == 8:
            r_url = "https://vtt.tumblr.com/%s_%s.mp4" % (arg_url[-2],arg_url[-1])
        else:
            r_url = "https://vtt.tumblr.com/%s.mp4" % (arg_url[-1])
        print r_url
        item['url'] =  r_url
        yield item

    def get_archive_post_video(self, response):
        print "Parse archive post page for video......"
        print response.url
#        with open ('archive_post.html','w') as f:
#            f.write(response.body)
        video_page_urls=re.findall('https://www.tumblr.com/video/\S+/',response.body)
        if video_page_urls :
            for video_page_url in video_page_urls :
                req = Request(video_page_url,dont_filter=True, callback = self.get_video_url)
                yield req

    def parse_likes(self, response):
        print "Parse likes......"
        print response.url
        video_page_urls=re.findall('https://www.tumblr.com/video/\S+/',response.body)
        for video_page_url in video_page_urls :
            req = Request(video_page_url,dont_filter=True, callback = self.get_video_url)
            yield req

    def parse_archive(self, response):
        print "Parse archive......"
        print response.url
        archive_post_urls = response.xpath('//*[@class="hover"]/@href').extract()
        for archive_post_url  in archive_post_urls:
            req = Request(archive_post_url,dont_filter=True, callback = self.get_archive_post_video)
            yield req

    def parse_following(self, response):
        print "Parse following user......"
        follows_blog_urls = response.xpath('//*[@class="blog-name"]/@href').extract()
        for follow_blog_url in follows_blog_urls:
            req = Request(follow_blog_url,dont_filter=True)
            print follow_blog_url
            yield req

