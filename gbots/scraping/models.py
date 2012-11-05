from django.db import models
from django.db.models import Manager
from dynamic_scraper.models import Scraper, SchedulerRuntime
from gbots.util import loggers
import re


logger = loggers.getLogger(__name__)

class WeakForeignKey(models.ForeignKey):
    """
    Loosly couple this to a foreign table to prevent cascading deletes, invalid ids, and to permit missing ids.
    """
    def __init__(self, *args, **kwargs):
        kwargs.update(blank=True, null=True, on_delete=models.SET_NULL)
        super(WeakForeignKey, self).__init__(*args, **kwargs)

# Allow South to introspect these fields
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^gbots\.scraping\.models\.WeakForeignKey"])

# Sample code to dynamically delete active scrapers when the scraper is deleted from the admin interface
#@receiver(pre_delete)
#def pre_delete_handler(sender, instance, using, **kwargs):
#    ....
#
#    if isinstance(instance, Article):
#        if instance.checker_runtime:
#            instance.checker_runtime.delete()
#
#pre_delete.connect(pre_delete_handler)


##### Sources ####

class SourceModel(models.Model):
    class Meta:
        abstract = True
    scraper = WeakForeignKey(Scraper)
    scraper_runtime = WeakForeignKey(SchedulerRuntime)
    alias = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

# Custom:

class WebSourceManager(Manager):
    def matching(self, url):
        logger.log("finding matching sources...")
        valid_sources = [source for source in self.exclude(pattern=u'')]
        matches = []
        for source in valid_sources:
            logger.log("matching url %s with /%s/ for source '%s'..." % (url, source.pattern, source.alias))
            if re.match(source.pattern, url):
                logger.log("success")
                matches.append(source)
            else:
                logger.log("failed")
        num = len(matches)
        logger.log("found %d sources" % len(matches))
        if num == 1:
            return matches[0]
        if not num:
            raise self.model.DoesNotExist(
                "%s matching url (%s) does not exist."
                % (self.model._meta.object_name, url))
        raise self.model.MultipleObjectsReturned(
            "url (%s) matched more than one %s -- it matched %s!"
            % (url, self.model._meta.object_name, num))

class WebSource(SourceModel):
    objects = WebSourceManager()
    url = models.URLField()
    pattern = models.CharField(blank=True, max_length=200)

    def __unicode__(self):
        return self.description


##### Items ####

class ScrapedItemModel(models.Model):
    class Meta:
        abstract = True
    checker_runtime = WeakForeignKey(SchedulerRuntime)
    source = models.ForeignKey(WebSource)

# Common list models

class Anchor(models.Model):
    href = models.URLField()
    text = models.CharField(max_length=1000)

class Image(models.Model):
    src = models.URLField()
    alt = models.CharField(max_length=1000)
    link = models.ForeignKey(Anchor)

class Section(models.Model):
    text = models.TextField()

# Custom Items:

class BaseItemModel(ScrapedItemModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField()

class Article(BaseItemModel):
    content = models.TextField()
    sections = models.ForeignKey(Section)
    images = models.ForeignKey(Image)
    links = models.ForeignKey(Anchor)

    def __unicode__(self):
        return self.title


