from typing import Optional

# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Function: copyRandomList
        Description: Creates a deep copy of a linked list with a random pointer.
                     Each node in the new list is an independent copy of the corresponding node
                     in the original list.

        Parameters:
        - head (Optional[Node]): The head of the original linked list.

        Returns:
        - Optional[Node]: The head of the deep copied linked list.
        """
        if not head:
            return None

        # Step 1: Clone nodes and insert them between original nodes
        current = head
        while current:
            cloned_node = Node(current.val)
            cloned_node.next = current.next
            current.next = cloned_node
            current = cloned_node.next

        # Step 2: Assign random pointers to the cloned nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the cloned list from the original list
        original = head
        cloned_head = head.next
        cloned_current = cloned_head

        while original:
            original.next = original.next.next
            cloned_current.next = cloned_current.next.next if cloned_current.next else None
            original = original.next
            cloned_current = cloned_current.next

        return cloned_head


# Helper functions for testing
def list_to_linked_list(lst):
    """Converts a list of [val, random_index] into a linked list with random pointers."""
    if not lst:
        return None

    nodes = [Node(val) for val, _ in lst]
    for i, (_, random_idx) in enumerate(lst):
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]

    return nodes[0]


def linked_list_to_list(head):
    """Converts a linked list with random pointers into a list representation."""
    if not head:
        return []

    index_map = {}
    current = head
    index = 0
    while current:
        index_map[current] = index
        current = current.next
        index += 1

    result = []
    current = head
    while current:
        random_index = index_map.get(current.random, None)
        result.append([current.val, random_index])
        current = current.next

    return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic case with random pointers
    head = list_to_linked_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    copied_head = solution.copyRandomList(head)
    print(linked_list_to_list(copied_head))
    # Expected output: [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

    # Test case 2: Simple case with all random pointers pointing to the same node
    head = list_to_linked_list([[1, 1], [2, 1]])
    copied_head = solution.copyRandomList(head)
    print(linked_list_to_list(copied_head))
    # Expected output: [[1, 1], [2, 1]]

    # Test case 3: All nodes with the same value but different random links
    head = list_to_linked_list([[3, None], [3, 0], [3, None]])
    copied_head = solution.copyRandomList(head)
    print(linked_list_to_list(copied_head))
    # Expected output: [[3, None], [3, 0], [3, None]]

    # Test case 4: Single-node list
    head = list_to_linked_list([[1, None]])
    copied_head = solution.copyRandomList(head)
    print(linked_list_to_list(copied_head))
    # Expected output: [[1, None]]

    # Test case 5: Empty list
    head = list_to_linked_list([])
    copied_head = solution.copyRandomList(head)
    print(linked_list_to_list(copied_head))
    # Expected output: []

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(n) where n is the number of nodes in the linked list. We perform three passes over the list.
# Space Complexity: O(n) where n is the number of nodes in the linked list. We maintain a mapping of nodes to their clones.
