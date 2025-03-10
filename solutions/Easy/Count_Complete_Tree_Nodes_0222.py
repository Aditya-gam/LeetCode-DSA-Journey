from typing import Optional, List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Counts the number of nodes in a complete binary tree using an approach
    that runs in O((log n)^2) time, leveraging the fact that some subtrees
    can be computed in constant time if they're perfect.
    """

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Compute the height of the leftmost branch
        left_height = self.get_height_left(root)
        # Compute the height of the rightmost branch
        right_height = self.get_height_right(root)

        # If heights match, it's a perfect binary tree at this level
        if left_height == right_height:
            # Node count of a perfect tree of height h is (2^h - 1)
            return (2 ** left_height) - 1
        else:
            # Otherwise, recursively count left & right
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_height_left(self, node: Optional[TreeNode]) -> int:
        """Returns the height of the tree by traversing left pointers."""
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def get_height_right(self, node: Optional[TreeNode]) -> int:
        """Returns the height of the tree by traversing right pointers."""
        height = 0
        while node:
            height += 1
            node = node.right
        return height


# ------------------------- TEST CASES -------------------------
def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Builds a complete binary tree from a level-order list. 
    None indicates an absent child.
    """
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        current = queue.popleft()
        if current:
            # Left child
            if values[i] is not None:
                current.left = TreeNode(values[i])
            queue.append(current.left)
            i += 1
            if i >= len(values):
                break
            # Right child
            if values[i] is not None:
                current.right = TreeNode(values[i])
            queue.append(current.right)
            i += 1
    return root


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Example provided
    root1 = build_tree_from_list([1, 2, 3, 4, 5, 6])
    print("Test Case 1:", solution.countNodes(root1))
    # Expected: 6

    # Test Case 2: Empty tree
    root2 = build_tree_from_list([])
    print("Test Case 2:", solution.countNodes(root2))
    # Expected: 0

    # Test Case 3: Single node
    root3 = build_tree_from_list([1])
    print("Test Case 3:", solution.countNodes(root3))
    # Expected: 1

    # Test Case 4: Perfect binary tree of height 3 => 7 nodes
    # Level order: [1,2,3,4,5,6,7]
    root4 = build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    print("Test Case 4:", solution.countNodes(root4))
    # Expected: 7

    # Test Case 5: Last level not fully filled but still complete: [1,2,3,4,5,6,None]
    # Should have 6 nodes
    root5 = build_tree_from_list([1, 2, 3, 4, 5, 6, None])
    print("Test Case 5:", solution.countNodes(root5))
    # Expected: 6

# ------------------- COMPLEXITY ANALYSIS -------------------
# - Time Complexity: O((log n)^2).
#   Each node's height check is O(log n), and we do this at most O(log n) times.
# - Space Complexity: O(log n) due to recursion stack, at worst for a complete tree.
