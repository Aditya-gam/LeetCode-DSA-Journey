class Solution(object):
    def uniquePaths(self, m, n):
        """
        Returns the number of unique paths in an m x n grid
        where the robot can move only down or right, starting
        from the top-left corner to the bottom-right corner.

        Parameters:
        m (int): Number of rows in the grid.
        n (int): Number of columns in the grid.

        Returns:
        int: Number of unique paths from (0, 0) to (m-1, n-1).
        """

        # Create a 2D dp array with dimensions m x n
        dp = [[0] * n for _ in range(m)]

        # Set the starting position
        dp[0][0] = 1

        # Fill the first row - only one way to move right
        for j in range(1, n):
            dp[0][j] = 1

        # Fill the first column - only one way to move down
        for i in range(1, m):
            dp[i][0] = 1

        # Fill the rest of the dp table
        for i in range(1, m):
            for j in range(1, n):
                # Number of ways to get to (i, j) is
                # the sum of ways to get to (i-1, j) and (i, j-1)
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The bottom-right corner has the total number of unique paths
        return dp[m - 1][n - 1]

# Example test cases


def test_uniquePaths():
    solution = Solution()

    # Test case 1: Small grid (1x1)
    # There's only one cell, so only 1 possible path (already there).
    assert solution.uniquePaths(1, 1) == 1

    # Test case 2: Single row (1x5)
    # The robot can only move right, so there's exactly 1 path.
    assert solution.uniquePaths(1, 5) == 1

    # Test case 3: Single column (5x1)
    # The robot can only move down, so there's exactly 1 path.
    assert solution.uniquePaths(5, 1) == 1

    # Test case 4: Example provided - m=3, n=7
    # Expected: 28
    assert solution.uniquePaths(3, 7) == 28

    # Test case 5: Example provided - m=3, n=2
    # The paths are: (Right->Down->Down), (Down->Down->Right), (Down->Right->Down)
    # Expected: 3
    assert solution.uniquePaths(3, 2) == 3

    # Test case 6: Some random checks
    # m=2, n=3 (2 rows, 3 columns)
    # Possible paths: Right->Right->Down, Right->Down->Right, Down->Right->Right -> 3
    assert solution.uniquePaths(2, 3) == 3

    # Larger test
    # m=5, n=5
    # Known result: 70 (choose(5+5-2, 5-1) = choose(8,4) = 70)
    assert solution.uniquePaths(5, 5) == 70

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(m*n) - We fill in the entire m x n grid once.
# Space complexity: O(m*n) - We use a 2D dp array of size m x n to store the number of unique paths for each cell.
