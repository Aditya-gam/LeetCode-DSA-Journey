class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            # Base case: If out of bounds, already visited, or land, stop recursion
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c] or grid[r][c] == 0:
                return 0

            # Mark the cell as visited and collect fish
            visited[r][c] = True
            fish_count = grid[r][c]

            # Explore all four directions
            for dr, dc in directions:
                fish_count += dfs(r + dr, c + dc)

            return fish_count

        max_fish = 0

        # Iterate through the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    # Start DFS for each unvisited water cell
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish


#  Example test cases
# Test case 1
grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
assert Solution().findMaxFish(grid) == 7

# Test case 2
grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
assert Solution().findMaxFish(grid) == 1

# Test case 3
grid = [[0, 0], [0, 0]]
assert Solution().findMaxFish(grid) == 0

# Test case 4
grid = [[5]]
assert Solution().findMaxFish(grid) == 5

# Test case 5
grid = [[1, 2], [3, 4]]
assert Solution().findMaxFish(grid) == 10

print("All test cases pass")

# Complexity analysis
# Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid.
# Space Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid.
