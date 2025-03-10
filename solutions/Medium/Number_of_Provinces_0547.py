
from collections import deque


class Solution(object):
    def findCircleNumDFS(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(node):
            visited.add(node)
            for neighbor in range(len(isConnected)):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        visited = set()
        provinces = 0

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces

    def findCircleNumBFS(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = set()
        provinces = 0

        for i in range(len(isConnected)):
            if i not in visited:
                queue = deque([i])
                while queue:
                    node = queue.popleft()
                    visited.add(node)
                    for neighbor in range(len(isConnected)):
                        if isConnected[node][neighbor] == 1 and neighbor not in visited:
                            queue.append(neighbor)
                provinces += 1

        return provinces


# Example test cases
solution = Solution()

# Test case 1
isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
assert solution.findCircleNumDFS(isConnected) == 2  # Expected: 2

# Test case 2
isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert solution.findCircleNumBFS(isConnected) == 3  # Expected: 3

# Test case 3
isConnected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
assert solution.findCircleNumDFS(isConnected) == 1  # Expected: 1

# Test case 4
isConnected = [[1]]
assert solution.findCircleNumBFS(isConnected) == 1  # Expected: 1

print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n^2), where N is the number of cities. The matrix has N^2 elements, and we visit each element once.
# Space complexity: O(n), where N is the number of cities. The visited set and the queue can contain at most N elements.
