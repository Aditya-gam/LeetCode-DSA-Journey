from collections import deque


class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # Direction mappings: [right, left, down, up]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Deque for 0-1 BFS
        queue = deque([(0, 0, 0)])  # (row, col, cost)
        visited = [[False] * n for _ in range(m)]

        while queue:
            x, y, cost = queue.popleft()

            # If we reach the bottom-right corner, return the cost
            if x == m - 1 and y == n - 1:
                return cost

            # Skip if already visited
            if visited[x][y]:
                continue
            visited[x][y] = True

            # Explore neighbors
            for idx, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:  # Valid cell
                    # If the direction matches, cost remains the same
                    if idx + 1 == grid[x][y]:
                        queue.appendleft((nx, ny, cost))  # 0-cost move
                    else:
                        queue.append((nx, ny, cost + 1))  # 1-cost move

        # If no path exists (shouldn't happen per problem constraints)
        return -1


# Example test cases

# Test Case 1
grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
assert Solution().minCost(grid) == 3

# Test Case 2
grid = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
assert Solution().minCost(grid) == 0

# Test Case 3
grid = [[1, 2], [4, 3]]
assert Solution().minCost(grid) == 1

# Edge Case: Single Cell
grid = [[1]]
assert Solution().minCost(grid) == 0

# Large Grid with Uniform Directions
grid = [[1] * 100 for _ in range(100)]
assert Solution().minCost(grid) == 0

print("All passed")

# Complexity Analysis
# Time Complexity: O(M * N), Each cell is processed at most once, and we explore at most 4 neighbors per cell.

# Space Complexity: O(M * N), The space used by the queue and visited arrays.
