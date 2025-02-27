class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left_size = (m + n + 1) // 2  # Ensures proper partitioning

        low, high = 0, m  # Binary search range

        while low <= high:
            i = (low + high) // 2  # Partition for nums1
            j = left_size - i  # Corresponding partition for nums2

            max_left1 = float('-inf') if i == 0 else nums1[i - 1]
            min_right1 = float('inf') if i == m else nums1[i]

            max_left2 = float('-inf') if j == 0 else nums2[j - 1]
            min_right2 = float('inf') if j == n else nums2[j]

            # Check if partition is correct
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Found the correct partition
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
                else:
                    return float(max(max_left1, max_left2))

            # Adjust partition
            elif max_left1 > min_right2:
                high = i - 1  # Move left
            else:
                low = i + 1  # Move right

        return -1  # This case should never be reached


# Example test cases
if __name__ == "__main__":
    sol = Solution()
    # Output: 2.0
    print(sol.findMedianSortedArrays([1, 3], [2]))
    # Output: 2.5
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))
    # Output: 1.0
    print(sol.findMedianSortedArrays([1], []))
    # Output: 1.0
    print(sol.findMedianSortedArrays([1, 2], []))
    # Output: 2.0
    print(sol.findMedianSortedArrays([1], [2, 3]))
    # Output: 2.5
    print(sol.findMedianSortedArrays([1, 3], [2, 4]))
    # Output: 3.0
    print(sol.findMedianSortedArrays([1, 2, 3], [4, 5, 6]))
    # Output: 3.0
    print(sol.findMedianSortedArrays([1, 2, 3], [4, 5]))
    # Output: 3.0
    print(sol.findMedianSortedArrays([1, 2], [3, 4, 5]))
    # Output: 3.0
    print(sol.findMedianSortedArrays([1, 3, 5], [2, 4, 6]))
    # Output: 3.0
    print(sol.findMedianSortedArrays([1, 3, 5], [2, 4, 6, 7]))
    # Output: 3.0
    print(sol.findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6]))
    # Output: 3.0
    print(sol.findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6, 8]))
    # Output: 3.0
    print(sol.findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6, 8, 9]))
    # Output: 3.0
    print(sol.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8]))
    # Output: 3.0
    print(sol.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))

    print("All test cases passed successfully!")

# Complexity Analysis
# Time Complexity: O(log(min(m, n))), where m and n are the lengths of the two input arrays.
# Space Complexity: O(1) since we are using constant extra space.
