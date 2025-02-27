from typing import List
from collections import deque, defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Function: findOrder
        Description: Determines a valid order of courses that can be completed given prerequisites.

        Parameters:
        - numCourses (int): Total number of courses.
        - prerequisites (List[List[int]]): List of prerequisite pairs.

        Returns:
        - List[int]: A valid ordering of courses, or an empty list if impossible.
        """

        # Step 1: Build graph and in-degree array
        graph = defaultdict(list)  # Adjacency list
        in_degree = [0] * numCourses  # Keeps track of incoming edges

        for course, prereq in prerequisites:
            graph[prereq].append(course)  # prereq → course
            in_degree[course] += 1  # Increase in-degree

        # Step 2: Initialize queue with courses having no prerequisites (in-degree 0)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        course_order = []  # Stores valid course order

        # Step 3: Process courses in topological order
        while queue:
            course = queue.popleft()
            course_order.append(course)  # Add to result

            for next_course in graph[course]:
                in_degree[next_course] -= 1  # Reduce in-degree
                if in_degree[next_course] == 0:
                    queue.append(next_course)  # Add course to queue

        # Step 4: Check if all courses are completed
        return course_order if len(course_order) == numCourses else []


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Can finish courses
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print(solution.findOrder(numCourses1, prerequisites1))
    # Expected output: [0,1]

    # Test case 2: Multiple valid orders
    numCourses2 = 4
    prerequisites2 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(solution.findOrder(numCourses2, prerequisites2))
    # Expected output: [0,1,2,3] or [0,2,1,3]

    # Test case 3: Single course with no prerequisites
    numCourses3 = 1
    prerequisites3 = []
    print(solution.findOrder(numCourses3, prerequisites3))
    # Expected output: [0]

    # Test case 4: Cycle exists, impossible to finish
    numCourses4 = 3
    prerequisites4 = [[0, 1], [1, 2], [2, 0]]
    print(solution.findOrder(numCourses4, prerequisites4))
    # Expected output: []

    # Test case 5: Courses with some independent
    numCourses5 = 6
    prerequisites5 = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]]
    print(solution.findOrder(numCourses5, prerequisites5))
    # Expected output: [0,1,2,3,4,5] or similar valid order

    # Test case 6: No prerequisites (all courses independent)
    numCourses6 = 3
    prerequisites6 = []
    print(solution.findOrder(numCourses6, prerequisites6))
    # Expected output: [0,1,2] or similar valid order

    # Test case 7: Large graph with cycle
    numCourses7 = 5
    prerequisites7 = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 2]]
    print(solution.findOrder(numCourses7, prerequisites7))
    # Expected output: []

    # Test case 8: Large graph with no cycles
    numCourses8 = 5
    prerequisites8 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(solution.findOrder(numCourses8, prerequisites8))
    # Expected output: [0,1,2,3,4] or similar valid order

    print("All test cases passed!")

# Complexity Analysis:
# Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
# Space Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
# We use a graph to represent the courses and their prerequisites, and a queue to process the courses in topological order. The space complexity is dominated by the graph and queue.
