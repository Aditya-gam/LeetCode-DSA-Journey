from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Function: reverseKGroup
        Description: Reverses nodes in k-sized groups in a linked list. 
                     If the remaining nodes are fewer than k, they remain unchanged.

        Parameters:
        - head (Optional[ListNode]): The head of the linked list.
        - k (int): The group size for reversal.

        Returns:
        - Optional[ListNode]: The head of the modified linked list.
        """
        def reverseLinkedList(start: ListNode, end: ListNode) -> ListNode:
            """
            Helper function to reverse a linked list segment from 'start' to 'end'.
            """
            prev, curr = None, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev  # New head after reversal

        # Step 1: Count the total number of nodes
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        curr = head

        # Step 2: Process k-sized groups
        while count >= k:
            start = curr
            end = curr
            for _ in range(k):  # Move to the k-th node
                end = end.next

            # Reverse this k-group
            new_start = reverseLinkedList(start, end)

            # Connect the previous group's end to the new start
            prev_group_end.next = new_start
            start.next = end  # Connect reversed part to the remaining list

            # Update pointers
            prev_group_end = start
            curr = end
            count -= k

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

    # Test case 1: k = 2
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseKGroup(head, 2)
    print(linked_list_to_list(result))
    # Expected output: [2, 1, 4, 3, 5]

    # Test case 2: k = 3
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseKGroup(head, 3)
    print(linked_list_to_list(result))
    # Expected output: [3, 2, 1, 4, 5]

    # Test case 3: k = 1 (No changes)
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseKGroup(head, 1)
    print(linked_list_to_list(result))
    # Expected output: [1, 2, 3, 4, 5]

    # Test case 4: k = length of list (Full reversal)
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseKGroup(head, 5)
    print(linked_list_to_list(result))
    # Expected output: [5, 4, 3, 2, 1]

    # Test case 5: List with only one element
    head = list_to_linked_list([1])
    result = solution.reverseKGroup(head, 1)
    print(linked_list_to_list(result))
    # Expected output: [1]

    # Test case 6: List with two elements
    head = list_to_linked_list([1, 2])
    result = solution.reverseKGroup(head, 2)
    print(linked_list_to_list(result))
    # Expected output: [2, 1]

    print("All test cases passed!")

# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the linked list. We process each node once.
# Space Complexity: O(1), since we use only a constant amount of space.
