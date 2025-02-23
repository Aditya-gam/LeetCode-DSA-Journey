from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Step 1: Build the graph
        graph = defaultdict(list)
        for (A, B), value in zip(equations, values):
            graph[A].append((B, value))
            graph[B].append((A, 1 / value))

        # Step 2: Helper function for DFS
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited.add(start)
            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    res = dfs(neighbor, end, visited)
                    if res != -1.0:
                        return res * weight
            return -1.0

        # Step 3: Evaluate each query using DFS
        results = []
        for C, D in queries:
            results.append(dfs(C, D, set()))

        return results


# Example test cases
solution = Solution()

# Test case 1
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
solution = Solution()
assert solution.calcEquation(equations, values, queries) == [
    6.0, 0.5, -1.0, 1.0, -1.0]

# Test case 2
equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values = [1.5, 2.5, 5.0]
queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
assert solution.calcEquation(equations, values, queries) == [
    3.75, 0.4, 5.0, 0.2]

# Test case 3
equations = [["a", "b"]]
values = [0.5]
queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
assert solution.calcEquation(equations, values, queries) == [
    0.5, 2.0, -1.0, -1.0]

print("All test cases passed successfully.")

# Complexity analysis
# Time Complexity: O(Q×(V+E)), where Q is the number of queries. For each query, we perform a DFS traversal of the graph, which takes O(V+E) time.
# Graph construction: O(E), where E is the number of equations.
# Each DFS query: O(V+E), where V is the number of variables.

# Space Complexity: O(V+E) for the graph and recursion stack.
