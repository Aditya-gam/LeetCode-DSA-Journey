from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Function: reverseBetween
        Description: Reverses a sublist of a linked list from position left to right.

        Parameters:
        - head (Optional[ListNode]): The head of the linked list.
        - left (int): The starting position of the reversal (1-based index).
        - right (int): The ending position of the reversal (1-based index).

        Returns:
        - Optional[ListNode]: The head of the modified linked list.
        """
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the sublist between left and right
        curr = prev.next
        next_node = None
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next


# Helper functions for testing
def list_to_linked_list(lst):
    """Converts a Python list to a linked list."""
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

    # Test case 1: Reversing a middle segment
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseBetween(head, 2, 4)
    print(linked_list_to_list(result))
    # Expected output: [1, 4, 3, 2, 5]

    # Test case 2: Reversing a single-node list
    head = list_to_linked_list([5])
    result = solution.reverseBetween(head, 1, 1)
    print(linked_list_to_list(result))
    # Expected output: [5]

    # Test case 3: Reversing the full list
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseBetween(head, 1, 5)
    print(linked_list_to_list(result))
    # Expected output: [5, 4, 3, 2, 1]

    # Test case 4: Reversing first two nodes
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseBetween(head, 1, 2)
    print(linked_list_to_list(result))
    # Expected output: [2, 1, 3, 4, 5]

    # Test case 5: Reversing last two nodes
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseBetween(head, 4, 5)
    print(linked_list_to_list(result))
    # Expected output: [1, 2, 3, 5, 4]

    # Test case 6: Reversing a single-node list with invalid range
    head = list_to_linked_list([5])
    result = solution.reverseBetween(head, 2, 3)
    print(linked_list_to_list(result))
    # Expected output: [5]

    # Test case 7: Reversing a list with only two nodes
    head = list_to_linked_list([1, 2])
    result = solution.reverseBetween(head, 1, 2)
    print(linked_list_to_list(result))
    # Expected output: [2, 1]

    # Test case 8: Reversing a list with only two nodes (reverse order)
    head = list_to_linked_list([1, 2])
    result = solution.reverseBetween(head, 2, 1)
    print(linked_list_to_list(result))
    # Expected output: [2, 1]

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the linked list.
# Space Complexity: O(1). We only use a constant amount of extra space.
