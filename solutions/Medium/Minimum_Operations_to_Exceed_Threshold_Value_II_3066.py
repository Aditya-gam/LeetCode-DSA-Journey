import heapq


class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Convert nums into a min-heap
        heapq.heapify(nums)
        operations = 0

        while nums[0] < k:
            # Extract the two smallest elements
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            # Create the new element and push it back
            new_element = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_element)

            # Increment operation count
            operations += 1

        return operations


# Example test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minOperations([1, 2, 3, 4, 5], 5) == 1
    assert solution.minOperations([5, 6, 7, 8, 9], 4) == 0
    assert solution.minOperations([1, 10, 100, 1000], 4) == 3
    assert solution.minOperations([1, 2, 3, 4, 5, 6], 10) == 3
    assert solution.minOperations([1, 10, 100, 1000], 4) == 3
    assert solution.minOperations([1, 2, 3, 4, 5], 5) == 1
    assert solution.minOperations([1, 2, 3, 4, 5, 6], 10) == 3
    assert solution.minOperations([1, 10, 100, 1000], 4) == 3
    assert solution.minOperations([1, 2, 3, 4, 5], 5) == 1
    assert solution.minOperations([5, 6, 7, 8, 9], 4) == 0
    assert solution.minOperations([1, 10, 100, 1000], 4) == 3
    assert solution.minOperations([1, 2, 3, 4, 5, 6], 10) == 3
    assert solution.minOperations([1, 10, 100, 1000], 4) == 3
    assert solution.minOperations([1, 2, 3, 4, 5], 5) == 1
    assert solution.minOperations([1, 2, 3, 4, 5, 6], 10) == 3
    assert solution.minOperations([1, 10, 100, 1000], 4) == 3
    assert solution.minOperations([1, 2, 3, 4, 5], 5) == 1
    assert solution.minOperations([5, 6, 7, 8, 9], 4) == 0
    assert solution.minOperations([1, 10, 100, 1000], 4) == 3

    print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(N * log(N)), where N is the length of the nums array.
# Space Complexity: O(N), where N is the length of the nums array.
