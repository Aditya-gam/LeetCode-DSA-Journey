from collections import defaultdict, deque


class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, True))  # True indicates directed edge a -> b
            # False indicates reverse direction b -> a
            graph[b].append((a, False))

        queue = deque([0])
        visited = set()
        changes = 0

        while queue:
            city = queue.popleft()
            visited.add(city)
            for neighbor, directed in graph[city]:
                if neighbor not in visited:
                    if directed:
                        changes += 1  # Count the edge that needs reorientation
                    queue.append(neighbor)

        return changes


# Example test cases
solution = Solution()

# Test case 1
n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
solution = Solution()
assert solution.minReorder(n, connections) == 3  # Expected: 3

# Test case 2
n = 5
connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
assert solution.minReorder(n, connections) == 2  # Expected: 2

# Test case 3
n = 3
connections = [[1, 0], [2, 0]]
assert solution.minReorder(n, connections) == 0  # Expected: 0

print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n), where n is the number of cities. We are visiting each city once.
# Space complexity: O(n), where n is the number of cities. We are using a dictionary to store the graph and a set to store visited cities.
