import heapq
import random


class Solution(object):
    def findKthLargestHeap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Use a min-heap of size k
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]  # The root of the heap is the kth largest element

    def findKthLargestQuickselect(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot_value = nums[pivot_index]
            # Move pivot to the end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left

            # Move all elements larger than the pivot to the left
            for i in range(left, right):
                if nums[i] > pivot_value:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1

            # Move pivot to its final place
            nums[store_index], nums[right] = nums[right], nums[store_index]
            return store_index

        def quickselect(left, right, k_smallest):
            # Base case: the list contains only one element
            if left == right:
                return nums[left]

            # Choose a random pivot
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            # The pivot is in its final sorted position
            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return quickselect(left, pivot_index - 1, k_smallest)
            else:
                return quickselect(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest
        return quickselect(0, len(nums) - 1, len(nums) - k)


# Example test cases
solution = Solution()

# Test case 1
nums = [3, 2, 1, 5, 6, 4]
k = 2
assert solution.findKthLargestHeap(nums, k) == 5  # Expected: 5

# Test case 2
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
assert solution.findKthLargestQuickselect(nums, k) == 4  # Expected: 4

# Test case 3
nums = [1]
k = 1
assert solution.findKthLargestHeap(nums, k) == 1  # Expected: 1

# Test case 4
nums = [7, 6, 5, 4, 3, 2, 1]
k = 3
assert solution.findKthLargestQuickselect(nums, k) == 5  # Expected: 5

print("All test cases passed successfully.")

# Complexity analysis
# Time Complexity: O(N * log(k)), where N is the number of elements in the input list nums.
#                   We are iterating over the list and pushing elements into the heap of size k.
#                   The time complexity of heap push is O(log(k)).

# Space Complexity: O(k), The space complexity is O(k) because we are using a heap of size k.
