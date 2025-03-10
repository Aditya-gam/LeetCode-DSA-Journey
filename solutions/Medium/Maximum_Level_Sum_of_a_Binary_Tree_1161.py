# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = deque([root])
        max_sum = float('-inf')
        max_level = 1
        current_level = 1

        while queue:
            level_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            current_level += 1

        return max_level


# Example test cases
solution = Solution()

# Test case 1
root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
assert solution.maxLevelSum(root) == 2  # Expected: 2

# Test case 2
root = TreeNode(989)
root.right = TreeNode(10250)
root.right.left = TreeNode(98693)
root.right.right = TreeNode(-89388)
root.right.right.right = TreeNode(-32127)
assert solution.maxLevelSum(root) == 2  # Expected: 2

# Test case 3
root = TreeNode(1)
assert solution.maxLevelSum(root) == 1  # Single node tree, Expected: 1

# Test case 4
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(-5)
assert solution.maxLevelSum(root) == 2  # Expected: 2

# Complexity Analysis
# time complexity: O(N), where N is the number of nodes in the tree. Each node is visited once.
# space complexity: O(M), where M is the maximum width of the tree (number of nodes at the widest level).
