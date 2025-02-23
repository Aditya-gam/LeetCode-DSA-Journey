from typing import Optional
from collections import deque

# Definition for a Node.


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        """
        Function: connect
        Description: Populates each next pointer of a binary tree to point to its next right node.
                     Uses a level-order traversal approach with constant extra space.

        Parameters:
        - root (Optional[Node]): The root of the binary tree.

        Returns:
        - Optional[Node]: The root of the modified binary tree.
        """
        if not root:
            return None

        # Start with the root node
        current = root
        dummy = Node(0)  # Dummy node for linking level's next pointers

        while current:
            tail = dummy  # Reset dummy's tail pointer
            dummy.next = None  # Reset for next level

            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                current = current.next  # Move to next node in the same level

            current = dummy.next  # Move to the next level

        return root


# Helper functions for testing
def list_to_binary_tree(lst):
    """Converts a level-order list to a binary tree."""
    if not lst or lst[0] is None:
        return None

    nodes = [Node(val) if val is not None else None for val in lst]

    for i, node in enumerate(nodes):
        if node:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(lst):
                node.left = nodes[left_idx]
            if right_idx < len(lst):
                node.right = nodes[right_idx]

    return nodes[0]  # Root node


def binary_tree_to_list_with_next(root):
    """Converts a binary tree to a level-order list representation with 'next' pointers."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        result.append("#")  # End of level

    # Remove trailing '#' and None values
    while result and result[-1] in (None, "#"):
        result.pop()

    return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Populating next pointers in a tree
    root = list_to_binary_tree([1, 2, 3, 4, 5, None, 7])
    connected_root = solution.connect(root)
    print(binary_tree_to_list_with_next(connected_root))
    # Expected output: [1, '#', 2, 3, '#', 4, 5, 7, '#']

    # Test case 2: Empty tree
    root = list_to_binary_tree([])
    connected_root = solution.connect(root)
    print(binary_tree_to_list_with_next(connected_root))
    # Expected output: []

    # Test case 3: Single node tree
    root = list_to_binary_tree([1])
    connected_root = solution.connect(root)
    print(binary_tree_to_list_with_next(connected_root))
    # Expected output: [1, '#']

    # Test case 4: Full binary tree
    root = list_to_binary_tree([1, 2, 3, 4, 5, 6, 7])
    connected_root = solution.connect(root)
    print(binary_tree_to_list_with_next(connected_root))
    # Expected output: [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']

    # Test case 5: Right skewed tree
    root = list_to_binary_tree([1, None, 2, None, 3, None, 4])
    connected_root = solution.connect(root)
    print(binary_tree_to_list_with_next(connected_root))
    # Expected output: [1, '#', 2, '#', 3, '#', 4, '#']

    # Test case 6: Left skewed tree
    root = list_to_binary_tree([1, 2, None, 3, None, 4, None])
    connected_root = solution.connect(root)
    print(binary_tree_to_list_with_next(connected_root))
    # Expected output: [1, '#', 2, '#', 3, '#', 4, '#']

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree.
# Space Complexity: O(1), since we are using only constant extra space.
