# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def searchBSTRecursive(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root or root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def searchBSTIterative(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right

        return None


# Example test cases
solution = Solution()

# Test case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
result = solution.searchBSTIterative(root, 2)
# Expected: [2,1,3]
assert result.val == 2 and result.left.val == 1 and result.right.val == 3

# Test case 2
result = solution.searchBSTRecursive(root, 5)
assert result == None  # Expected: None

# Test case 3
root = TreeNode(5)
result = solution.searchBSTIterative(root, 5)
assert result.val == 5  # Expected: [5]

# Test case 4
result = solution.searchBSTRecursive(root, 1)
assert result == None  # Expected: None

# Complexity Analysis
# Time Complexity: O(H), where H is the height of the tree.
# In the worst case, we may have to visit all nodes in the tree.

# Space Complexity: O(1) for the iterative solution and O(H) for the recursive solution due to the recursion stack.
