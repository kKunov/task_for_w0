import unittest

from is_an_bn import is_an_bn


class TestIsAnBn(unittest.TestCase):

    def test_is_an_bn_with_true_case(self):
        self.assertTrue(is_an_bn("aaaabbbb"))

    def test_is_an_bn_with_false_case_a_in_the_end(self):
        self.assertFalse(is_an_bn("aaaabbba"))

    def test_is_an_bn_with_false_case_a_not_in_the_end(self):
        self.assertFalse(is_an_bn("aaaabbab"))

    def test_is_an_bn_with_false_case_as_less_than_b(self):
        self.assertFalse(is_an_bn("aabbb"))

    def test_is_an_bn_with_false_case_bs_less_than_a(self):
        self.assertFalse(is_an_bn("aabbb"))

if __name__ == '__main__':
    unittest.main()
