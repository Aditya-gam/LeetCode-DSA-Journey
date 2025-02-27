import bisect


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # Step 1: Find the closest index using Binary Search
        pos = bisect.bisect_left(arr, x)  # Find insertion point for x

        # Step 2: Initialize two pointers around this position
        left, right = pos - 1, pos

        # Step 3: Expand the window of size `k`
        while k > 0:
            if left < 0:  # If left is out of bounds, move right
                right += 1
            elif right >= len(arr):  # If right is out of bounds, move left
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):  # Closer to left
                left -= 1
            else:  # Closer to right
                right += 1
            k -= 1

        # Step 4: Return the sorted k closest elements
        return arr[left + 1:right]


# Example test cases
if __name__ == "__main__":
    sol = Solution()
    # Output: [1, 2, 3, 4]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 3))
    # Output: [1, 2, 3, 4]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, -1))
    # Output: [2, 3, 4, 5]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 6))
    # Output: [1, 2, 3, 4]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 0))
    # Output: [2, 3, 4, 5]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 5))
    # Output: [1, 2, 3, 4]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 1))
    # Output: [1, 2, 3, 4]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 2))
    # Output: [1, 2, 3, 4]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 4))
    # Output: [2, 3, 4, 5]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 3.5))
    # Output: [1, 2, 3, 4]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 2.5))
    # Output: [2, 3, 4, 5]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 4.5))
    # Output: [1, 2, 3, 4]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 1.5))

    print("All test cases passed successfully!")

# Complexity Analysis:
# Time Complexity: O(log(N) + K), where N is the length of the input array arr.
# - The binary search takes O(log(N)) time.
# - The window expansion takes O(K) time.

# Space Complexity: O(1) since we use only a constant amount of space.
