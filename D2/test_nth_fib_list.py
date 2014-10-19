import unittest

from nth_fib_lists import nth_fib_lists


class Test_nth_fib_list(unittest.TestCase):

    def test_n_eq_1(self):
        self.assertTrue(nth_fib_lists([1], [2], 1))

    def test_n_eq_2(self):
        self.assertTrue(nth_fib_lists([1], [2], 2))

    def test_n_bigger_than_2(self):
        self.assertTrue(nth_fib_lists([1], [2], 3))


if __name__ == '__main__':
    unittest.main()
