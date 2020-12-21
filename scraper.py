# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess


class MuratorScraper(scrapy.Spider):
    name = 'PHScraper'

    def start_requests(self):
        yield scrapy.Request(url='https://www.muratorplus.pl/', callback=self.parse)

    def parse(self, response):
        rank = dict()
        titles_list = response.xpath('/html/body/section[2]/div/section[2]/div/div/div[1]/div/div//div[@class="element__headline"]/a/@title').extract()
        for title in titles_list:
            print(title)
            for word in title.split():
                word = word.strip().lower()
                if len(word) < 2:
                    continue
                elif word[-1] in ['?','.','!']:
                    word = word[:-1]
                try:
                    rank[word] += 1
                except KeyError:
                    rank[word] = 1
        for word, number in sorted(rank.items(), key=lambda x:x[1], reverse=True):
            if number > 2:
                print(word, ": ", number)

process = CrawlerProcess()
process.crawl(MuratorScraper)
process.start()
