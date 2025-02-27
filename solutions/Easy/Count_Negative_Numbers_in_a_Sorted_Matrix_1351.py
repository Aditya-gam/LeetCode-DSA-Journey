class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        Counts the total number of negative numbers in grid, which is
        sorted in non-increasing order row-wise and column-wise.
        """
        m = len(grid)
        n = len(grid[0])

        count = 0
        row, col = 0, n - 1

        while row < m and col >= 0:
            if grid[row][col] < 0:
                # All cells below 'row' in this column 'col' are negative
                count += (m - row)
                col -= 1
            else:
                # If current is non-negative, move down to find smaller values
                row += 1

        return count


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    grid1 = [[4, 3, 2, -1],
             [3, 2, 1, -1],
             [1, 1, -1, -2],
             [-1, -1, -2, -3]]
    # Expected: 8
    assert solution.countNegatives(grid1) == 8

    # Example 2
    grid2 = [[3, 2], [1, 0]]
    # Expected: 0
    assert solution.countNegatives(grid2) == 0

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(m + n), where m is the number of rows and n is the number of columns in the grid.
# Space complexity: O(1) since we are using only a constant amount of space.
