# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        from collections import defaultdict

        def dfs(node, currentSum):
            if not node:
                return 0

            # Update current sum
            currentSum += node.val

            # Check if there is a prefix sum that matches currentSum - targetSum
            count = prefix_sums[currentSum - targetSum]

            # Update the prefix_sums for the current path
            prefix_sums[currentSum] += 1

            # Recur for left and right children
            count += dfs(node.left, currentSum)
            count += dfs(node.right, currentSum)

            # Backtrack to remove the current node's prefix sum
            prefix_sums[currentSum] -= 1

            return count

        # Hash map to store prefix sums
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case to handle exact targetSum at the root

        return dfs(root, 0)


# Example test cases
sol = Solution()

# Test case 1
node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(-3)
node4 = TreeNode(3)
node5 = TreeNode(2)
node6 = TreeNode(11)
node7 = TreeNode(3)
node8 = TreeNode(-2)
node9 = TreeNode(1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node4.left = node7
node4.right = node8
node5.right = node9
root = node1
print(sol.pathSum(root, 8))  # Output: 3

# Test case 2
node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)

node1.left = node2
node1.right = node3
node2.left = node4
root = node1
print(sol.pathSum(root, 22))  # Output: 1


# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree.
# We visit each node once.

# Space Complexity: O(N), where N is the number of nodes in the binary tree.
# The space is used to store the prefix sums in the hash map.
