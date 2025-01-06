import sys
import os
import unittest
from solutions.Easy.Minimum_Average_of_Smallest_and_Largest_Elements_3194 import Solution

# Add the root directory to the system path to allow module imports
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../..')))


class TestMinimumAverage(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [7, 8, 3, 4, 15, 13, 4, 1]
        result = self.solution.minimumAverage(nums)
        self.assertEqual(result, 5.5)

    def test_example_2(self):
        nums = [1, 9, 8, 3, 10, 5]
        result = self.solution.minimumAverage(nums)
        self.assertEqual(result, 5.5)

    def test_example_3(self):
        nums = [1, 2, 3, 7, 8, 9]
        result = self.solution.minimumAverage(nums)
        self.assertEqual(result, 5.0)

    def test_edge_case_min_elements(self):
        nums = [1, 2]
        result = self.solution.minimumAverage(nums)
        self.assertEqual(result, 1.5)

    def test_edge_case_all_same_elements(self):
        nums = [5, 5, 5, 5]
        result = self.solution.minimumAverage(nums)
        self.assertEqual(result, 5.0)

    def test_edge_case_unsorted_input(self):
        nums = [50, 1, 25, 26, 2, 49]
        result = self.solution.minimumAverage(nums)
        self.assertEqual(result, 25.5)

    def test_edge_case_large_elements(self):
        nums = [50, 50, 50, 50]
        result = self.solution.minimumAverage(nums)
        self.assertEqual(result, 50.0)


if __name__ == '__main__':
    unittest.main()
