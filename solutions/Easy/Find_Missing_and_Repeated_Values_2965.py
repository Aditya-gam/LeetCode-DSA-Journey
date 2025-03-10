from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        Function: findMissingAndRepeatedValues
        Description: Finds the repeated number `a` and the missing number `b` in the given `n x n` grid.

        Parameters:
        - grid (List[List[int]]): A 2D matrix of size `n x n` containing numbers from `[1, n^2]` with one missing and one duplicate.

        Returns:
        - List[int]: A list `[a, b]` where `a` is the repeated number and `b` is the missing number.
        """

        n = len(grid)
        num_count = {}  # Dictionary to track occurrences of numbers

        # Flatten the grid and count occurrences
        for row in grid:
            for num in row:
                num_count[num] = num_count.get(num, 0) + 1

        repeated, missing = -1, -1

        # Scan through numbers from 1 to n^2 to find missing and repeated
        for i in range(1, n * n + 1):
            if i in num_count:
                if num_count[i] == 2:
                    repeated = i
            else:
                missing = i

        return [repeated, missing]


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic case with small grid
    grid = [[1, 3], [2, 2]]
    print("Test Case 1:", solution.findMissingAndRepeatedValues(grid))
    # Expected Output: [2, 4]

    # Test Case 2: Larger grid with missing in the middle
    grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
    print("Test Case 2:", solution.findMissingAndRepeatedValues(grid))
    # Expected Output: [9, 5]

    # Test Case 3: Missing number is the largest
    grid = [[1, 2, 3], [4, 5, 6], [7, 7, 8]]
    print("Test Case 3:", solution.findMissingAndRepeatedValues(grid))
    # Expected Output: [7, 9]

    # Test Case 4: Missing number is the smallest
    grid = [[2, 3, 4], [5, 6, 7], [8, 2, 9]]
    print("Test Case 4:", solution.findMissingAndRepeatedValues(grid))
    # Expected Output: [2, 1]

    # Test Case 5: Grid size is 4x4
    grid = [[1, 2, 3, 4], [5, 6, 6, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("Test Case 5:", solution.findMissingAndRepeatedValues(grid))
    # Expected Output: [6, 7]

    # Test Case 6: Edge case with n=50 (performance test)
    n = 50
    grid = [[(i * n + j + 1) for j in range(n)] for i in range(n)]
    grid[5][5] = 1  # Duplicate 1
    grid[49][49] = 2500  # Missing 2500
    print("Test Case 6:", solution.findMissingAndRepeatedValues(grid))
    # Expected Output: [1, 2500]

"""
Time Complexity:
- O(n^2) since we iterate through the entire grid twice.
- Total: O(n^2)

Space Complexity:
- O(n^2) for the dictionary storing occurrences.
- Total: O(n^2)
"""
