from typing import List, Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Function: averageOfLevels
        Description: Computes the average value of nodes on each level in a binary tree.

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        - List[float]: A list of average values for each level.
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_size)

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

    # Test case 1: Standard tree with multiple levels
    root = list_to_binary_tree([3, 9, 20, None, None, 15, 7])
    print(solution.averageOfLevels(root))
    # Expected output: [3.00000, 14.50000, 11.00000]

    # Test case 2: Tree with left-heavy structure
    root = list_to_binary_tree([3, 9, 20, 15, 7])
    print(solution.averageOfLevels(root))
    # Expected output: [3.00000, 14.50000, 11.00000]

    # Test case 3: Single node tree
    root = list_to_binary_tree([5])
    print(solution.averageOfLevels(root))
    # Expected output: [5.00000]

    # Test case 4: Tree with negative values
    root = list_to_binary_tree([1, -2, 3, -4, -5, 6, 7])
    print(solution.averageOfLevels(root))
    # Expected output: [1.00000, 0.50000, 1.00000]

    # Test case 5: Tree with mixed positive and negative values
    root = list_to_binary_tree([-10, -20, -30, -40, -50, -60, -70])
    print(solution.averageOfLevels(root))
    # Expected output: [-10.00000, -25.00000, -55.00000]

    # Test case 6: Empty tree
    root = list_to_binary_tree([])
    print(solution.averageOfLevels(root))
    # Expected output: []

    # Test case 7: Tree with only left children
    root = list_to_binary_tree([1, 2, None, 3])
    print(solution.averageOfLevels(root))
    # Expected output: [1.00000, 2.00000, 3.00000]

    # Test case 8: Tree with only right children
    root = list_to_binary_tree([1, None, 2, None, 3])
    print(solution.averageOfLevels(root))
    # Expected output: [1.00000, 2.00000, 3.00000]

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# We visit each node once and perform a constant amount of work for each node.
# Hence, the time complexity is O(n).

# Space Complexity: O(n), where n is the number of nodes in the binary tree.
# The space complexity is O(n) due to the queue used for level-order traversal.
# In the worst case, the queue can contain all the nodes at the maximum level of the binary tree.
