import unittest

from magic_square import magic_square, colums, rows, f_diagonal, b_diagonal


class TestMagicSquare(unittest.TestCase):

    def test_rows_for_true(self):
        self.assertEqual(15, rows([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))

    def test_rows_for_false(self):
        self.assertFalse(rows([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_colums_for_true(self):
        self.assertEqual(6, colums([[1, 2, 3], [3, 2, 1], [2, 2, 2]]))

    def test_colums_for_false(self):
        self.assertFalse(colums([[1, 2, 3], [3, 2, 1], [2, 1, 2]]))

    def test_f_diagonal(self):
        self.assertEqual(6, f_diagonal([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))

    def test_b_diagonal(self):
        self.assertEqual(6, b_diagonal([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))

    def test_magic_square_for_true(self):
        self.assertTrue(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))

    def test_magic_square_for_false(self):
        self.assertFalse(magic_square([[4, 1, 2], [3, 5, 7], [8, 1, 6]]))


if __name__ == '__main__':
    unittest.main()
