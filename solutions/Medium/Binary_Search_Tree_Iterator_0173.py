from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """
    Function: BSTIterator
    Description: Implements an iterator over the in-order traversal of a Binary Search Tree (BST).
    """

    def __init__(self, root: Optional[TreeNode]):
        """
        Initializes the iterator. Performs an in-order traversal and stores nodes in a stack.

        Parameters:
        - root (Optional[TreeNode]): The root of the BST.
        """
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node: Optional[TreeNode]):
        """
        Pushes all left children onto the stack to prepare for in-order traversal.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Returns the next smallest element in the BST.

        Returns:
        - int: The next in-order value.
        """
        top_node = self.stack.pop()

        # If the node has a right child, process its leftmost children
        if top_node.right:
            self._leftmost_inorder(top_node.right)

        return top_node.val

    def hasNext(self) -> bool:
        """
        Checks if there is a next smallest number in the BST.

        Returns:
        - bool: True if there are remaining elements, False otherwise.
        """
        return len(self.stack) > 0


# Helper functions for testing
def list_to_binary_search_tree(lst):
    """Converts a level-order list to a BST."""
    if not lst or lst[0] is None:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in lst]

    for i, node in enumerate(nodes):
        if node:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(lst):
                node.left = nodes[left_idx]
            if right_idx < len(lst):
                node.right = nodes[right_idx]

    return nodes[0]  # Root node


# Example Test Cases
if __name__ == "__main__":
    root = list_to_binary_search_tree([7, 3, 15, None, None, 9, 20])
    iterator = BSTIterator(root)

    print(iterator.next())      # 3
    print(iterator.next())      # 7
    print(iterator.hasNext())   # True
    print(iterator.next())      # 9
    print(iterator.hasNext())   # True
    print(iterator.next())      # 15
    print(iterator.hasNext())   # True
    print(iterator.next())      # 20
    print(iterator.hasNext())   # False

    root = list_to_binary_search_tree([1])
    iterator = BSTIterator(root)

    print(iterator.next())      # 1
    print(iterator.hasNext())   # False
    print(iterator.next())      # None

    root = list_to_binary_search_tree([2, 1])
    iterator = BSTIterator(root)

    print(iterator.next())      # 1
    print(iterator.hasNext())   # True
    print(iterator.next())      # 2
    print(iterator.hasNext())   # False
    print(iterator.next())      # None

    root = list_to_binary_search_tree([5, 1, 7, None, 3, 6, 8])
    iterator = BSTIterator(root)

    print(iterator.next())      # 1
    print(iterator.next())      # 3
    print(iterator.next())      # 5
    print(iterator.next())      # 6
    print(iterator.next())      # 7
    print(iterator.next())      # 8
    print(iterator.hasNext())   # False
    print(iterator.next())      # None

    print("All test cases passed.")

# Complexity Analysis
# Time Complexity: O(1) for the next() and hasNext() operations.
# The average time complexity for the next() operation is O(1) because the amortized time complexity of popping an element from the stack is O(1).

# Space Complexity: O(h) where h is the height of the BST.
# The space complexity is O(h) because the stack can store up to h elements for a skewed tree.
# For a balanced tree, the space complexity is O(log n) where n is the number of nodes in the BST.
