from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Function: maxPathSum
        Description: Finds the maximum path sum of any non-empty path in a binary tree.

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        - int: The maximum path sum.
        """
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Compute the max path sum for left and right subtrees
            left_max = max(dfs(node.left), 0)  # Ignore negative paths
            right_max = max(dfs(node.right), 0)

            # Compute the max path sum passing through the current node
            current_path_sum = node.val + left_max + right_max

            # Update global max path sum
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the max sum of path ending at the current node
            return node.val + max(left_max, right_max)

        dfs(root)

        return self.max_sum


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

    # Test case 1: Simple tree
    root = list_to_binary_tree([1, 2, 3])
    print(solution.maxPathSum(root))
    # Expected output: 6 (2 -> 1 -> 3)

    # Test case 2: Tree with negative values
    root = list_to_binary_tree([-10, 9, 20, None, None, 15, 7])
    print(solution.maxPathSum(root))
    # Expected output: 42 (15 -> 20 -> 7)

    # Test case 3: Single node tree
    root = list_to_binary_tree([5])
    print(solution.maxPathSum(root))
    # Expected output: 5

    # Test case 4: Tree with only negative numbers
    root = list_to_binary_tree([-3])
    print(solution.maxPathSum(root))
    # Expected output: -3

    # Test case 5: Complex tree with mixed values
    root = list_to_binary_tree(
        [10, 2, 10, 20, 1, None, -25, None, None, None, None, None, None, 3, 4])
    print(solution.maxPathSum(root))
    # Expected output: 42 (20 -> 2 -> 10 -> 10)

    # Test case 6: Large tree
    root = list_to_binary_tree(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print(solution.maxPathSum(root))
    # Expected output: 60 (15 -> 14 -> 13 -> 12 -> 11 -> 10 -> 9 -> 8 -> 7 -> 6)

    # Test case 7: Large tree with negative values
    root = list_to_binary_tree(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, -15])
    print(solution.maxPathSum(root))
    # Expected output: 56 (14 -> 13 -> 12 -> 11 -> 10 -> 9 -> 8 -> 7 -> 6)

    # Test case 8: Large tree with negative values
    root = list_to_binary_tree(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -13, -14, -15])
    print(solution.maxPathSum(root))
    # Expected output: 56 (11 -> 10 -> 9 -> 8 -> 7 -> 6)

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree. We visit each node once.
# Space Complexity: O(H), where H is the height of the binary tree. This space is used for the recursive call stack.
# In the worst case, the height of the binary tree is O(N), leading to a space complexity of O(N). In the average case, the space complexity is O(log(N)).
# In the worst case, the space complexity is O(N) for a skewed binary tree.
# In the average case, the space complexity is O(log(N)) for a balanced binary tree.
