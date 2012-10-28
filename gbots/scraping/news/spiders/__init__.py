# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# Utility spiders
from bs4 import BeautifulSoup
from dynamic_scraper.spiders.django_spider import DjangoSpider
from scraping.models import Article, WebSource
from scraping.news.items import ArticleItem
from util.strings import clean_control_chars

class ArticleSpider(DjangoSpider):
    name = 'article'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(WebSource, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Article
        self.scraped_obj_item_class = ArticleItem
        super(ArticleSpider, self).__init__(self, *args, **kwargs)

    def parse_item(self, response, *args, **kwargs):
        article = super(ArticleSpider, self).parse_item(response, *args, **kwargs)
        soup = BeautifulSoup(article['description'])
        clean_description = "\n".join(clean_control_chars(string) for string in soup.stripped_strings)
        article['description'] = clean_description
        return article


