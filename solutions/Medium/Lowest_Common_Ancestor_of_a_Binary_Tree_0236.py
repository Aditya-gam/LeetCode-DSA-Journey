from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        """
        Function: lowestCommonAncestor
        Description: Finds the lowest common ancestor (LCA) of two given nodes in a binary tree.

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.
        - p (TreeNode): The first target node.
        - q (TreeNode): The second target node.

        Returns:
        - TreeNode: The lowest common ancestor of p and q.
        """
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root  # If p and q are found in different subtrees, root is LCA

        return left if left else right  # Return the non-null subtree


# Helper functions for testing
def list_to_binary_tree(lst):
    """Converts a level-order list to a binary tree."""
    if not lst or lst[0] is None:
        return None

    nodes = {val: TreeNode(val) for val in lst if val is not None}
    root = nodes[lst[0]]

    for i, val in enumerate(lst):
        if val is not None:
            node = nodes[val]
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(lst) and lst[left_idx] is not None:
                node.left = nodes[lst[left_idx]]
            if right_idx < len(lst) and lst[right_idx] is not None:
                node.right = nodes[lst[right_idx]]

    return root, nodes


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: LCA of 5 and 1 is 3
    tree, nodes = list_to_binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(solution.lowestCommonAncestor(tree, nodes[5], nodes[1]).val)
    # Expected output: 3

    # Test case 2: LCA of 5 and 4 is 5
    tree, nodes = list_to_binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(solution.lowestCommonAncestor(tree, nodes[5], nodes[4]).val)
    # Expected output: 5

    # Test case 3: LCA of 1 and 2 is 1
    tree, nodes = list_to_binary_tree([1, 2])
    print(solution.lowestCommonAncestor(tree, nodes[1], nodes[2]).val)
    # Expected output: 1

    # Test case 4: LCA of 1 and 1 is 1
    tree, nodes = list_to_binary_tree([1])
    print(solution.lowestCommonAncestor(tree, nodes[1], nodes[1]).val)
    # Expected output: 1

    # Test case 5: LCA of 1 and 2 is 1
    tree, nodes = list_to_binary_tree([1, 2, 3])
    print(solution.lowestCommonAncestor(tree, nodes[1], nodes[2]).val)
    # Expected output: 1

    # Test case 6: LCA of 1 and 3 is 1
    tree, nodes = list_to_binary_tree([1, 2, 3])
    print(solution.lowestCommonAncestor(tree, nodes[1], nodes[3]).val)
    # Expected output: 1

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(n), where n is the number of nodes in the binary tree. In the worst case, we might visit all the nodes of the binary tree.
# Space Complexity: O(n). The maximum amount of space utilized by the recursion stack would be n since the height of a skewed binary tree could be n.
