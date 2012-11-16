# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# Utility spiders
from bs4 import BeautifulSoup
from dynamic_scraper.spiders.django_spider import DjangoSpider
from gbots.scraping.models import Article, WebSource, BaseItemModel
from gbots.scraping.news.items import ArticleItem, BaseItem
from gbots.util.strings import clean_control_chars

# TODO: Convert this to a base item spider

# 1. check if the spider is done scraping
# 2. if not, find the appropriate web source

class SourceSpider(DjangoSpider):
    name = 'source'

    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        self._set_ref_object(WebSource, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scraped_obj_class = BaseItemModel
        self.scraped_obj_item_class = BaseItem
        self.scheduler_runtime = self.ref_object.scraper_runtime
        super(SourceSpider, self).__init__(self, *args, **kwargs)

    def _set_ref_object(self, ref_object_class, **kwargs):
        # TODO: allow searching by alias
        super(SourceSpider, self)._set_ref_object(ref_object_class, **kwargs)
        # for clarity
        self.source = self.ref_object

    def parse_item(self, *args, **kwargs):
        item = super(SourceSpider, self).parse_item(*args, **kwargs)
        url_elem = self.scraper.get_detail_page_url_elem()
        url_name = url_elem.scraped_obj_attr.name
        # apply post processing to clean up the url
        processed_url = self.source.process_url(item[url_name])
        item[url_name] = processed_url
        # check if the item is done being scraped
        if self.is_done_scraping(item):
            return item
        else:
            # open a new scraper for the processed url
            self.log("openning scraper for %s" % processed_url)
            self.open_scraper_for(item, processed_url)
            return item

    def open_scraper_for(self, item, url):
        source = WebSource.objects.matching(url)
        # I. Reinitialize scraper
        self.kwargs["id"] = source.id
        self.__init__(**self.kwargs)
        # TODO: Get web source that matches scraped url
        # TODO: Either create new spider, or reinitialize this one
        # Test to see which is better
        # Open matching django spider here instead of reusing the same spider?

    #        return Request(url, self.process_item, meta={'item': item})

    def is_done_scraping(self, item):
        # Always retrieve a source for this item
        return False


class RssFeedSpider(SourceSpider):
    name = 'rss'

    def is_done_scraping(self, item):
        # Stop once we have a base item from this RSS feed
        return True


class ArticleSpider(SourceSpider):
    name = 'article'

    def __init__(self, *args, **kwargs):
        self.scraped_obj_item_class = ArticleItem
        self.scraped_obj_class = Article
        super(ArticleSpider, self).__init__(self, *args, **kwargs)

    def is_done_scraping(self, item):
        return "contents" in item

    def parse_item(self, *args, **kwargs):
        article = super(ArticleSpider, self).parse_item(*args, **kwargs)
        article["description"] = self.clean_description(article)
        return article

    def clean_description(self, article):
        soup = BeautifulSoup(article['description'])
        return "\n".join(clean_control_chars(string) for string in soup.stripped_strings)
