# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def findMin(self, node):
        """
        Find the minimum value node in a BST.
        :type node: TreeNode
        :rtype: TreeNode
        """
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        # Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to delete found
            # Case 1: Node is a leaf
            if not root.left and not root.right:
                return None
            # Case 2: Node has one child
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 3: Node has two children
            else:
                # Find the in-order successor (smallest in right subtree)
                successor = self.findMin(root.right)
                root.val = successor.val
                # Delete the in-order successor
                root.right = self.deleteNode(root.right, successor.val)

        return root


# Example test cases
solution = Solution()

# Test case 1
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
result = solution.deleteNode(root, 3)
# Expected: [5, 4, 6, 2, null, null, 7]

# Test case 2
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
result = solution.deleteNode(root, 0)
# Expected: [5, 3, 6] (no deletion as key is not found)

# Test case 3
root = None
result = solution.deleteNode(root, 0)
# Expected: None (empty tree)

# Test case 4
root = TreeNode(1)
result = solution.deleteNode(root, 1)
# Expected: None (single node deleted)

# Complexity Analysis
# Time Complexity: O(H), where H is the height of the binary tree.
# In the worst case, we may need to traverse the height of the tree.

# Space Complexity: O(H), where H is the height of the binary tree.
# The space complexity is due to the recursion stack used in the algorithm.
