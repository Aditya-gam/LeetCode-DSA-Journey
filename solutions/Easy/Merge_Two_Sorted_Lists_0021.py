from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Function: mergeTwoLists
        Description: Merges two sorted linked lists into a single sorted linked list.

        Parameters:
        - list1 (Optional[ListNode]): The first sorted linked list.
        - list2 (Optional[ListNode]): The second sorted linked list.

        Returns:
        - Optional[ListNode]: The head of the merged sorted linked list.
        """

        dummy_head = ListNode(0)  # Dummy node to build the result list
        current = dummy_head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If any elements remain in either list, append them
        current.next = list1 if list1 else list2

        return dummy_head.next  # Return the head of the merged list


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

    # Test case 1: Both lists have elements
    list1 = list_to_linked_list([1, 2, 4])
    list2 = list_to_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))
    # Expected output: [1, 1, 2, 3, 4, 4]

    # Test case 2: Both lists are empty
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))
    # Expected output: []

    # Test case 3: One list is empty
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))
    # Expected output: [0]

    # Test case 4: Lists with different lengths
    list1 = list_to_linked_list([2, 5, 7])
    list2 = list_to_linked_list([1, 3, 4, 6, 8])
    result = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))
    # Expected output: [1, 2, 3, 4, 5, 6, 7, 8]

    # Test case 5: Lists with duplicate elements
    list1 = list_to_linked_list([1, 3, 3])
    list2 = list_to_linked_list([1, 2, 3])
    result = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))
    # Expected output: [1, 1, 2, 3, 3, 3]

    # Test case 6: Lists with negative elements
    list1 = list_to_linked_list([-2, 0, 1])
    list2 = list_to_linked_list([-3, -1, 2])
    result = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))
    # Expected output: [-3, -2, -1, 0, 1, 2]

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(n + m) where n and m are the lengths of the input lists list1 and list2 respectively. We iterate through both lists once to merge them.
# Space Complexity: O(1) since we only use a constant amount of extra space. The merged list is created in-place without using any additional data structures.
