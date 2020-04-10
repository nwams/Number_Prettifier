import unittest
import number_prettifier

class TestNumberPrettifier(unittest.TestCase):
    """
    The class inherits from unittest
    """
    def test_pretty_format(self):
        self.assertEqual(number_prettifier.pretty_format(1000000), '1M')
        self.assertEqual(number_prettifier.pretty_format(2500000.34), '2.5M')
        self.assertEqual(number_prettifier.pretty_format(532), '532')
        self.assertEqual(number_prettifier.pretty_format(1123456789), '1.1B')
        self.assertEqual(number_prettifier.pretty_format(9487634567534), '9.5T')
        self.assertEqual(number_prettifier.pretty_format(1100), '1.1K')
        self.assertEqual(number_prettifier.pretty_format(-199999999999), '-200B') # test a negative num
        self.assertEqual(number_prettifier.pretty_format(9.9), '9.9')
        # test the min and max trillions
        self.assertEqual(number_prettifier.pretty_format(999000000000000), '999T')
        self.assertEqual(number_prettifier.pretty_format(-999000000000000), '-999T')


if __name__ == '__main__':
    unittest.main()