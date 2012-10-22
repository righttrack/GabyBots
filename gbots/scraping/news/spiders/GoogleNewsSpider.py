from bs4 import BeautifulSoup
from dynamic_scraper.spiders.django_spider import DjangoSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from scraping.news.spiders import ArticleSpider
from util.strings import clean_control_chars

__author__ = 'jeffmay'

class GoogleNewsSpider(ArticleSpider):
    name = 'google-news'
    allowed_domains = ['news.google.com']
    start_urls = ['http://news.google.com/?ned=us&hl=en&output=rss']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response, *args, **kwargs):
        article = super(GoogleNewsSpider, self).parse_item(response, *args, **kwargs)
        soup = BeautifulSoup(article['description'])
        clean_description = "\n".join(clean_control_chars(string) for string in soup.stripped_strings)
        article['description'] = clean_description
        return article
