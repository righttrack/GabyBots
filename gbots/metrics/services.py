from metrics.calc import target_name_count
from metrics.models import TotalTargetCount, TotalTargetNameCount

__author__ = 'jeffmay'


class ArticleMetricService(object):

    def createTotalTargetCount(self, article, target):
        # then you will create the model like so...
        target_name_counts = target_name_count(target, article.description)
        target_count_metric = TotalTargetCount(
            target=target,
            target_name_counts=[
            TotalTargetNameCount(target_name=name, score=count)
            for name, count in target_name_counts
            ]
        )
        # having a separate return line is helpful for debugging, but you could just return the result of the previous line
        return target_count_metric  # the caller can save this model to the database by calling .save() on this
