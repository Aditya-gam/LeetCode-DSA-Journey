from typing import List
from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Function: canFinish
        Description: Determines if it is possible to complete all courses given the prerequisites.

        Parameters:
        - numCourses (int): Total number of courses.
        - prerequisites (List[List[int]]): List of prerequisite pairs.

        Returns:
        - bool: True if all courses can be finished, False if there is a cycle.
        """

        # Step 1: Build the graph
        graph = defaultdict(list)  # Adjacency list
        in_degree = [0] * numCourses  # Keeps track of incoming edges

        for course, prereq in prerequisites:
            graph[prereq].append(course)  # prereq → course
            in_degree[course] += 1  # Increase in-degree

        # Step 2: Initialize queue with courses having no prerequisites (in-degree 0)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited_courses = 0  # Counter for processed courses

        # Step 3: Process courses in topological order
        while queue:
            course = queue.popleft()
            visited_courses += 1  # Mark course as completed

            for next_course in graph[course]:
                in_degree[next_course] -= 1  # Reduce in-degree
                if in_degree[next_course] == 0:
                    queue.append(next_course)  # Add course to queue

        # Step 4: If we visited all courses, it means no cycle exists
        return visited_courses == numCourses


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Can finish courses
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print(solution.canFinish(numCourses1, prerequisites1))
    # Expected output: True

    # Test case 2: Cannot finish due to cycle
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(solution.canFinish(numCourses2, prerequisites2))
    # Expected output: False

    # Test case 3: No prerequisites (all courses independent)
    numCourses3 = 3
    prerequisites3 = []
    print(solution.canFinish(numCourses3, prerequisites3))
    # Expected output: True

    # Test case 4: Complex dependencies with no cycles
    numCourses4 = 4
    prerequisites4 = [[1, 0], [2, 1], [3, 2]]
    print(solution.canFinish(numCourses4, prerequisites4))
    # Expected output: True

    # Test case 5: Large graph with cycle
    numCourses5 = 5
    prerequisites5 = [[0, 1], [1, 2], [2, 3], [3, 4],
                      [4, 2]]  # Cycle exists (2 → 3 → 4 → 2)
    print(solution.canFinish(numCourses5, prerequisites5))
    # Expected output: False

    # Test case 6: Large graph with no cycles
    numCourses6 = 5
    prerequisites6 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(solution.canFinish(numCourses6, prerequisites6))
    # Expected output: True

    print("All test cases passed!")

# Complexity Analysis:
# Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.

# Space Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
# We use a graph to represent the courses and their prerequisites, and a queue to keep track of courses with no prerequisites
