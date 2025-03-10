class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Returns an array 'answer' where each answer[i] is the product of
        all elements of 'nums' except 'nums[i]', in O(n) time and without
        using division.
        """
        n = len(nums)
        answer = [0] * n

        # Step 1: Construct prefix product
        answer[0] = 1
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Step 2: Multiply with suffix product (traverse from right to left)
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix *= nums[i]

        return answer


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 4]
    # Each answer[i] = product of all except nums[i]
    # Expected = [24, 12, 8, 6]
    assert solution.productExceptSelf(nums1) == [24, 12, 8, 6]

    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    # Explanation:
    #   If there's a zero in the array, all other positions except the zero's position
    #   become 0 in the product, except the position where zero is will contain the product
    #   of the rest if there's only one zero. Here, there's exactly one zero at index=2.
    #   So answer = [0, 0, 9, 0, 0]
    assert solution.productExceptSelf(nums2) == [0, 0, 9, 0, 0]

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate through the nums list twice
# Space complexity: O(1) - We use a constant amount of extra space
