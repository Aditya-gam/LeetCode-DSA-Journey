from typing import Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    """
    Class: FindElements
    Description: Recovers a contaminated binary tree and allows efficient lookup for target values.
    """

    def __init__(self, root: Optional[TreeNode]):
        """
        Initializes the object and recovers the tree using the given rules.

        Parameters:
        - root (Optional[TreeNode]): The root of the contaminated tree (all values initially -1).
        """
        self.values = set()
        self.recover_tree(root, 0)

    def recover_tree(self, node: Optional[TreeNode], val: int):
        """
        Recovers the binary tree by assigning correct values following the rule:
        - left child = 2 * parent + 1
        - right child = 2 * parent + 2

        Parameters:
        - node (Optional[TreeNode]): Current node being processed.
        - val (int): The correct value assigned to the node.
        """
        if not node:
            return
        node.val = val
        self.values.add(val)
        self.recover_tree(node.left, 2 * val + 1)
        self.recover_tree(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        """
        Checks if the target value exists in the recovered tree.

        Parameters:
        - target (int): The value to search for.

        Returns:
        - bool: True if the target exists, False otherwise.
        """
        return target in self.values


# Helper function to create a binary tree from a level-order list
def list_to_binary_tree(lst):
    """Converts a level-order list to a binary tree."""
    if not lst or lst[0] is None:
        return None

    nodes = [TreeNode(val=-1) if val is not None else None for val in lst]

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
    # Test case 1: Recover and find values
    root = list_to_binary_tree([-1, None, -1])
    find_elements = FindElements(root)
    print(find_elements.find(1))  # Expected output: False
    print(find_elements.find(2))  # Expected output: True

    # Test case 2: Recover and check multiple values
    root = list_to_binary_tree([-1, -1, -1, -1, -1])
    find_elements = FindElements(root)
    print(find_elements.find(1))  # Expected output: True
    print(find_elements.find(3))  # Expected output: True
    print(find_elements.find(5))  # Expected output: False

    # Test case 3: Another tree structure
    root = list_to_binary_tree([-1, None, -1, -1, None, -1])
    find_elements = FindElements(root)
    print(find_elements.find(2))  # Expected output: True
    print(find_elements.find(3))  # Expected output: False
    print(find_elements.find(4))  # Expected output: False
    print(find_elements.find(5))  # Expected output: True
    print(find_elements.find(6))  # Expected output: False

    # Test case 4: Single node tree
    root = list_to_binary_tree([-1])
    find_elements = FindElements(root)
    print(find_elements.find(0))  # Expected output: True
    print(find_elements.find(1))  # Expected output: False

    # Test case 5: Empty tree
    root = list_to_binary_tree([])
    find_elements = FindElements(root)
    print(find_elements.find(0))  # Expected output: False

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(n) for initialization and O(1) for each find operation.
# - The initialization step recovers the binary tree by assigning values to each node.
# - The find operation checks if the target value exists in the recovered tree.
# - Both operations have a time complexity of O(n) and O(1), respectively.
# - Here, n is the number of nodes in the binary tree.

# Space Complexity: O(n) for initialization and O(1) for each find operation.
# - The initialization step uses O(n) space to store the recovered values.
# - The find operation uses O(1) space to check if the target value exists.
# - Here, n is the number of nodes in the binary tree.
