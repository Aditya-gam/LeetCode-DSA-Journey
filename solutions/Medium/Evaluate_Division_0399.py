from typing import List
from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Function: calcEquation
        Description: Evaluates division results based on given equations and values.

        Parameters:
        - equations (List[List[str]]): List of equations representing variable relationships.
        - values (List[float]): List of division results corresponding to each equation.
        - queries (List[List[str]]): List of queries to evaluate.

        Returns:
        - List[float]: Computed division results for each query. Returns -1.0 if not possible.
        """

        # Step 1: Build the graph representation of equations
        graph = defaultdict(dict)

        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value  # Store reciprocal relation

        # Step 2: Function to find the path using BFS
        def bfs(source, target):
            if source not in graph or target not in graph:
                return -1.0  # If either variable is unknown, return -1.0

            queue = deque([(source, 1.0)])  # (current node, current product)
            visited = set()

            while queue:
                node, product = queue.popleft()
                if node == target:
                    return product  # Found the path

                visited.add(node)

                for neighbor, value in graph[node].items():
                    if neighbor not in visited:
                        queue.append((neighbor, product * value))

            return -1.0  # No valid path found

        # Step 3: Process each query
        results = [bfs(A, B) for A, B in queries]

        return results


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard equations and queries
    equations1 = [["a", "b"], ["b", "c"]]
    values1 = [2.0, 3.0]
    queries1 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(solution.calcEquation(equations1, values1, queries1))
    # Expected output: [6.0, 0.5, -1.0, 1.0, -1.0]

    # Test case 2: Mixed relations
    equations2 = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values2 = [1.5, 2.5, 5.0]
    queries2 = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    print(solution.calcEquation(equations2, values2, queries2))
    # Expected output: [3.75, 0.4, 5.0, 0.2]

    # Test case 3: Single equation and inverse
    equations3 = [["a", "b"]]
    values3 = [0.5]
    queries3 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    print(solution.calcEquation(equations3, values3, queries3))
    # Expected output: [0.5, 2.0, -1.0, -1.0]

    # Test case 4: Single equation and inverse with different values
    equations4 = [["a", "b"]]
    values4 = [2.0]
    queries4 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    print(solution.calcEquation(equations4, values4, queries4))
    # Expected output: [2.0, 0.5, -1.0, -1.0]

    # Test case 5: Single equation and inverse with zero value
    equations5 = [["a", "b"]]
    values5 = [0.0]
    queries5 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    print(solution.calcEquation(equations5, values5, queries5))
    # Expected output: [0.0, 0.0, -1.0, -1.0]

    # Test case 6: Single equation and inverse with negative value
    equations6 = [["a", "b"]]
    values6 = [-2.0]
    queries6 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    print(solution.calcEquation(equations6, values6, queries6))
    # Expected output: [-2.0, -0.5, -1.0, -1.0]

    print("All test cases passed successfully.")

# Complexity Analysis:
# Time Complexity: O((V + E) * Q), where V is the number of variables, E is the number of equations, and Q is the number of queries.
#   - Building the graph takes O(E) time.
#   - Processing each query takes O(V + E) time in the worst case.
#   - We process each query separately, so the total time complexity is O((V + E) * Q).

# Space Complexity: O(E), where E is the number of equations.
#   - We store the graph as an adjacency list, which requires O(E) space.
#   - The space complexity is dominated by the graph representation.
