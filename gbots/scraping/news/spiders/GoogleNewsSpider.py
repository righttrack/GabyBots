__author__ = 'jeffmay'

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from scraping.news.spiders import ArticleSpider
from scraping.news.items import ArticleItem

class GoogleNewsSpider(ArticleSpider):
    name = 'google-news'
    allowed_domains = ['news.google.com']
    start_urls = ['http://news.google.com/']
    # https://news.google.com/news/feeds?pz=1&cf=all&ned=us&hl=en&topic=w&output=rss

    rules = (
        Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        )

    def parse_item(self, response, xs=None):
        # TODO: Call super to get article?
        hxs = HtmlXPathSelector(response)
        i = ArticleItem()
        i['title'] = hxs.select('//div[@class="story_headline"]/h1').extract()
        i['description'] = hxs.select('//div[@id="description"]').extract()
        return i
