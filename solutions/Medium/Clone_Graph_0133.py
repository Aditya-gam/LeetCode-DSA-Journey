from typing import Optional
from collections import deque

# Definition for a Node.


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Function: cloneGraph
        Description: Creates a deep copy of a given undirected graph.

        Parameters:
        - node (Optional[Node]): The reference to a node in the original graph.

        Returns:
        - Optional[Node]: The reference to the cloned graph.
        """
        if not node:
            return None

        # Dictionary to keep track of cloned nodes
        cloned_nodes = {}

        # BFS queue for traversal
        queue = deque([node])

        # Clone the first node
        cloned_nodes[node] = Node(node.val)

        while queue:
            original_node = queue.popleft()

            for neighbor in original_node.neighbors:
                if neighbor not in cloned_nodes:
                    # Clone the neighbor node
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Link the cloned node to its neighbors
                cloned_nodes[original_node].neighbors.append(
                    cloned_nodes[neighbor])

        return cloned_nodes[node]


# Helper function to convert adjacency list to graph
def build_graph(adj_list):
    """Builds a graph from an adjacency list representation."""
    if not adj_list:
        return None

    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}

    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[j] for j in neighbors]

    return nodes[1]  # Return the first node (val = 1)

# Helper function to convert graph to adjacency list


def graph_to_adj_list(node):
    """Converts a graph to an adjacency list representation."""
    if not node:
        return []

    visited = {}
    queue = deque([node])

    while queue:
        curr = queue.popleft()
        if curr.val not in visited:
            visited[curr.val] = [neighbor.val for neighbor in curr.neighbors]
            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)

    return [visited.get(i, []) for i in range(1, len(visited) + 1)]


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard graph
    adj_list1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    graph1 = build_graph(adj_list1)
    cloned_graph1 = solution.cloneGraph(graph1)
    print(graph_to_adj_list(cloned_graph1))
    # Expected output: [[2,4],[1,3],[2,4],[1,3]]

    # Test case 2: Single node with no edges
    adj_list2 = [[]]
    graph2 = build_graph(adj_list2)
    cloned_graph2 = solution.cloneGraph(graph2)
    print(graph_to_adj_list(cloned_graph2))
    # Expected output: [[]]

    # Test case 3: Empty graph
    adj_list3 = []
    graph3 = build_graph(adj_list3)
    cloned_graph3 = solution.cloneGraph(graph3)
    print(graph_to_adj_list(cloned_graph3))
    # Expected output: []

    # Test case 4: Graph with a single cycle
    adj_list4 = [[2], [1, 3], [2, 4], [3, 1]]
    graph4 = build_graph(adj_list4)
    cloned_graph4 = solution.cloneGraph(graph4)
    print(graph_to_adj_list(cloned_graph4))
    # Expected output: [[2],[1,3],[2,4],[3,1]]

    # Test case 5: Graph with multiple cycles
    adj_list5 = [[2, 4], [1, 3], [2, 4], [1, 3], [6], [5]]
    graph5 = build_graph(adj_list5)
    cloned_graph5 = solution.cloneGraph(graph5)
    print(graph_to_adj_list(cloned_graph5))
    # Expected output: [[2,4],[1,3],[2,4],[1,3],[6],[5]]

    # Test case 6: Graph with a single node and self-loop
    adj_list6 = [[1]]
    graph6 = build_graph(adj_list6)
    cloned_graph6 = solution.cloneGraph(graph6)
    print(graph_to_adj_list(cloned_graph6))
    # Expected output: [[1]]

    print("All clone graph test cases passed!")

# Complexity Analysis:
# Time Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.
# The algorithm traverses each node and each edge exactly once, so the time complexity is O(V + E).
# Space Complexity: O(V), where V is the number of vertices (nodes) in the graph.
# The space complexity is due to the use of the queue and the dictionary to store the cloned nodes. In the worst case, the space complexity can be O(V) if all nodes are unique.
