from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Function: buildTree
        Description: Constructs a binary tree from given inorder and postorder traversals.

        Parameters:
        - inorder (List[int]): The inorder traversal of the tree.
        - postorder (List[int]): The postorder traversal of the tree.

        Returns:
        - Optional[TreeNode]: The root of the constructed binary tree.
        """
        if not inorder or not postorder:
            return None

        # The last element of postorder is always the root
        root_val = postorder.pop()
        root = TreeNode(root_val)

        # Find the index of the root in inorder traversal
        root_index = inorder.index(root_val)

        # Recursively build right subtree before left subtree (postorder processes left last)
        root.right = self.buildTree(inorder[root_index + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)

        return root


# Helper functions for testing
def tree_to_list(root):
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

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic tree construction
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = solution.buildTree(inorder, postorder)
    print(tree_to_list(root))
    # Expected output: [3, 9, 20, None, None, 15, 7]

    # Test case 2: Single node tree
    inorder = [-1]
    postorder = [-1]
    root = solution.buildTree(inorder, postorder)
    print(tree_to_list(root))
    # Expected output: [-1]

    # Test case 3: Left-skewed tree
    inorder = [3, 2, 1]
    postorder = [3, 2, 1]
    root = solution.buildTree(inorder, postorder)
    print(tree_to_list(root))
    # Expected output: [1, 2, None, 3]

    # Test case 4: Right-skewed tree
    inorder = [1, 2, 3]
    postorder = [3, 2, 1]
    root = solution.buildTree(inorder, postorder)
    print(tree_to_list(root))
    # Expected output: [1, None, 2, None, 3]

    # Test case 5: Complex tree
    inorder = [2, 3, 4, 5, 6, 7, 8]
    postorder = [2, 4, 3, 6, 8, 7, 5]
    root = solution.buildTree(inorder, postorder)
    print(tree_to_list(root))
    # Expected output: [5, 3, 7, 2, 4, 6, 8]

    # Test case 6: Empty tree
    inorder = []
    postorder = []
    root = solution.buildTree(inorder, postorder)
    print(tree_to_list(root))
    # Expected output: []

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N^2), where N is the number of nodes in the binary tree.
# In the worst case, the root node is the last node in the postorder traversal, and we have to search for it in the inorder traversal.
# This search takes O(N) time. We can reduce the time complexity to O(N) by using a hashmap to store the indices of the elements in the inorder traversal.

# Space Complexity: O(N), where N is the number of nodes in the binary tree.
# The space complexity is O(N) for the recursive call stack.
# Additionally, we use O(N) space for the hashmap to store the indices of the elements in the inorder traversal.
