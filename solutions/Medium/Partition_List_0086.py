from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Function: partition
        Description: Partitions a linked list so that all nodes less than x come before nodes 
                     greater than or equal to x while maintaining the original order.

        Parameters:
        - head (Optional[ListNode]): The head of the linked list.
        - x (int): The partition value.

        Returns:
        - Optional[ListNode]: The head of the modified linked list.
        """
        # Two dummy nodes to separate smaller and greater/equal lists
        small_dummy = ListNode(0)
        large_dummy = ListNode(0)

        small = small_dummy  # Pointer for the smaller list
        large = large_dummy  # Pointer for the larger/equal list

        # Traverse the original list and partition nodes into two lists
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        # Connect the two partitions and end the larger list
        small.next = large_dummy.next
        large.next = None  # Avoid cyclic reference

        return small_dummy.next


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

    # Test case 1: Basic partition
    head = list_to_linked_list([1, 4, 3, 2, 5, 2])
    result = solution.partition(head, 3)
    print(linked_list_to_list(result))
    # Expected output: [1, 2, 2, 4, 3, 5]

    # Test case 2: Already sorted with respect to x
    head = list_to_linked_list([2, 1])
    result = solution.partition(head, 2)
    print(linked_list_to_list(result))
    # Expected output: [1, 2]

    # Test case 3: All nodes less than x
    head = list_to_linked_list([1, 2, 0])
    result = solution.partition(head, 3)
    print(linked_list_to_list(result))
    # Expected output: [1, 2, 0]

    # Test case 4: All nodes greater than or equal to x
    head = list_to_linked_list([5, 6, 7])
    result = solution.partition(head, 4)
    print(linked_list_to_list(result))
    # Expected output: [5, 6, 7]

    # Test case 5: Single node list
    head = list_to_linked_list([1])
    result = solution.partition(head, 1)
    print(linked_list_to_list(result))
    # Expected output: [1]

    # Test case 6: Empty list
    head = list_to_linked_list([])
    result = solution.partition(head, 3)
    print(linked_list_to_list(result))
    # Expected output: []

    # Test case 7: All nodes equal to x
    head = list_to_linked_list([3, 3, 3])
    result = solution.partition(head, 3)
    print(linked_list_to_list(result))
    # Expected output: [3, 3, 3]

    # Test case 8: Multiple nodes less than x
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.partition(head, 6)
    print(linked_list_to_list(result))
    # Expected output: [1, 2, 3, 4, 5]

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the linked list. We process each node once.
# Space Complexity: O(1), since we only use a constant amount of extra space.
