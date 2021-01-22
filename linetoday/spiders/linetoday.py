
from linetoday.items import PostItem
from bs4 import BeautifulSoup
import scrapy
import time


class LinetodaySpider(scrapy.Spider):
    name = 'linetoday' #scrapy crawl linetoday -o output.json
    start_urls = ['https://today.line.me/tw/v2/tab/domestic']

    def parse(self, response):
        # item['url'] = response.css("a.articleCard articleCard--horizontal::attr(href)")[0].extract()
        # item['title'] = response.css("a::attr(href)")[0].extract()
        # item['source'] = response.css("a::attr(href)")[0].extract()
        
        item = PostItem()
        soup = BeautifulSoup(response.text,'lxml')
        post_list = soup.find_all('a',class_='articleCard articleCard--horizontal')
        for i in post_list:
            temp = i.getText().split('\n')[1:]
            item['title'] = temp[0].replace(' ','')
            item['source'] = temp[1].replace(' ','')
            item['url'] = i['href']
            yield item
