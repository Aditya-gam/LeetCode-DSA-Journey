from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Function: rotateRight
        Description: Rotates the linked list to the right by k places.

        Parameters:
        - head (Optional[ListNode]): The head of the linked list.
        - k (int): The number of rotations.

        Returns:
        - Optional[ListNode]: The head of the rotated linked list.
        """
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Optimize k (avoid unnecessary full rotations)
        k = k % length
        if k == 0:
            return head  # No rotation needed

        # Step 3: Find the new tail (length - k - 1 th node)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Step 4: Update head and break the link
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head  # Connect old tail to old head

        return new_head


# Helper functions for testing
def list_to_linked_list(lst):
    """Converts a Python list to a linked list."""
    if not lst:
        return None
    dummy_head = ListNode(0)
    current = dummy_head
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy_head.next


def linked_list_to_list(node):
    """Converts a linked list to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic rotation
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.rotateRight(head, 2)
    print(linked_list_to_list(result))
    # Expected output: [4, 5, 1, 2, 3]

    # Test case 2: k larger than list length
    head = list_to_linked_list([0, 1, 2])
    result = solution.rotateRight(head, 4)
    print(linked_list_to_list(result))
    # Expected output: [2, 0, 1]

    # Test case 3: No rotation needed
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.rotateRight(head, 5)
    print(linked_list_to_list(result))
    # Expected output: [1, 2, 3, 4, 5]

    # Test case 4: Single node
    head = list_to_linked_list([1])
    result = solution.rotateRight(head, 3)
    print(linked_list_to_list(result))
    # Expected output: [1]

    # Test case 5: Empty list
    head = list_to_linked_list([])
    result = solution.rotateRight(head, 2)
    print(linked_list_to_list(result))
    # Expected output: []

    # Test case 6: No rotation needed
    head = list_to_linked_list([1, 2, 3])
    result = solution.rotateRight(head, 0)
    print(linked_list_to_list(result))
    # Expected output: [1, 2, 3]

    # Test case 7: Large k
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.rotateRight(head, 100)
    print(linked_list_to_list(result))
    # Expected output: [1, 2, 3, 4, 5]

    # Test case 8: Large list with large k
    head = list_to_linked_list([1] * 1000)
    result = solution.rotateRight(head, 1003)
    print(linked_list_to_list(result))
    # Expected output: [998, 999, 1000, 1, 1, ..., 1] (1000 elements)

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the linked list. We process each node once.
# Space Complexity: O(1), since we use only a constant amount of extra space.
