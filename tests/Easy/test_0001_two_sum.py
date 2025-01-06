import sys
import os
import unittest
from solutions.Easy.Two_Sum_0001 import Solution

# Add the root directory to the system path to allow module imports
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../..')))


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 1])

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [1, 2])

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 1])

    def test_edge_case_min_elements(self):
        nums = [1, 2]
        target = 3
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 1])

    def test_edge_case_negative_numbers(self):
        nums = [-3, 4, 3, 90]
        target = 0
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 2])

    def test_edge_case_large_input(self):
        nums = list(range(1, 10**4 + 1))
        target = 19999
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [9997, 9998])


if __name__ == '__main__':
    unittest.main()
