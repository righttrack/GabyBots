from dynamic_scraper.models import ScrapedObjClass
from gbots.scraping.models import WebSource
from gbots.tests import TestCase

class GoogleNewsSourceSpiderTest(TestCase):
    # fixtures = ['initial_data.json']  # initial_data.json is assumed by Django's TestCase

    def testGoogleNewsHasArticleScraper(self):
        """
        The fixture contains the Google RSS Feed scraper whose scraped object class is an Article
        """
        source = WebSource.objects.get(alias="rss-google-world")
        article_obj_class = ScrapedObjClass.objects.get(name="Article")
        self.assertEqual(article_obj_class, source.scraper.scraped_obj_class)
