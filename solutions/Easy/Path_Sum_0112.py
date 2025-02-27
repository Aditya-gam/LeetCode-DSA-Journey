from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Function: hasPathSum
        Description: Checks if the tree has a root-to-leaf path with a sum equal to targetSum.

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.
        - targetSum (int): The target sum to check.

        Returns:
        - bool: True if there exists a root-to-leaf path with sum == targetSum, otherwise False.
        """
        if not root:
            return False

        # If it's a leaf node, check if the remaining sum matches
        if not root.left and not root.right:
            return targetSum == root.val

        # Recursively check left and right subtrees
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


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

    # Test case 1: Valid path with target sum
    root = list_to_binary_tree(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    print(solution.hasPathSum(root, 22))
    # Expected output: True

    # Test case 2: No valid path
    root = list_to_binary_tree([1, 2, 3])
    print(solution.hasPathSum(root, 5))
    # Expected output: False

    # Test case 3: Empty tree
    root = list_to_binary_tree([])
    print(solution.hasPathSum(root, 0))
    # Expected output: False

    # Test case 4: Single node, valid path
    root = list_to_binary_tree([5])
    print(solution.hasPathSum(root, 5))
    # Expected output: True

    # Test case 5: Single node, invalid path
    root = list_to_binary_tree([1])
    print(solution.hasPathSum(root, 2))
    # Expected output: False

    # Test case 6: Negative numbers
    root = list_to_binary_tree([1, 2, 3])
    print(solution.hasPathSum(root, 4))
    # Expected output: True

    # Test case 7: Large tree
    root = list_to_binary_tree(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print(solution.hasPathSum(root, 15))
    # Expected output: True

    # Test case 8: Large tree, invalid path
    root = list_to_binary_tree(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print(solution.hasPathSum(root, 16))
    # Expected output: False

    # Test case 9: Large tree, negative numbers
    root = list_to_binary_tree(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print(solution.hasPathSum(root, 10))
    # Expected output: True

    # Test case 10: Large tree, negative numbers, invalid path
    root = list_to_binary_tree(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print(solution.hasPathSum(root, 20))
    # Expected output: False

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree. We visit each node exactly once.
# Space Complexity: O(H), where H is the height of the binary tree. In the worst case, the space complexity is O(N) due to the recursive call stack.
# In the average case, the space complexity is O(log(N)).
