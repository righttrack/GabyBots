"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from metrics.calc import target_name_count
from metrics.models import Target, Metric, TotalTargetCount
from metrics.services import ArticleMetricService
from scraping.models import Article


class TestTargetNameCount(TestCase):
    target_obama = Target(names=[
        "barack", "obama"
    ])
    known_values = [
        "President Obama", [("obama", 1)],
        "the campaign organizer Barack O. in 1992", [("barack", 1)],
        "obamabasedgod", [],
        "barack obama said ...", [("barack", 1), ("obama", 1)],
    ]
    # TODO: this test data makes me think we need a better way to represent and/or make reference to targets
    #
    # 1. What if the name of a target is often only made in context.
    #     example: "The President was adamant about ..."
    #     Does this mean the president of Libya? Barack Obama?
    #
    # 2. Are we satisfied with enumerating all the iterations of name combinations?
    #    example: target.names = ["barack", "obama", "president of the us", "u.s. president", ...]
    #    Couldn't we use some semantic knowledge from natural language processing to extract things like
    #    compound targets (president, united_states)
    #
    # TODO: WWKD (What would Kripke do?)

    def test_known_values(self):
        for sample, expected in self.known_values:
            self.assertEqual(target_name_count(self.target_obama, sample), expected)


# TODO: Separate service tests from calculation unit tests

class TestTotalTargetCount(TestCase):
    fixtures = ['total_target_count__targets', 'total_target_count__articles', 'total_target_count__metrics']
    # TODO: Make json files fosr the target data and expected values for the metrics

    def test_target_count_article(self):
        # TODO: create a metrics fixture that relates the data from targets
        # Given the article and target of every expected metric
        for expected in TotalTargetCount.objects.select_related('article', 'target'):
            # When metric has been calculated
            actual = ArticleMetricService.createTotalTargetCount(expected.article, expected.target)
            # It should match the expected metric
            self.assertEqual(actual, expected)

