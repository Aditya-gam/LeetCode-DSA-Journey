class Solution:
    def coloredCells(self, n: int) -> int:
        """
        Function: coloredCells
        Description: Computes the total number of colored cells in the grid after `n` minutes.

        Parameters:
        - n (int): The number of minutes to apply the coloring process.

        Returns:
        - int: The total number of colored cells.
        """
        return n * n + (n - 1) * (n - 1)


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Minimal case (n=1)
    n = 1
    print("Test Case 1:", solution.coloredCells(n))
    # Expected Output: 1

    # Test Case 2: Small case (n=2)
    n = 2
    print("Test Case 2:", solution.coloredCells(n))
    # Expected Output: 5

    # Test Case 3: Medium case (n=3)
    n = 3
    print("Test Case 3:", solution.coloredCells(n))
    # Expected Output: 13

    # Test Case 4: Larger case (n=10)
    n = 10
    print("Test Case 4:", solution.coloredCells(n))
    # Expected Output: 181

    # Test Case 5: Large input (n=100)
    n = 100
    print("Test Case 5:", solution.coloredCells(n))
    # Expected Output: 19801

    # Test Case 6: Maximum input case (n=100000)
    n = 100000
    print("Test Case 6:", solution.coloredCells(n))
    # Expected Output: 19999800001

"""
Time Complexity:
- O(1), since we use a direct mathematical formula to compute the result.

Space Complexity:
- O(1), as we use only a single integer variable.
"""
