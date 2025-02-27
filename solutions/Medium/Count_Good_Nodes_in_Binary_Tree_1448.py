# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_val):
            if not node:
                return 0

            # Check if the current node is a "good" node
            good = 1 if node.val >= max_val else 0

            # Update the max value for the path
            max_val = max(max_val, node.val)

            # Recur for left and right subtrees
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)

            return good

        # Start DFS with the root node
        return dfs(root, root.val)


# Example test cases
sol = Solution()

# Test case 1
node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(4)
node4 = TreeNode(3)
node5 = TreeNode(1)
node6 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
root = node1
print(sol.goodNodes(root))  # Output: 4

# Test case 2
node1 = TreeNode(3)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(2)
node1.left = node2
node1.right = node3
node2.left = node4
root = node1
print(sol.goodNodes(root))  # Output: 3

# Test case 3
node1 = TreeNode(1)
root = node1
print(sol.goodNodes(root))  # Output: 1

# Test case 4
node1 = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(2)
node5 = TreeNode(2)
node6 = TreeNode(2)
node7 = TreeNode(2)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
root = node1
print(sol.goodNodes(root))  # Output: 7

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree.
# We visit each node once.
# Space Complexity: O(H), where H is the height of the binary tree.
# The maximum depth of the recursion stack is the height of the binary tree.
