import unittest

from main import Solution

cases = [(3, "III"), (4, "IV"), (58, "LVIII"), (1994, "MCMXCIV"), (3000, "MMM"), (9, "IX")]


class TestSolution(unittest.TestCase):

    def test_int_to_roman(self):
        solution = Solution()
        for case in cases:
            with self.subTest():
                self.assertEqual(solution.int_to_roman(case[0]), case[1])
