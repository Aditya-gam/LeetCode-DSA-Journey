import sys
import os
import unittest
from solutions.Easy.Check_if_Array_Is_Sorted_and_Rotated_1752 import Solution

# Add the root directory to the system path to allow module imports
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../..')))


class TestCheckIfSortedAndRotated(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 4, 5, 1, 2]
        self.assertTrue(self.solution.check(nums))

    def test_example_2(self):
        nums = [2, 1, 3, 4]
        self.assertFalse(self.solution.check(nums))

    def test_example_3(self):
        nums = [1, 2, 3]
        self.assertTrue(self.solution.check(nums))

    def test_edge_case_single_element(self):
        nums = [1]
        # A single element array is always sorted and rotated.
        self.assertTrue(self.solution.check(nums))

    def test_edge_case_all_same_elements(self):
        nums = [2, 2, 2, 2]
        # All elements being the same is valid.
        self.assertTrue(self.solution.check(nums))

    def test_edge_case_large_sorted(self):
        nums = list(range(1, 101))
        # A fully sorted array is valid.
        self.assertTrue(self.solution.check(nums))

    def test_edge_case_large_rotated(self):
        nums = list(range(51, 101)) + list(range(1, 51))
        # A large rotated array is valid.
        self.assertTrue(self.solution.check(nums))


if __name__ == '__main__':
    unittest.main()
