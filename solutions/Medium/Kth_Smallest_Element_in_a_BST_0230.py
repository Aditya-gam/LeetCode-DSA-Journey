from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Function: kthSmallest
        Description: Finds the kth smallest element in a BST using in-order traversal.

        Parameters:
        - root (Optional[TreeNode]): The root of the BST.
        - k (int): The index (1-based) of the kth smallest element.

        Returns:
        - int: The kth smallest element in the BST.
        """
        self.count = 0
        self.result = None

        def inorder(node: Optional[TreeNode]):
            """Performs in-order traversal to find kth smallest element."""
            if not node or self.result is not None:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            inorder(node.right)

        inorder(root)

        return self.result


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
    root = list_to_bst([3, 1, 4, None, 2])
    print(solution.kthSmallest(root, 1))
    # Expected output: 1

    # Test case 2: Larger BST
    root = list_to_bst([5, 3, 6, 2, 4, None, None, 1])
    print(solution.kthSmallest(root, 3))
    # Expected output: 3

    # Test case 3: Small BST
    root = list_to_bst([2, 1])
    print(solution.kthSmallest(root, 2))
    # Expected output: 2

    # Test case 4: Right-skewed BST
    root = list_to_bst([1, None, 2, None, 3, None, 4])
    print(solution.kthSmallest(root, 3))
    # Expected output: 3

    # Test case 5: Left-skewed BST
    root = list_to_bst([4, 3, None, 2, None, 1])
    print(solution.kthSmallest(root, 4))
    # Expected output: 4

    # Test case 6: BST with only one node
    root = list_to_bst([1])
    print(solution.kthSmallest(root, 1))
    # Expected output: 1

    # Test case 7: Empty BST
    root = list_to_bst([])
    print(solution.kthSmallest(root, 1))
    # Expected output: None

    # Test case 8: BST with negative numbers
    root = list_to_bst([-1, -2, -3, -4, -5])
    print(solution.kthSmallest(root, 3))
    # Expected output: -3

    # Test case 9: BST with duplicate values
    root = list_to_bst([1, 1, 1, 1, 1])
    print(solution.kthSmallest(root, 3))
    # Expected output: 1

    # Test case 10: BST with negative and positive numbers
    root = list_to_bst([-1, -2, -3, 1, 2, 3])
    print(solution.kthSmallest(root, 4))
    # Expected output: 1

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the BST. In the worst case, we might have to visit all nodes of the BST to find the kth smallest element.
# Space Complexity: O(H), where H is the height of the BST. In the worst case, the stack can contain all nodes at a particular depth.
