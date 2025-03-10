from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Function: hasCycle
        Description: Determines whether a linked list has a cycle using Floyd’s Tortoise and Hare algorithm.

        Parameters:
        - head (Optional[ListNode]): The head node of the linked list.

        Returns:
        - bool: True if the linked list contains a cycle, otherwise False.
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next           # Move slow pointer one step
            fast = fast.next.next      # Move fast pointer two steps

            if slow == fast:           # If they meet, a cycle exists
                return True

        return False  # No cycle found


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Cycle exists (pos = 1)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle

    print(solution.hasCycle(node1))
    # Expected output: True

    # Test case 2: Cycle exists (pos = 0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1  # Creates a cycle

    print(solution.hasCycle(node1))
    # Expected output: True

    # Test case 3: No cycle (pos = -1)
    node1 = ListNode(1)

    print(solution.hasCycle(node1))
    # Expected output: False

    # Test case 4: Empty list (head = None)
    print(solution.hasCycle(None))
    # Expected output: False

    # Test case 5: List with multiple nodes but no cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    print(solution.hasCycle(node1))
    # Expected output: False

    # Test case 6: List with multiple nodes and a cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Creates a cycle

    print(solution.hasCycle(node1))
    # Expected output: True

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(n) where n is the number of nodes in the linked list. In the worst case, we visit each node exactly once.
# Space Complexity: O(1) since we only use two pointers (slow and fast) to detect the cycle. The space complexity is constant.
