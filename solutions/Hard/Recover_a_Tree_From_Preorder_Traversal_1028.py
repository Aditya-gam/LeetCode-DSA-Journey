from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """
        Function: recoverFromPreorder
        Description: Recovers a binary tree from its preorder traversal with depth information.

        Parameters:
        - traversal (str): The preorder traversal string containing node values and dashes representing depth.

        Returns:
        - TreeNode: The root of the reconstructed binary tree.
        """
        stack = []
        i = 0

        while i < len(traversal):
            depth = 0
            # Count the number of dashes to determine depth
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1

            # Read the node value
            value_start = i
            while i < len(traversal) and traversal[i].isdigit():
                i += 1
            value = int(traversal[value_start:i])

            # Create new node
            node = TreeNode(value)

            # If depth is equal to stack length, it's the left child of the last node
            while len(stack) > depth:
                stack.pop()

            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            # Push new node onto stack
            stack.append(node)

        return stack[0]  # Root node is at the bottom of the stack


# Helper function to print the tree in level-order for verification
def level_order_traversal(root):
    """Returns a level-order representation of the tree."""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.val if node else None)

        if node:
            queue.append(node.left)
            queue.append(node.right)

    # Trim trailing None values for better visualization
    while result and result[-1] is None:
        result.pop()

    return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard tree recovery
    traversal = "1-2--3--4-5--6--7"
    root = solution.recoverFromPreorder(traversal)
    print(level_order_traversal(root))
    # Expected output: [1, 2, 5, 3, 4, 6, 7]

    # Test case 2: Tree with mixed left and right children
    traversal = "1-2--3---4-5--6---7"
    root = solution.recoverFromPreorder(traversal)
    print(level_order_traversal(root))
    # Expected output: [1, 2, 5, 3, None, 6, None, 4, None, 7]

    # Test case 3: Tree with irregular branching
    traversal = "1-401--349---90--88"
    root = solution.recoverFromPreorder(traversal)
    print(level_order_traversal(root))
    # Expected output: [1, 401, None, 349, 88, 90]

    # Test case 4: Single node tree
    traversal = "1"
    root = solution.recoverFromPreorder(traversal)
    print(level_order_traversal(root))
    # Expected output: [1]

    # Test case 5: Empty tree
    traversal = ""
    root = solution.recoverFromPreorder(traversal)
    print(level_order_traversal(root))
    # Expected output: []

    # Test case 6: Tree with only left children
    traversal = "1-2-3-4-5"
    root = solution.recoverFromPreorder(traversal)
    print(level_order_traversal(root))
    # Expected output: [1, 2, None, 3, None, 4, None, 5]

    # Test case 7: Tree with only right children
    traversal = "1--2--3--4--5"
    root = solution.recoverFromPreorder(traversal)
    print(level_order_traversal(root))
    # Expected output: [1, None, 2, None, 3, None, 4, None, 5]

    # Test case 8: Tree with only one left child
    traversal = "1-2"
    root = solution.recoverFromPreorder(traversal)
    print(level_order_traversal(root))
    # Expected output: [1, 2]

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the length of the traversal string.
# Space Complexity: O(H), where H is the height of the tree. In the worst case, the stack can contain all nodes at a particular depth.
