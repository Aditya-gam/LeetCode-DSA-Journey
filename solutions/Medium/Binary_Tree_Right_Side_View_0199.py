# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        from collections import deque
        queue = deque([root])
        right_side = []

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                # Add the last node of each level to the right_side view
                if i == level_length - 1:
                    right_side.append(node.val)
                # Enqueue left and right children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_side


# Example test cases
solution = Solution()

# Test case 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
assert solution.rightSideView(root) == [1, 3, 4]  # Expected: [1, 3, 4]

# Test case 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)
assert solution.rightSideView(root) == [1, 3, 4, 5]  # Expected: [1, 3, 4, 5]

# Test case 3
root = TreeNode(1)
root.right = TreeNode(3)
assert solution.rightSideView(root) == [1, 3]  # Expected: [1, 3]

# Test case 4
assert solution.rightSideView(None) == []  # Expected: []

# Test case 5
root = TreeNode(10)
assert solution.rightSideView(root) == [10]  # Expected: [10]

print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree.
# Space Complexity: O(D), where D is the maximum width of the tree (number of nodes at the widest level).
