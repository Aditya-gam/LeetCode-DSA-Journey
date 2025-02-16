from collections import deque

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # Recursive solution using DFS
    def maxDepthRecursive(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

    # Iterative solution using BFS
    def maxDepthIterative(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth


# Example test cases
solution = Solution()

# Test case 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
assert solution.maxDepthRecursive(root) == 3  # Expected: 3

# Test case 2
root = TreeNode(1)
root.right = TreeNode(2)
assert solution.maxDepthIterative(root) == 2  # Expected: 2

# Test case 3
root = None
assert solution.maxDepthRecursive(root) == 0  # Expected: 0

# Test case 4
root = TreeNode(1)
assert solution.maxDepthIterative(root) == 1  # Expected: 1

print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(N) - In the worst case, we visit all nodes of the tree once.
# Space complexity:
# Recursive solution: O(H) - The maximum depth of the recursion stack is the height of the binary tree.
# Iterative solution: O(N) - The maximum number of nodes in a level of the binary tree.
