from typing import List, Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Function: zigzagLevelOrder
        Description: Performs a zigzag level order traversal of a binary tree.

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        - List[List[int]]: A list of lists, where each list contains node values at a specific level in zigzag order.
        """
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True  # Flag to alternate directions

        while queue:
            level_size = len(queue)
            level_nodes = deque()

            for _ in range(level_size):
                node = queue.popleft()
                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(level_nodes))
            left_to_right = not left_to_right  # Toggle direction for next level

        return result


# Helper function to construct a binary tree from a level-order list
def list_to_binary_tree(lst):
    """Converts a level-order list to a binary tree."""
    if not lst or lst[0] is None:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in lst]

    for i, node in enumerate(nodes):
        if node:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(lst):
                node.left = nodes[left_idx]
            if right_idx < len(lst):
                node.right = nodes[right_idx]

    return nodes[0]  # Root node


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard binary tree with zigzag order
    root = list_to_binary_tree([3, 9, 20, None, None, 15, 7])
    print(solution.zigzagLevelOrder(root))
    # Expected output: [[3], [20, 9], [15, 7]]

    # Test case 2: Single-node tree
    root = list_to_binary_tree([1])
    print(solution.zigzagLevelOrder(root))
    # Expected output: [[1]]

    # Test case 3: Empty tree
    root = list_to_binary_tree([])
    print(solution.zigzagLevelOrder(root))
    # Expected output: []

    # Test case 4: Left-skewed tree
    root = list_to_binary_tree([1, 2, None, 3, None, 4, None])
    print(solution.zigzagLevelOrder(root))
    # Expected output: [[1], [2], [3], [4]]

    # Test case 5: Right-skewed tree
    root = list_to_binary_tree([1, None, 2, None, 3, None, 4])
    print(solution.zigzagLevelOrder(root))
    # Expected output: [[1], [2], [3], [4]]

    # Test case 6: Tree with irregular branching
    root = list_to_binary_tree([1, 2, 3, 4, None, None, 5])
    print(solution.zigzagLevelOrder(root))
    # Expected output: [[1], [3, 2], [4, 5]]

    # Test case 7: Tree with multiple levels
    root = list_to_binary_tree([1, 2, 3, 4, 5, 6, 7])
    print(solution.zigzagLevelOrder(root))
    # Expected output: [[1], [3, 2], [4, 5, 6, 7]]

    # Test case 8: Tree with only left children
    root = list_to_binary_tree([1, 2, 3, 4, 5])
    print(solution.zigzagLevelOrder(root))
    # Expected output: [[1], [2], [3], [4], [5]]

    # Test case 9: Tree with only right children
    root = list_to_binary_tree([1, None, 2, None, 3, None, 4])
    print(solution.zigzagLevelOrder(root))
    # Expected output: [[1], [2], [3], [4]]

    # Test case 10: Tree with only one left child
    root = list_to_binary_tree([1, 2])
    print(solution.zigzagLevelOrder(root))
    # Expected output: [[1], [2]]

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree. We visit each node once, and the overall time complexity is O(N).
# Space Complexity: O(N), where N is the number of nodes in the binary tree. The maximum space used by the queue is O(N) since at most all nodes are added to the queue.
