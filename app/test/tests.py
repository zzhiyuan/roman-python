import unittest

from test_roman import RomanTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(RomanTest())
    return suite


if __name__ == '__main__':
    unittest.main()
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
