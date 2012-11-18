"""
Tests for the scraping app.
"""

from gbots.tests import TestCase
from gbots.scraping.processors import process


class ProcessorTest(TestCase):
    """
    Tests process function.
    """

    def test_parsing_empty_command(self):
        """
        Forward slashes should be properly recognized.
        """
        self.assertEqual(process(r's///', 'same'), 'same')

    def test_parsing_simple_command(self):
        """
        A simple substitution can be made.
        """
        self.assertEqual(process(r's/if/else/', 'if'), 'else')

    def test_parsing_inner_backslash(self):
        """
        An escaped forward slashes inside the substitute command is parsed correctly.
        """
        self.assertEqual(process(r's/http:\/\/google.com/google/', 'http://google.com/home'),
            'google/home')

    def test_parsing_leading_backslash(self):
        """
        A leading escaped forward slash in the find portion of the substitute command is parsed correctly.
        """
        self.assertEqual(process(r's/\/img//', '/img/cool.jpg'), '/cool.jpg')

    def test_parsing_leading_and_trailing_backslash(self):
        """
        Leading and trailing escaped forward slashes in the find portion of the substitute command are parsed correctly.
        """
        self.assertEqual(process(r's/\/img//', '/img/cool.jpg'), '/cool.jpg')

    def test_escaped_slash_replacement(self):
        """
        Escaped forward slashes in the replace portion of the command are parsed correctly.
        """
        self.assertEqual(process(r's/\/img/http:\/\/sample.com\/img/', '/img/cool.jpg'),
            'http://sample.com/img/cool.jpg')
