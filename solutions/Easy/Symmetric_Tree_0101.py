from typing import Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Function: isSymmetric
        Description: Checks if a binary tree is symmetric around its center.

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        - bool: True if the tree is symmetric, otherwise False.
        """
        if not root:
            return True

        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            """
            Helper function to check if two subtrees are mirror images of each other.
            """
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root.left, root.right)

    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative approach using a queue.
        """
        if not root:
            return True

        queue = deque([(root.left, root.right)])

        while queue:
            t1, t2 = queue.popleft()

            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False

            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))

        return True


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

    # Test case 1: Symmetric tree
    root = list_to_binary_tree([1, 2, 2, 3, 4, 4, 3])
    print(solution.isSymmetric(root))  # Expected output: True
    print(solution.isSymmetricIterative(root))  # Expected output: True

    # Test case 2: Asymmetric tree
    root = list_to_binary_tree([1, 2, 2, None, 3, None, 3])
    print(solution.isSymmetric(root))  # Expected output: False
    print(solution.isSymmetricIterative(root))  # Expected output: False

    # Test case 3: Single node tree
    root = list_to_binary_tree([1])
    print(solution.isSymmetric(root))  # Expected output: True
    print(solution.isSymmetricIterative(root))  # Expected output: True

    # Test case 4: Empty tree
    root = list_to_binary_tree([])
    print(solution.isSymmetric(root))  # Expected output: True
    print(solution.isSymmetricIterative(root))  # Expected output: True

    # Test case 5: Larger symmetric tree
    root = list_to_binary_tree([1, 2, 2, 3, 4, 4, 3, None, None, 5, 6, 6, 5])
    print(solution.isSymmetric(root))  # Expected output: True
    print(solution.isSymmetricIterative(root))  # Expected output: True

    # Test case 6: Larger asymmetric tree
    root = list_to_binary_tree(
        [1, 2, 2, 3, 4, 4, 3, None, None, 5, 6, 6, None, 5])
    print(solution.isSymmetric(root))  # Expected output: False
    print(solution.isSymmetricIterative(root))  # Expected output: False

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree. We traverse the entire tree once, so the time complexity is O(N).

# Space Complexity: O(N) for the recursive approach and O(N) for the iterative approach.
# In the recursive approach, the maximum depth of the recursion stack is the height of the tree, which is O(N) in the worst case.
# In the iterative approach, the queue can contain up to O(N) nodes in the worst case.
