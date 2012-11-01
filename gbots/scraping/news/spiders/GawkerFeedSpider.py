from bs4 import BeautifulSoup
from dynamic_scraper.spiders.django_spider import DjangoSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from scraping.news.spiders import ArticleSpider
from util.strings import clean_control_chars

__author__ = 'coleman'   ## TODO Ask Jeff what this is and why pycharm automatically created it for my django project

class GawkerFeedSpider(ArticleSpider):
    name = 'gawker-feed'
    allowed_domains = ['gawker.com']
    start_urls = ['http://feeds.gawker.com/gawker/full']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        )

    def parse_item(self, response, *args, **kwargs):
        article = super(GoogleNewsSpider, self).parse_item(response, *args, **kwargs)
        soup = BeautifulSoup(article['description'])
        clean_description = "\n".join(clean_control_chars(string) for string in soup.stripped_strings)
        article['description'] = clean_description
        return article






## TODO create related scrapy.item.Gawker?



'''
Scrapy docs
http://doc.scrapy.org/en/0.14/intro/tutorial.html
Spiders are user-written classes used to scrape information from a domain (or group of domains).

'''