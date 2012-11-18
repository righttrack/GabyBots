"""
Utility method tests
"""
from tempfile import mkdtemp
import unittest
from gbots.tests import skip, TestCase
from gbots.util.web import save_web_page_complete, convert_to_posix_args
from gbots.util.loggers import getLogger

logger = getLogger(__name__)

class PynixTest(unittest.TestCase):
    """
    @note: inheriting from a simple unittest.TestCase to avoid loading fixtures
    """

    def testConvertToPosixArgsSimpleArguments(self):
        """
        convert_to_posix_args uses proper '--' for verbose arguments
        """
        args = convert_to_posix_args(a=True)
        self.assertEqual('-a', args[0], "simple posix arguments must start with '-'")

    def testConvertToPosixArgsVerboseArguments(self):
        """
        convert_to_posix_args uses proper '--' for verbose arguments
        """
        args = convert_to_posix_args(aa=True)
        self.assertEqual('--aa', args[0], "verbose posix arguments must start with '--'")

    def testConvertToPosixArgsFiltersFalsyValues(self):
        """
        convert_to_posix_args filters out falsy values from kwargs.
        """
        args = convert_to_posix_args(a=True, b=1, c=0, d=False, e='', aa=True, bb=1, cc=0, dd=False, ee='')
        self.assertIn('-a', args)
        self.assertIn('-b', args)
        self.assertIn('--aa', args)
        self.assertIn('--bb', args)

    def testConvertToPosixArgsKeepsNonBooleanValues(self):
        """
        convert_to_posix_args keeps all non-bool values
        """
        args = convert_to_posix_args(a=True, b=1, c='c_v', aa=True, bb=1, cc='cc_v')
        self.assertItemsEqual(('-a', '-b', '1', '-c', 'c_v', '--aa', '--bb', '1', '--cc', 'cc_v'), args)


class WebTest(TestCase):
    def setUp(self):
        self.temp_dir = mkdtemp(prefix="%s-%s_" % ('-'.join(__name__.split('.')), self.__class__.__name__))

    @skip("this test takes too long to run every time")
    def testSaveWebPageComplete(self):
        path = "www.nytimes.com/2012/11/06/world/middleeast/Syria.html"
        save_web_page_complete(
            "http://" + path,
            self.temp_dir,
            quiet=True
        )
        logger.log("Web page saved to file://%s/%s" % (self.temp_dir, path))


