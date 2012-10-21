from scraping.models import Article
from scrapy.contrib_exp.djangoitem import DjangoItem

class ArticleItem(DjangoItem):
    django_model = Article
