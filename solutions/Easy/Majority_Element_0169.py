class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        This function returns the majority element in the array,
        using the Boyer-Moore Voting Algorithm in O(n) time and O(1) space.
        """
        candidate = None
        count = 0

        # Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [3, 2, 3]
    assert solution.majorityElement(nums1) == 3  # Expected: 3

    # Test case 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    assert solution.majorityElement(nums2) == 2  # Expected: 2

    print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(n), where n is the length of nums.
# Space Complexity: O(1).
