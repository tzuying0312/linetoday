
from linetoday.items import PostItem
from bs4 import BeautifulSoup
from datetime import datetime
import scrapy
import time


class LinetodaySpider(scrapy.Spider):
    name = 'linetoday' #scrapy crawl linetoday -o output.json
    start_urls = ['https://today.line.me/tw/v2/tab/domestic']

    def parse(self, response):  
        item = PostItem()
        content = response.css('script:nth-child(2)::text')[0].extract()
        publishTime_list = (content.replace('publishTimeUnix:','  ').split('  '))[-3:]
        for i,post in enumerate(response.css('section > div > a')):
            item['title'] = (post.css('div.articleCard-content > span::text')[0].extract()).replace(' ','').replace('\n','')
            item['source'] = post.css('div.articleCard-content > div > span::text')[0].extract()
            timestamp = publishTime_list[i].split('000,contentType')[0]
            item['time'] = datetime.fromtimestamp(int(timestamp))
            item['url'] = post.css('a::attr(href)')[0].extract()
            yield item

        # item = PostItem()
        # soup = BeautifulSoup(response.text,'lxml')
        # post_list = soup.find_all('a',class_='articleCard articleCard--horizontal')
        # for i in post_list:
        #     temp = i.getText().split('\n')[1:]
        #     item['title'] = temp[0].replace(' ','')
        #     item['source'] = temp[1].replace(' ','')
        #     item['url'] = i['href']
        #     yield item
