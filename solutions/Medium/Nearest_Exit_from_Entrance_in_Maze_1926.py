from collections import deque


class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        rows, cols = len(maze), len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            row, col, steps = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    if (nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1) and (nr, nc) != (entrance[0], entrance[1]):
                        return steps + 1  # Found the nearest exit
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))

        return -1  # No exit found


# Example test cases
solution = Solution()

# Test case 1
maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]
assert solution.nearestExit(maze, entrance) == 1  # Expected: 1

# Test case 2
maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
entrance = [1, 0]
assert solution.nearestExit(maze, entrance) == 2  # Expected: 2

# Test case 3
maze = [[".", "+"]]
entrance = [0, 0]
assert solution.nearestExit(maze, entrance) == -1  # Expected: -1

# Test case 4
maze = [[".", ".", "."], [".", "+", "."], [".", ".", "."]]
entrance = [1, 0]
assert solution.nearestExit(maze, entrance) == 1  # Expected: 1

print("All test cases passed successfully.")

# Complexity analysis
# Time Complexity: O(m×n). In the worst case, BFS explores all cells in the maze.

# Space Complexity: O(m×n) Space for the queue and the visited set.
