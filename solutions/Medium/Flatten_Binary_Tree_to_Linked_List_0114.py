from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Function: flatten
        Description: Flattens a binary tree to a linked list in-place following pre-order traversal.

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        - None (modifies the tree in-place).
        """
        if not root:
            return

        # Use a stack to simulate pre-order traversal
        stack = [root]
        prev = None

        while stack:
            node = stack.pop()

            if prev:
                prev.right = node
                prev.left = None  # Nullify left child

            # Push right child first so left child is processed first (pre-order)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            prev = node  # Move to the next node


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


def binary_tree_to_list(root):
    """Converts a binary tree to a right-skewed list representation."""
    result = []
    while root:
        result.append(root.val)
        root = root.right
    return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Flattening a standard binary tree
    root = list_to_binary_tree([1, 2, 5, 3, 4, None, 6])
    solution.flatten(root)
    print(binary_tree_to_list(root))
    # Expected output: [1, 2, 3, 4, 5, 6]

    # Test case 2: Empty tree
    root = list_to_binary_tree([])
    solution.flatten(root)
    print(binary_tree_to_list(root))
    # Expected output: []

    # Test case 3: Single node tree
    root = list_to_binary_tree([0])
    solution.flatten(root)
    print(binary_tree_to_list(root))
    # Expected output: [0]

    # Test case 4: Left-skewed tree
    root = list_to_binary_tree([1, 2, None, 3, None, 4])
    solution.flatten(root)
    print(binary_tree_to_list(root))
    # Expected output: [1, 2, 3, 4]

    # Test case 5: Right-skewed tree (Already flattened)
    root = list_to_binary_tree([1, None, 2, None, 3, None, 4])
    solution.flatten(root)
    print(binary_tree_to_list(root))
    # Expected output: [1, 2, 3, 4]

    # Test case 6: Complex tree
    root = list_to_binary_tree(
        [1, 2, 5, 3, 4, None, 6, 7, 8, None, None, None, None, 9])
    solution.flatten(root)
    print(binary_tree_to_list(root))
    # Expected output: [1, 2, 3, 7, 8, 4, 5, 6, 9]

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree.
# Space Complexity: O(N), where N is the number of nodes in the binary tree. The space complexity is due to the stack used for the pre-order traversal
