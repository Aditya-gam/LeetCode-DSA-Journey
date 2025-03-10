class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])

        # Map numbers to their positions in the matrix
        num_to_position = {}
        for i in range(m):
            for j in range(n):
                num_to_position[mat[i][j]] = (i, j)

        # Row and column counters
        row_counts = [0] * m
        col_counts = [0] * n

        # Process arr and update row/col counts
        for i, num in enumerate(arr):
            row, col = num_to_position[num]

            # Increment counts
            row_counts[row] += 1
            col_counts[col] += 1

            # Check if the row or column is fully painted
            if row_counts[row] == n or col_counts[col] == m:
                return i

        return -1  # Should never reach here based on problem constraints


# Example test cases
solution = Solution()

# Example 1
arr = [1, 3, 4, 2]
mat = [[1, 4], [2, 3]]
assert Solution().firstCompleteIndex(arr, mat) == 2

# Example 2
arr = [2, 8, 7, 4, 1, 3, 5, 6, 9]
mat = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
assert Solution().firstCompleteIndex(arr, mat) == 3

# Edge Case: Single Cell
arr = [1]
mat = [[1]]
assert Solution().firstCompleteIndex(arr, mat) == 0

# Larger Grid
arr = [3, 2, 1, 6, 5, 4]
mat = [[3, 2], [1, 6], [5, 4]]
assert Solution().firstCompleteIndex(arr, mat) == 5

print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the matrix.
# Preprocessing: O(m*n), to create the number-to-position mapping.
# Simulation: O(m*n), as we iterate through arr.

# Space Complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix.
# Map: O(m*n), to store the number-to-position mapping.
# Counts: O(m+n), to store the row and column counts.
