"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from gbots.scraping.processors import process


class SubstituteProcessorTest(TestCase):
    def test_parsing_empty_command(self):
        """
        Tests that forward slashes are properly recognized
        """
        self.assertEqual(process(r's///', 'same'), 'same')

    def test_parsing_simple_command(self):
        """
        Tests that a simple substitution can be made
        """
        self.assertEqual(process(r's/if/else/', 'if'), 'else')

    def test_parsing_inner_backslash(self):
        """
        Tests that a escaped forward slashes inside the command will be parsed correctly
        """
        self.assertEqual(process(r's/http:\/\/google.com/google/', 'http://google.com/home'),
            'google/home')

    def test_parsing_leading_backslash(self):
        """
        Tests that a leading escaped forward slash in the find portion of the command will be parsed correctly
        """
        self.assertEqual(process(r's/\/img//', '/img/cool.jpg'), '/cool.jpg')

    def test_parsing_leading_and_trailing_backslash(self):
        """
        Tests that leading and trailing escaped forward slashes can be parsed simultaneously in the find portion of the command
        """
        self.assertEqual(process(r's/\/img//', '/img/cool.jpg'), '/cool.jpg')

    def test_escaped_slash_replacement(self):
        """
        Tests that escaped forward slashes in the replace portion of the command will be parse correctly
        """
        self.assertEqual(process(r's/\/img/http:\/\/sample.com\/img/', '/img/cool.jpg'),
            'http://sample.com/img/cool.jpg')
