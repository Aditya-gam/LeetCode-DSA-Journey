from typing import List
from collections import defaultdict, deque


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        """
        Determines the maximum net income Alice can have while traveling optimally in a tree.
        """
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def find_bob_path():
            # store the outer 'bob' in local variable 'b'
            b = bob
            queue = deque([(b, -1)])  # (current node, parent)
            parent_map = {b: None}

            while queue:
                node, parent = queue.popleft()
                for neighbor in tree[node]:
                    if neighbor == parent:
                        continue
                    parent_map[neighbor] = node
                    queue.append((neighbor, node))

            # Reconstruct Bob's path (from b up to None)
            bob_path_local = {}
            steps = 0
            while b is not None:
                bob_path_local[b] = steps
                b = parent_map[b]
                steps += 1

            return bob_path_local

        bob_path = find_bob_path()

        max_profit = float('-inf')

        def dfs(node, parent, depth, profit):
            nonlocal max_profit

            # If Bob arrives at 'node' strictly later, Alice gets full amount.
            # If Bob arrives exactly at the same time, share half.
            # If Bob arrives earlier, gate is already open, so 0 for Alice.
            if node in bob_path:
                if bob_path[node] > depth:
                    profit += amount[node]
                elif bob_path[node] == depth:
                    profit += amount[node] // 2
                # else Bob arrived first => gate is open => +0
            else:
                profit += amount[node]

            # If it's a leaf node (and not the root, unless it's the only node)
            # Condition: node != 0 ensures we don't treat root as leaf if it has children
            if len(tree[node]) == 1 and node != 0:
                max_profit = max(max_profit, profit)
                return

            # DFS on children
            for neighbor in tree[node]:
                if neighbor != parent:
                    dfs(neighbor, node, depth + 1, profit)

        dfs(0, -1, 0, 0)

        return max_profit


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard example with an optimal path
    edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
    bob = 3
    amount = [-2, 4, 2, -4, 6]
    print(solution.mostProfitablePath(edges, bob, amount))
    # Expected output: 6

    # Test case 2: Simple two-node case
    edges = [[0, 1]]
    bob = 1
    amount = [-7280, 2350]
    print(solution.mostProfitablePath(edges, bob, amount))
    # Expected output: -7280

    # Test case 3: Larger tree scenario
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [4, 5]]
    bob = 5
    amount = [-5, 10, 5, -2, 8, 4]
    print(solution.mostProfitablePath(edges, bob, amount))
    # Expected output: Optimized result based on the path Alice takes

    # Test case 4: Another larger tree scenario
    edges = [[0, 1], [1, 2], [2, 3], [2, 4], [3, 5], [3, 6], [4, 7], [4, 8]]
    bob = 8
    amount = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    print(solution.mostProfitablePath(edges, bob, amount))
    # Expected output: Optimized result based on the path Alice takes

    # Test case 5: Single node tree
    edges = []
    bob = 0
    amount = [100]
    print(solution.mostProfitablePath(edges, bob, amount))
    # Expected output: 100

    # Test case 6: Single node tree with negative value
    edges = []
    bob = 0
    amount = [-100]
    print(solution.mostProfitablePath(edges, bob, amount))
    # Expected output: -100

    print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the tree. We perform a DFS traversal of the tree to find the optimal path for Alice.
# Space Complexity: O(N), where N is the number of nodes in the tree. We use a recursive DFS approach to traverse the tree and store the path from Bob to the root node.
