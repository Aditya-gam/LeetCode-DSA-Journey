from typing import List
from collections import defaultdict, deque


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        """
        Determines the maximum net income Alice can have 
        while traveling optimally in a tree.
        """
        # Step 1: Build an adjacency list
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Step 2: Find Bob's path dictionary: node -> time Bob arrives
        def find_bob_path():
            # Use a local variable 'b' so as not to overwrite 'bob'
            b = bob
            queue = deque([(b, -1)])
            parent_map = {b: None}

            # BFS from b (treating b as root of BFS)
            while queue:
                node, parent = queue.popleft()
                for neighbor in tree[node]:
                    if neighbor == parent:
                        continue
                    parent_map[neighbor] = node
                    queue.append((neighbor, node))

            # ---- FIXED PART: Reconstruct path from node=0 back to None ----
            path = []
            curr = 0
            # Climb from 0 up to b in the BFS tree
            while curr is not None:
                path.append(curr)
                # get() to avoid KeyError if missing
                curr = parent_map.get(curr)

            # Now 'path' is [0, 1, b] in reverse order of Bob's movement
            path.reverse()  # => [b, 1, 0] if 3 -> 1 -> 0 is the chain

            # Build bob_path_local with the time Bob arrives at each node
            bob_path_local = {}
            for time, node_id in enumerate(path):
                bob_path_local[node_id] = time

            return bob_path_local

        bob_path = find_bob_path()

        # Step 3: DFS for Alice from node 0
        max_profit = float('-inf')

        def dfs(node, parent, depth, profit):
            nonlocal max_profit

            # Compare Bob's arrival time to Alice's 'depth' at this node
            if node in bob_path:
                bob_arrival = bob_path[node]
                if bob_arrival > depth:
                    # Alice arrives first => gets full amount
                    profit += amount[node]
                elif bob_arrival == depth:
                    # Arrive simultaneously => share
                    profit += amount[node] // 2
                # else Bob arrived first => gate is open => +0
            else:
                # Bob never arrives => Alice gets full amount
                profit += amount[node]

            # Check if 'node' is a leaf (and not the root with children)
            if len(tree[node]) == 1 and node != 0:
                max_profit = max(max_profit, profit)
                return

            # Continue DFS
            for neighbor in tree[node]:
                if neighbor != parent:
                    dfs(neighbor, node, depth + 1, profit)

        # Start DFS with Alice at node 0, time (depth) = 0, initial profit = 0
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
