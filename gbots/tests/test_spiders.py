from dynamic_scraper.models import ScrapedObjClass
from gbots.scraping.models import WebSource
from gbots.tests import TestCase

class FileSystemScrapingSpider(TestCase):
    pass

class GoogleNewsSourceSpiderTest(TestCase):
    fixtures = ['starter.json']  # TODO: make a testing fixture when this becomes too big

    def testGoogleNewsHasArticleScraper(self):
        """
        The fixture contains the Google RSS Feed scraper whose scraped object class is an Article
        """
        source = WebSource.objects.get(alias="rss-google-world")
        article_obj_class = ScrapedObjClass.objects.get(name="Article")
        self.assertEqual(article_obj_class, source.scraper.scraped_obj_class)

