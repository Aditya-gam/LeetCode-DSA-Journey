# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseListIterative(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # Save the next node
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev to the current node
            curr = next_node       # Move to the next node

        return prev  # New head of the reversed list

    def reverseListRecursive(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        # Reverse the rest of the list
        new_head = self.reverseList(head.next)

        # Adjust the pointers
        head.next.next = head
        head.next = None

        return new_head


# Example test cases
solution = Solution()

# Test case 1: Regular case
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = solution.reverseListIterative(head)  # Expected: [5,4,3,2,1]

# Test case 2: Two nodes
head = ListNode(1, ListNode(2))
reversed_head = solution.reverseListIterative(head)  # Expected: [2,1]

# Test case 3: Empty list
head = None
reversed_head = solution.reverseListRecursive(head)  # Expected: []

# Test case 4: Single node
head = ListNode(1)
reversed_head = solution.reverseListRecursive(head)  # Expected: [1]

# Complexity Analysis:
# Time complexity: O(n) for both iterative and recursive solutions.
# We visit each node once.

# Space complexity: O(1) for the iterative solution and O(n) for the recursive solution.
# The iterative solution uses a constant amount of extra space.
# The recursive solution uses space on the call stack proportional to the number of nodes in the list.
