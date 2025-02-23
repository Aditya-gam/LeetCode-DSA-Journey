import heapq


class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        # Pair nums1 and nums2, and sort by nums2 in descending order
        paired = sorted(zip(nums1, nums2), key=lambda x: -x[1])

        min_heap = []
        current_sum = 0
        max_score = 0

        for num1, num2 in paired:
            heapq.heappush(min_heap, num1)
            current_sum += num1

            # If the heap exceeds size k, remove the smallest element
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)

            # If the heap has exactly k elements, calculate the score
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * num2)

        return max_score


# Example test cases
solution = Solution()

# Test case 1
nums1 = [1, 3, 3, 2]
nums2 = [2, 1, 3, 4]
k = 3
assert solution.maxScore(nums1, nums2, k) == 12  # Expected: 12

# Test case 2
nums1 = [4, 2, 3, 1, 1]
nums2 = [7, 5, 10, 9, 6]
k = 1
assert solution.maxScore(nums1, nums2, k) == 30  # Expected: 30

# Test case 3
nums1 = [1, 2, 3]
nums2 = [3, 2, 1]
k = 2
assert solution.maxScore(nums1, nums2, k) == 8  # Expected: 8

# Test case 4
nums1 = [5, 5, 5]
nums2 = [5, 5, 5]
k = 3
assert solution.maxScore(nums1, nums2, k) == 75  # Expected: 75

# Complexity Analysis
# Time Complexity: O(nlogn), since k≤n.
# Sorting the paired array: O(nlogn)
# Maintaining the heap: O(nlogk)

# Space Complexity: O(n).
# Heap size: O(k)
# Storage for paired array: O(n)
