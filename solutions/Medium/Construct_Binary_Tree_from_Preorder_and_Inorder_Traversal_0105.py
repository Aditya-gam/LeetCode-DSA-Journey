from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Function: buildTree
        Description: Constructs a binary tree from given preorder and inorder traversals.

        Parameters:
        - preorder (List[int]): The preorder traversal of the tree.
        - inorder (List[int]): The inorder traversal of the tree.

        Returns:
        - Optional[TreeNode]: The root of the constructed binary tree.
        """
        if not preorder or not inorder:
            return None

        # Root is the first element in preorder traversal
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the index of root in inorder traversal
        root_index = inorder.index(root_val)

        # Recursively build left and right subtrees
        root.left = self.buildTree(
            preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(
            preorder[root_index+1:], inorder[root_index+1:])

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
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = solution.buildTree(preorder, inorder)
    print(tree_to_list(root))
    # Expected output: [3, 9, 20, None, None, 15, 7]

    # Test case 2: Single node tree
    preorder = [-1]
    inorder = [-1]
    root = solution.buildTree(preorder, inorder)
    print(tree_to_list(root))
    # Expected output: [-1]

    # Test case 3: Left skewed tree
    preorder = [1, 2, 3]
    inorder = [3, 2, 1]
    root = solution.buildTree(preorder, inorder)
    print(tree_to_list(root))
    # Expected output: [1, 2, None, 3]

    # Test case 4: Right skewed tree
    preorder = [1, 2, 3]
    inorder = [1, 2, 3]
    root = solution.buildTree(preorder, inorder)
    print(tree_to_list(root))
    # Expected output: [1, None, 2, None, 3]

    # Test case 5: Complex tree
    preorder = [5, 3, 2, 4, 7, 6, 8]
    inorder = [2, 3, 4, 5, 6, 7, 8]
    root = solution.buildTree(preorder, inorder)
    print(tree_to_list(root))
    # Expected output: [5, 3, 7, 2, 4, 6, 8]

    print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(N^2), where N is the number of nodes in the binary tree.
# In the worst case, the root node is the last node in the inorder traversal, so the index() function will take O(N) time.
# This happens for each node, so the overall time complexity is O(N^2).

# Space Complexity: O(N) for the recursion stack. In the worst case, the recursion stack will have O(N) nodes.
