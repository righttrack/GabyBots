from scraping.news.spiders import ArticleSpider

__author__ = 'jeffmay'

class GoogleNewsSpider(ArticleSpider):
    """A sample spider for specific source processing."""
    name = 'google-news'
    allowed_domains = ['news.google.com']

    def parse_item(self, response, *args, **kwargs):
        article = super(GoogleNewsSpider, self).parse_item(response, *args, **kwargs)
        # Do some stuff with article...
        #
        # For processing the document in question, you can use urllib with article["url"]
        # You should also look at using beautifulsoup for processing the html
        #
        # If you want to optionally perform other steps on the result, you should look
        # at creating a pipeline.
        return article
