from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Function: getMinimumDifference
        Description: Finds the minimum absolute difference between any two nodes in a BST.

        Parameters:
        - root (Optional[TreeNode]): The root of the Binary Search Tree.

        Returns:
        - int: The minimum absolute difference between values of any two different nodes.
        """
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node: Optional[TreeNode]):
            """Performs in-order traversal and computes min difference."""
            if not node:
                return
            inorder(node.left)  # Traverse left subtree
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)  # Traverse right subtree

        inorder(root)

        return self.min_diff


# Helper function to construct a BST from a level-order list
def list_to_bst(lst):
    """Converts a level-order list to a BST."""
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

    # Test case 1: Standard BST
    root = list_to_bst([4, 2, 6, 1, 3])
    print(solution.getMinimumDifference(root))
    # Expected output: 1

    # Test case 2: Another BST with large numbers
    root = list_to_bst([1, 0, 48, None, None, 12, 49])
    print(solution.getMinimumDifference(root))
    # Expected output: 1

    # Test case 3: Minimum difference in a linear BST
    root = list_to_bst([5, 3, 10, 1, 4, 7, 12])
    print(solution.getMinimumDifference(root))
    # Expected output: 1

    # Test case 4: BST with only two nodes
    root = list_to_bst([1, None, 2])
    print(solution.getMinimumDifference(root))
    # Expected output: 1

    # Test case 5: BST with only one node
    root = list_to_bst([1])
    print(solution.getMinimumDifference(root))
    # Expected output: 0

    # Test case 6: Empty BST
    root = list_to_bst([])
    print(solution.getMinimumDifference(root))
    # Expected output: 0

    # Test case 7: BST with negative numbers
    root = list_to_bst([4, 2, 6, 1, 3, -1, -3])
    print(solution.getMinimumDifference(root))
    # Expected output: 1

    # Test case 8: BST with duplicate values
    root = list_to_bst([1, 1, 1, 1, 1])
    print(solution.getMinimumDifference(root))
    # Expected output: 0

    # Test case 9: BST with negative and positive numbers
    root = list_to_bst([4, 2, 6, 1, 3, -1, -3, -5])
    print(solution.getMinimumDifference(root))
    # Expected output: 1

    # Test case 10: BST with negative and positive numbers
    root = list_to_bst([4, 2, 6, 1, 3, -1, -3, -5, 5])
    print(solution.getMinimumDifference(root))
    # Expected output: 1

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the BST. We perform an in-order traversal of the tree, which takes O(N) time.
# Space Complexity: O(H), where H is the height of the BST. The space complexity is O(H) due to the recursive stack space used during the in-order traversal.
# In the worst case, the height of the BST is O(N) (unbalanced tree), and in the best case, the height is O(log N) (balanced tree).
# Therefore, the space complexity is O(N) in the worst case and O(log N) in the best case.
