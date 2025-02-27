from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Function: isValidBST
        Description: Determines if a given binary tree is a valid Binary Search Tree (BST).

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        - bool: True if the tree is a valid BST, otherwise False.
        """
        def validate(node, low=float('-inf'), high=float('inf')):
            """
            Helper function to validate BST properties using recursion.

            Parameters:
            - node (Optional[TreeNode]): The current node being checked.
            - low (int): The lower bound for node values.
            - high (int): The upper bound for node values.

            Returns:
            - bool: True if the subtree rooted at node is a valid BST.
            """
            if not node:
                return True

            if not (low < node.val < high):
                return False  # Node value is out of valid BST bounds.

            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root)


# Helper function to construct a binary tree from a level-order list
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

    # Test case 1: Simple valid BST
    root = list_to_binary_tree([2, 1, 3])
    print(solution.isValidBST(root))
    # Expected output: True

    # Test case 2: Invalid BST (right child violates BST property)
    root = list_to_binary_tree([5, 1, 4, None, None, 3, 6])
    print(solution.isValidBST(root))
    # Expected output: False

    # Test case 3: Single node tree
    root = list_to_binary_tree([1])
    print(solution.isValidBST(root))
    # Expected output: True

    # Test case 4: Left-skewed tree (valid BST)
    root = list_to_binary_tree([5, 3, None, 2, None, 1])
    print(solution.isValidBST(root))
    # Expected output: True

    # Test case 5: Right-skewed tree (valid BST)
    root = list_to_binary_tree([1, None, 2, None, 3, None, 4])
    print(solution.isValidBST(root))
    # Expected output: True

    # Test case 6: Invalid BST (duplicate values)
    root = list_to_binary_tree([2, 2, 2])
    print(solution.isValidBST(root))
    # Expected output: False

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree. We visit each node exactly once, thus the time complexity is O(N).
# Space Complexity: O(H), where H is the height of the binary tree. The space complexity is O(H) due to the recursive calls on the stack.
# In the worst case, the tree is linear (H = N), resulting in O(N) space complexity. In the average case, the tree is balanced (H = logN), resulting in O(logN) space complexity.

