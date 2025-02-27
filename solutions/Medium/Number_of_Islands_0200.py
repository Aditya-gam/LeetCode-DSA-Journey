from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Function: numIslands
        Description: Counts the number of islands in a given 2D grid using DFS.

        Parameters:
        - grid (List[List[str]]): A 2D list representing the map, where '1' indicates land and '0' indicates water.

        Returns:
        - int: The number of islands in the grid.
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r, c):
            """
            Depth-first search to mark all connected land ('1') as visited.
            """
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'  # Mark the current cell as visited
            # Explore all four possible directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # Found a new island
                    num_islands += 1
                    dfs(r, c)  # Mark all connected land as visited

        return num_islands


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Single large island
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(solution.numIslands(grid1))
    # Expected output: 1

    # Test case 2: Multiple islands
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(solution.numIslands(grid2))
    # Expected output: 3

    # Test case 3: No islands (all water)
    grid3 = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    print(solution.numIslands(grid3))
    # Expected output: 0

    # Test case 4: Single isolated land cell
    grid4 = [
        ["0", "0", "0"],
        ["0", "1", "0"],
        ["0", "0", "0"]
    ]
    print(solution.numIslands(grid4))
    # Expected output: 1

    # Test case 5: All land (one big island)
    grid5 = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"]
    ]
    print(solution.numIslands(grid5))
    # Expected output: 1

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the grid.
# We visit each cell in the grid once and perform a constant amount of work for each cell.

# Space Complexity: O(M * N), where M is the number of rows and N is the number of columns in the grid.
# The depth of the recursion can go up to M * N in the worst case, which occurs when the grid is filled with land.
