from collections import deque


class Solution(object):
    def canVisitAllRoomsBFS(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        queue = deque([0])  # Start from room 0
        visited.add(0)

        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        return len(visited) == len(rooms)

    def canVisitAllRoomsDFS(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                dfs(key)

        visited = set()
        dfs(0)

        return len(visited) == len(rooms)


# Example test cases
solution = Solution()

# Test case 1
rooms = [[1], [2], [3], []]
assert solution.canVisitAllRoomsBFS(rooms) == True  # Expected: True

# Test case 2
rooms = [[1, 3], [3, 0, 1], [2], [0]]
assert solution.canVisitAllRoomsDFS(rooms) == False  # Expected: False

# Test case 3
rooms = [[1], [], [0, 3], [1]]
assert solution.canVisitAllRoomsBFS(rooms) == False  # Expected: False

# Test case 4
rooms = [[1, 2, 3], [0], [0], [0]]
assert solution.canVisitAllRoomsDFS(rooms) == True  # Expected: True

# Complexity analysis
# Time Complexity: O(N+E), where N is the number of rooms and E is the total number of keys across all rooms. Each room and key are visited once.

# Space Complexity: O(N), for the visited set and recursion stack (in DFS) or queue (in BFS).
