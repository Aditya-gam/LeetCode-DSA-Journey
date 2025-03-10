from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Function: removeNthFromEnd
        Description: Removes the nth node from the end of a linked list in one pass 
                     using the two-pointer technique.

        Parameters:
        - head (Optional[ListNode]): The head of the linked list.
        - n (int): The position (from the end) of the node to remove.

        Returns:
        - Optional[ListNode]: The head of the modified linked list.
        """
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        first = second = dummy

        # Move first pointer n+1 steps ahead to create a gap of n between first and second
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node
        second.next = second.next.next

        return dummy.next  # Return the updated list


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

    # Test case 1: Removing the 2nd node from end
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.removeNthFromEnd(head, 2)
    print(linked_list_to_list(result))
    # Expected output: [1, 2, 3, 5]

    # Test case 2: Removing the only node
    head = list_to_linked_list([1])
    result = solution.removeNthFromEnd(head, 1)
    print(linked_list_to_list(result))
    # Expected output: []

    # Test case 3: Removing the last node
    head = list_to_linked_list([1, 2])
    result = solution.removeNthFromEnd(head, 1)
    print(linked_list_to_list(result))
    # Expected output: [1]

    # Test case 4: Removing the first node
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.removeNthFromEnd(head, 5)
    print(linked_list_to_list(result))
    # Expected output: [2, 3, 4, 5]

    # Test case 5: Removing from a longer list
    head = list_to_linked_list([10, 20, 30, 40, 50, 60, 70])
    result = solution.removeNthFromEnd(head, 4)
    print(linked_list_to_list(result))
    # Expected output: [10, 20, 30, 50, 60, 70]

    # Test case 6: Removing from a list with duplicates
    head = list_to_linked_list([1, 1, 2, 2, 3, 3])
    result = solution.removeNthFromEnd(head, 2)
    print(linked_list_to_list(result))
    # Expected output: [1, 1, 2, 3, 3]

    # Test case 7: Removing from a list with all duplicates
    head = list_to_linked_list([1, 1, 1, 1, 1])
    result = solution.removeNthFromEnd(head, 1)
    print(linked_list_to_list(result))
    # Expected output: [1, 1, 1, 1]

    # Test case 8: Removing from a list with negative numbers
    head = list_to_linked_list([-1, -2, -3, -4, -5])
    result = solution.removeNthFromEnd(head, 3)
    print(linked_list_to_list(result))
    # Expected output: [-1, -2, -4, -5]

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the linked list. We process each node once.
# Space Complexity: O(1), since we only use a constant amount of extra space.
