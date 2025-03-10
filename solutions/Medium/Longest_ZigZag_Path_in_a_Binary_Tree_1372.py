# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, is_left, length, max_length):
            if not node:
                return

            # Update the global maximum length
            max_length[0] = max(max_length[0], length)

            # If the current direction is left, go to the right and vice versa
            if is_left:
                # Switch direction to right
                dfs(node.left, False, length + 1, max_length)
                # Start a new ZigZag path
                dfs(node.right, True, 1, max_length)
            else:
                # Switch direction to left
                dfs(node.right, True, length + 1, max_length)
                # Start a new ZigZag path
                dfs(node.left, False, 1, max_length)

        max_length = [0]  # Use a list to hold the max length
        # Start DFS assuming initial direction is left
        dfs(root, True, 0, max_length)
        # Start DFS assuming initial direction is right
        dfs(root, False, 0, max_length)
        return max_length[0]


# Example test cases
sol = Solution()

# Test case 1
node1 = TreeNode(1)
node2 = TreeNode(1)
node3 = TreeNode(1)
node4 = TreeNode(1)
node5 = TreeNode(1)
node6 = TreeNode(1)
node7 = TreeNode(1)
node8 = TreeNode(1)
node9 = TreeNode(1)
node10 = TreeNode(1)
node11 = TreeNode(1)
node12 = TreeNode(1)
node13 = TreeNode(1)
node14 = TreeNode(1)
node15 = TreeNode(1)
node16 = TreeNode(1)
node17 = TreeNode(1)
node18 = TreeNode(1)
node19 = TreeNode(1)
node20 = TreeNode(1)
node21 = TreeNode(1)
node22 = TreeNode(1)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node6
node4.right = node7
node5.left = node8
node5.right = node9
node3.left = node10
node3.right = node11
node10.left = node12
node10.right = node13
node11.left = node14
node11.right = node15
node12.left = node16
node12.right = node17
node13.left = node18
node13.right = node19
node14.left = node20
node14.right = node21
node15.left = node22

root = node1
print(sol.longestZigZag(root))  # Output: 4

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree. We visit each node exactly once.
# Space Complexity: O(H), where H is the height of the binary tree. The maximum depth of the recursion stack is the height of the binary tree.
