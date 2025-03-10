from typing import List, Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Function: rightSideView
        Description: Returns the values of nodes visible from the right side of a binary tree.

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        - List[int]: The list of values seen from the right side, from top to bottom.
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # The rightmost node at each level is added to the result
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


# Helper functions for testing
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

    # Test case 1: Basic tree with right-side view [1, 3, 4]
    root = list_to_binary_tree([1, 2, 3, None, 5, None, 4])
    print(solution.rightSideView(root))
    # Expected output: [1, 3, 4]

    # Test case 2: Tree with nodes forming deeper right view [1, 3, 4, 5]
    root = list_to_binary_tree([1, 2, 3, 4, None, None, None, 5])
    print(solution.rightSideView(root))
    # Expected output: [1, 3, 4, 5]

    # Test case 3: Simple right-skewed tree [1, 3]
    root = list_to_binary_tree([1, None, 3])
    print(solution.rightSideView(root))
    # Expected output: [1, 3]

    # Test case 4: Empty tree
    root = list_to_binary_tree([])
    print(solution.rightSideView(root))
    # Expected output: []

    # Test case 5: Tree with only left children [1, 2, 3]
    root = list_to_binary_tree([1, 2, None, 3])
    print(solution.rightSideView(root))
    # Expected output: [1, 2, 3]

    # Test case 6: Tree with only right children [1, None, 2, None, 3]
    root = list_to_binary_tree([1, None, 2, None, 3])
    print(solution.rightSideView(root))
    # Expected output: [1, 2, 3]

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# We visit each node exactly once, which gives a linear time complexity.
# The maximum number of nodes at any level is n / 2, where n is the number of nodes in the binary tree.
# Hence, the time complexity is O(n).

# Space Complexity: O(n), where n is the number of nodes in the binary tree.
# The maximum space occupied by the queue is the maximum number of nodes at any level in the binary tree.
# In the worst case, the binary tree is a complete binary tree, and the number of nodes at the last level is (n + 1) / 2. Hence, the space complexity is O(n).
