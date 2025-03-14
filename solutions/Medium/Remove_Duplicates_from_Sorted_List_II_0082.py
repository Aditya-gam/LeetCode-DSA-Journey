from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Function: deleteDuplicates
        Description: Removes all nodes that have duplicate numbers, leaving only distinct numbers.

        Parameters:
        - head (Optional[ListNode]): The head of the sorted linked list.

        Returns:
        - Optional[ListNode]: The head of the modified linked list with only distinct numbers.
        """
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        prev = dummy  # Pointer to track non-duplicate nodes

        while head:
            if head.next and head.val == head.next.val:
                # Skip all nodes with this duplicate value
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next  # Remove all duplicates
            else:
                prev = prev.next  # Move prev pointer forward if no duplicate
            head = head.next  # Move to next node

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

    # Test case 1: Duplicates removed
    head = list_to_linked_list([1, 2, 3, 3, 4, 4, 5])
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
    # Expected output: [1, 2, 5]

    # Test case 2: Removing all duplicates
    head = list_to_linked_list([1, 1, 1, 2, 3])
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
    # Expected output: [2, 3]

    # Test case 3: List with no duplicates
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
    # Expected output: [1, 2, 3, 4, 5]

    # Test case 4: All nodes are duplicates
    head = list_to_linked_list([1, 1, 1, 1])
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
    # Expected output: []

    # Test case 5: Empty list
    head = list_to_linked_list([])
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
    # Expected output: []

    # Test case 6: Single node (no duplicates)
    head = list_to_linked_list([1])
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
    # Expected output: [1]

    # Test case 7: Single node (duplicate)
    head = list_to_linked_list([1, 1])
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
    # Expected output: []

    print("All test cases passed!")

# Complexity Analysis
# Time complexity: O(N), where N is the number of nodes in the linked list. We process each node once.
# Space complexity: O(1), since we only use a constant amount of space.
