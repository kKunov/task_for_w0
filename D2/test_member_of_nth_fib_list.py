import unittest

from member_of_nth_fib_lists import member_of_nth_fib_lists


class Test_Member_of_nth_fib_list(unittest.TestCase):

    def test_needle_eq_listA(self):
        self.assertTrue(member_of_nth_fib_lists([1], [2], [1]))

    def test_needle_eq_listB(self):
        self.assertTrue(member_of_nth_fib_lists([1], [2], [2]))

    def test_needle_not_eq_to_lists_but_true(self):
        self.assertTrue(member_of_nth_fib_lists([1], [2], [1, 2]))

    def test_needle_not_eq_lists_and_false(self):
        self.assertFalse(member_of_nth_fib_lists([1], [2], [3, 4]))


if __name__ == '__main__':
    unittest.main()
