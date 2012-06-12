#encoding;shift-jis

import sys
import unittest

from CsvReader import CsvReader


class TestMySuite(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNewClass(self):
        csr = CsvReader('AutoCtrl_Area01_01.csv')
        csr.print()
        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMySuite)
    unittest.TextTestRunner(verbosity=2).run(suite)
