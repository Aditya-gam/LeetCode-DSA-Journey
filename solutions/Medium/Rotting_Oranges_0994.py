from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0

        # Step 1: Initialize the queue with all rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Step 2: Perform BFS
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_time = 0

        while queue:
            r, c, time = queue.popleft()
            max_time = max(max_time, time)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Mark the orange as rotten
                    fresh_oranges -= 1
                    queue.append((nr, nc, time + 1))

        # Step 3: Check for remaining fresh oranges
        return max_time if fresh_oranges == 0 else -1


# Example test cases
solution = Solution()

# Test case 1
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
assert solution.orangesRotting(grid) == 4  # Expected: 4

# Test case 2
grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
assert solution.orangesRotting(grid) == -1  # Expected: -1

# Test case 3
grid = [[0, 2]]
assert solution.orangesRotting(grid) == 0  # Expected: 0

# Test case 4
grid = [[1]]
assert solution.orangesRotting(grid) == -1  # Expected: -1

# Test case 5
grid = [[0, 0], [0, 0]]
assert solution.orangesRotting(grid) == 0  # Expected: 0

print("All test cases pass")

# Complexity Analysis
# Time Complexity: O(m×n), Each cell is processed at most once during BFS.
# Space Complexity: O(m×n), The queue can hold all the grid cells in the worst case.
