#encoding;shift-jis

import sys
import unittest

from MyCsvReader import MyCsvReader

class TestMySuite(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOfTest(self):
        self.assertEqual(1, 1)

    def testNewClass(self):
        self.assertTrue(MyCsvReader())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMySuite)
    unittest.TextTestRunner(verbosity=2).run(suite)
