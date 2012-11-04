from django.db import models

# Targets

class TargetName(models.Model):
    class Meta:
        db_table = "target_names"
    value = models.CharField(max_length=200)

class Target(models.Model):
#    names = ListField(str, "names")
    names = models.ForeignKey('metrics.TargetName')


# Metrics

class Metric(models.Model):
    class Meta:
        abstract = True
    score = models.FloatField()

class ArticleMetric(Metric):
    class Meta:
        abstract = True
    article = models.ForeignKey('scraping.Article')

class TotalTargetNameCount(Metric):
    target_name = models.ForeignKey('metrics.TargetName')

class TotalTargetCount(ArticleMetric):
    target = models.ForeignKey('metrics.Target')
    target_name_counts = models.ForeignKey('metrics.TotalTargetNameCount')
