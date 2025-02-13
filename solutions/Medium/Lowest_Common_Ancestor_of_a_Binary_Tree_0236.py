# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root

        # Recursively search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return non-None, root is LCA
        if left and right:
            return root

        # Otherwise, return the non-None side
        return left if left else right


# Example test cases
# Test case 1
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
p = root.left  # Node 5
q = root.right  # Node 1
solution = Solution()
assert solution.lowestCommonAncestor(root, p, q).val == 3  # Expected: 3

# Test case 2
p = root.left  # Node 5
q = root.left.right.right  # Node 4
assert solution.lowestCommonAncestor(root, p, q).val == 5  # Expected: 5

# Test case 3
root = TreeNode(1)
root.left = TreeNode(2)
p = root
q = root.left
assert solution.lowestCommonAncestor(root, p, q).val == 1  # Expected: 1

# Test case 4
root = TreeNode(1)
root.left = TreeNode(2)
p = root.left
q = root
assert solution.lowestCommonAncestor(root, p, q).val == 1  # Expected: 1

print("All test cases pass")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree. The algorithm traverses the entire tree once.
# Space Complexity: O(H), where H is the height of the tree, due to the recursion stack.
