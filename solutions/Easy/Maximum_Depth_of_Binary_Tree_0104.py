from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Function: maxDepth
        Description: Computes the maximum depth of a binary tree using recursion.

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        - int: The maximum depth of the binary tree.
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


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

    # Test case 1: Standard tree
    root = list_to_binary_tree([3, 9, 20, None, None, 15, 7])
    print(solution.maxDepth(root))
    # Expected output: 3

    # Test case 2: Single node tree
    root = list_to_binary_tree([1])
    print(solution.maxDepth(root))
    # Expected output: 1

    # Test case 3: Unbalanced tree
    root = list_to_binary_tree([1, None, 2])
    print(solution.maxDepth(root))
    # Expected output: 2

    # Test case 4: Deeper unbalanced tree
    root = list_to_binary_tree([1, 2, None, 3, None, None, None, 4])
    print(solution.maxDepth(root))
    # Expected output: 4

    # Test case 5: Empty tree
    root = list_to_binary_tree([])
    print(solution.maxDepth(root))
    # Expected output: 0

    # Test case 6: Full tree
    root = list_to_binary_tree([1, 2, 3, 4, 5, 6, 7])
    print(solution.maxDepth(root))
    # Expected output: 3

    # Test case 7: Full tree with different depths
    root = list_to_binary_tree([1, 2, 2, 3, 3, 3, 3])
    print(solution.maxDepth(root))
    # Expected output: 3

    # Test case 8: Full tree with different depths
    root = list_to_binary_tree([1, 2, 2, 3, 3, 3, 3, 4])
    print(solution.maxDepth(root))
    # Expected output: 4

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree. We visit each node once.
# Space Complexity: O(H), where H is the height of the binary tree. This represents the maximum depth of the recursion stack.
