from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Function: permute
        Description: Generates all possible permutations of a given list of distinct integers.

        Parameters:
        - nums (List[int]): List of distinct integers.

        Returns:
        - List[List[int]]: A list of all possible permutations.
        """

        res = []

        def backtrack(path, available):
            # Base case: If the path contains all elements, store the permutation
            if not available:
                res.append(path[:])  # Make a copy before adding
                return

            # Iterate through remaining elements
            for i in range(len(available)):
                backtrack(path + [available[i]], available[:i] +
                          available[i+1:])  # Choose and explore

        backtrack([], nums)

        return res


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard case with three elements
    print("Test Case 1: nums = [1,2,3]")
    print("Expected Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] | Actual Output:", solution.permute(
        [1, 2, 3]))

    # Test case 2: Two elements (simplest multi-permutation case)
    print("Test Case 2: nums = [0,1]")
    print("Expected Output: [[0,1],[1,0]] | Actual Output:",
          solution.permute([0, 1]))

    # Test case 3: Single element
    print("Test Case 3: nums = [1]")
    print("Expected Output: [[1]] | Actual Output:", solution.permute([1]))

    # Test case 4: Largest input size (6 elements)
    print("Test Case 4: nums = [1,2,3,4,5,6]")
    print("Expected Output: Computed Output:",
          solution.permute([1, 2, 3, 4, 5, 6]))

    # Test case 5: Permutations of negative numbers
    print("Test Case 5: nums = [-1, -2, -3]")
    print("Expected Output: Computed Output:", solution.permute([-1, -2, -3]))

    # Test case 6: Mixed positive and negative numbers
    print("Test Case 6: nums = [-1, 0, 1]")
    print("Expected Output: Computed Output:", solution.permute([-1, 0, 1]))

"""
Time Complexity:
- O(N!) → There are N! permutations to generate.
- Space Complexity:
  - O(N) → Recursion depth is at most N.
"""
