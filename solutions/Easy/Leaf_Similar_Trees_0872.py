# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def get_leaf_sequence(root):
            """
            Helper function to get the leaf sequence of a tree.
            """
            if not root:
                return []

            stack = [root]
            leaf_sequence = []

            while stack:
                node = stack.pop()
                if not node.left and not node.right:  # Leaf node
                    leaf_sequence.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

            return leaf_sequence

        # Get leaf sequences for both trees
        leaf_sequence1 = get_leaf_sequence(root1)
        leaf_sequence2 = get_leaf_sequence(root2)

        # Compare the leaf sequences
        return leaf_sequence1 == leaf_sequence2


# Example test cases
solution = Solution()

# Test case 1
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

assert solution.leafSimilar(root1, root2) == True  # Expected: True

# Test case 2
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.right = TreeNode(2)

assert solution.leafSimilar(root1, root2) == False  # Expected: False

# Test case 3
root1 = TreeNode(1)
root2 = TreeNode(1)
assert solution.leafSimilar(root1, root2) == True  # Expected: True

# Complexity Analysis
# Time Complexity: O(N1 + N2), where N1 and N2 are the number of nodes in the two trees.
# The algorithm traverses both trees once to get the leaf sequences.

# Space Complexity: O(H1 + H2), where H1 and H2 are the heights of the two trees.
# The space complexity is due to the stack used to traverse the trees.
