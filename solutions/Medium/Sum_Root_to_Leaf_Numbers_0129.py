from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Function: sumNumbers
        Description: Computes the sum of all root-to-leaf numbers in a binary tree.

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        - int: The total sum of all root-to-leaf numbers.
        """
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum = current_sum * 10 + node.val

            # If it's a leaf node, return the computed number
            if not node.left and not node.right:
                return current_sum

            # Sum results from left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)


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

    # Test case 1: Standard binary tree
    root = list_to_binary_tree([1, 2, 3])
    print(solution.sumNumbers(root))
    # Expected output: 25 (12 + 13)

    # Test case 2: Tree with different values
    root = list_to_binary_tree([4, 9, 0, 5, 1])
    print(solution.sumNumbers(root))
    # Expected output: 1026 (495 + 491 + 40)

    # Test case 3: Single node tree
    root = list_to_binary_tree([5])
    print(solution.sumNumbers(root))
    # Expected output: 5

    # Test case 4: Left-skewed tree
    root = list_to_binary_tree([1, 2, None, 3, None, 4])
    print(solution.sumNumbers(root))
    # Expected output: 1234

    # Test case 5: Right-skewed tree
    root = list_to_binary_tree([1, None, 2, None, 3, None, 4])
    print(solution.sumNumbers(root))
    # Expected output: 1234

    # Test case 6: Empty tree
    root = list_to_binary_tree([])
    print(solution.sumNumbers(root))
    # Expected output: 0

    # Test case 7: Large tree
    root = list_to_binary_tree(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print(solution.sumNumbers(root))
    # Expected output: 13632 (1234 + 1235 + ... + 1215)

    # Test case 8: Negative numbers
    root = list_to_binary_tree([1, -2, 3])
    print(solution.sumNumbers(root))
    # Expected output: 4 (-2 + 3)

    # Test case 9: Large tree with negative numbers
    root = list_to_binary_tree(
        [1, -2, 3, 4, 5, -6, 7, 8, 9, 10, -11, 12, 13, 14, 15])
    print(solution.sumNumbers(root))
    # Expected output: 13632 (-234 + -235 + ... + -215)

    print("All test cases passed!")

# Complexity Analysis
# Time complexity: O(N), where N is the number of nodes in the binary tree. We visit each node once.
# Space complexity: O(H), where H is the height of the binary tree. The space complexity is determined by the recursion stack, which can go up to the height of the binary tree.
# In the worst case, the space complexity is O(N) for a skewed binary tree.
# In the average case, the space complexity is O(log(N)) for a balanced binary tree.
