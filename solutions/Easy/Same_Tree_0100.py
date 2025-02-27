from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Function: isSameTree
        Description: Checks if two binary trees are structurally identical and have the same values.

        Parameters:
        - p (Optional[TreeNode]): Root of the first binary tree.
        - q (Optional[TreeNode]): Root of the second binary tree.

        Returns:
        - bool: True if both trees are the same, otherwise False.
        """
        if not p and not q:
            return True  # Both are None, so they are the same
        if not p or not q or p.val != q.val:
            return False  # One is None, or values do not match

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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

    # Test case 1: Identical trees
    p = list_to_binary_tree([1, 2, 3])
    q = list_to_binary_tree([1, 2, 3])
    print(solution.isSameTree(p, q))
    # Expected output: True

    # Test case 2: Different structure
    p = list_to_binary_tree([1, 2])
    q = list_to_binary_tree([1, None, 2])
    print(solution.isSameTree(p, q))
    # Expected output: False

    # Test case 3: Different values
    p = list_to_binary_tree([1, 2, 1])
    q = list_to_binary_tree([1, 1, 2])
    print(solution.isSameTree(p, q))
    # Expected output: False

    # Test case 4: Both trees are empty
    p = list_to_binary_tree([])
    q = list_to_binary_tree([])
    print(solution.isSameTree(p, q))
    # Expected output: True

    # Test case 5: One tree is empty, one is not
    p = list_to_binary_tree([1])
    q = list_to_binary_tree([])
    print(solution.isSameTree(p, q))
    # Expected output: False

    # Test case 6: One tree is empty, one is not
    p = list_to_binary_tree([])
    q = list_to_binary_tree([1])
    print(solution.isSameTree(p, q))
    # Expected output: False

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the total number of nodes in the binary tree. We visit each node once.
# Space Complexity: O(H), where H is the height of the binary tree. This represents the recursive call stack space.
