import scrapy
from scrapy import Selector

from spider2022.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        sel = Selector(response)
        listitems = sel.css('#content > div > div.article > ol > li')
        for list_item in listitems:
            movieitem = MovieItem()
            movieitem['title'] = list_item.css('span.title::text').extract_first()
            movieitem['rank'] = list_item.css('span.rating_num::text').extract_first()
            movieitem['subject'] = list_item.css('span.inq::text').extract_first()
            yield movieitem

