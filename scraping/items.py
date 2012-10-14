from scraping.models import WebContent
from scrapy.contrib_exp.djangoitem import DjangoItem

class WebContentItem(DjangoItem):
    django_model = WebContent
