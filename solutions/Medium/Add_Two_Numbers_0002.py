from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two non-negative integers represented as linked lists (in reverse order)
        and returns the sum as a linked list.

        Parameters:
            l1 (Optional[ListNode]): The first linked list.
            l2 (Optional[ListNode]): The second linked list.

        Returns:
            Optional[ListNode]: The linked list representing the sum of the two numbers.
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next


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

    # Test case 1: Basic addition
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))
    # Expected output: [7, 0, 8]  -> 342 + 465 = 807

    # Test case 2: Adding two zeros
    l1 = list_to_linked_list([0])
    l2 = list_to_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))
    # Expected output: [0]

    # Test case 3: Unequal length numbers
    l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))
    # Expected output: [8, 9, 9, 9, 0, 0, 0, 1]  -> 9999999 + 9999 = 10009998

    # Test case 4: Carry at the last digit
    l1 = list_to_linked_list([1])
    l2 = list_to_linked_list([9])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))
    # Expected output: [0, 1] -> 1 + 9 = 10

    # Test case 5: Multiple carries
    l1 = list_to_linked_list([5, 6, 4])
    l2 = list_to_linked_list([5, 4, 6])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))
    # Expected output: [0, 1, 1, 1] -> 465 + 654 = 1110

    # Test case 6: Adding zero to a number
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))
    # Expected output: [2, 4, 3] -> 342 + 0 = 342

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(max(m, n)), where m and n are the lengths of the input linked lists l1 and l2, respectively. We iterate through both linked lists once.

# Space Complexity: O(max(m, n)), where m and n are the lengths of the input linked lists l1 and l2, respectively. The length of the new linked list will be at most max(m, n) + 1.
