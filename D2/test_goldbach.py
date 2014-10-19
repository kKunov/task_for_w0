import unittest

from goldbach import is_prime, goldbach


class GoldbachTest(unittest.TestCase):

    def test_is_prime_if_n_less_than_zero_for_True(self):
        self.assertTrue(is_prime(-7))

    def test_is_prime_if_n_less_than_zero_for_False(self):
        self.assertFalse(is_prime(-8))

    def test_is_prime_if_n_bigger_than_zero_for_False(self):
        self.assertFalse(is_prime(10))

    def test_is_prime_if_n_bigger_than_zero_for_True(self):
        self.assertTrue(is_prime(17))

    def test_goldbach_for_goldbach_number(self):
        self.assertEqual([(3, 7), (5, 5)], goldbach(10))

    def test_goldbach_for_odd_number(self):
        self.assertEqual("Error: Odd number!", goldbach(7))


if __name__ == '__main__':
    unittest.main()
