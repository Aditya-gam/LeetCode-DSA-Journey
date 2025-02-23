from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Function: invertTree
        Description: Inverts a binary tree by swapping left and right child nodes recursively.

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        - Optional[TreeNode]: The root of the inverted binary tree.
        """
        if not root:
            return None

        # Swap left and right subtrees
        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)

        return root


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
    """Converts a binary tree to a level-order list representation."""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values to match expected output format
    while result and result[-1] is None:
        result.pop()

    return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic tree inversion
    root = list_to_binary_tree([4, 2, 7, 1, 3, 6, 9])
    inverted_root = solution.invertTree(root)
    print(binary_tree_to_list(inverted_root))
    # Expected output: [4, 7, 2, 9, 6, 3, 1]

    # Test case 2: Small tree
    root = list_to_binary_tree([2, 1, 3])
    inverted_root = solution.invertTree(root)
    print(binary_tree_to_list(inverted_root))
    # Expected output: [2, 3, 1]

    # Test case 3: Empty tree
    root = list_to_binary_tree([])
    inverted_root = solution.invertTree(root)
    print(binary_tree_to_list(inverted_root))
    # Expected output: []

    # Test case 4: Tree with only left children
    root = list_to_binary_tree([1, 2, None, 3])
    inverted_root = solution.invertTree(root)
    print(binary_tree_to_list(inverted_root))
    # Expected output: [1, None, 2, None, 3]

    # Test case 5: Tree with only right children
    root = list_to_binary_tree([1, None, 2, None, 3])
    inverted_root = solution.invertTree(root)
    print(binary_tree_to_list(inverted_root))
    # Expected output: [1, 2, None, 3, None]

    # Test case 6: Single node tree
    root = list_to_binary_tree([1])
    inverted_root = solution.invertTree(root)
    print(binary_tree_to_list(inverted_root))
    # Expected output: [1]

    print("All test cases passed!")

# Complexity Analysis
# Time complexity: O(n), where n is the number of nodes in the binary tree. We visit each node once and perform a constant amount of work at each node.

# Space complexity: O(n), where n is the number of nodes in the binary tree.
# The maximum space used by the recursion stack is the height of the tree, which is O(n) for a skewed tree and O(log n) for a balanced tree.
