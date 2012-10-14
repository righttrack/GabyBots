# Set up the environment
from .. import settings
#from settings import PROJECT_ROOT  # According to the tutorial, this is required
#from django.core.management import setup_environ
#setup_environ(settings)

# Scrapy settings for scraping.news project
#
# All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scraping'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'scraping.news']
NEWSPIDER_MODULE = 'spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'dynamic_scraper.pipelines.ValidationPipeline',
    'scraping.news.pipelines.DjangoWriterPipeline',
]

