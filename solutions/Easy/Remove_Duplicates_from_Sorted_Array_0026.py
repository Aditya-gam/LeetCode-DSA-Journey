class Solution(object):
    def removeDuplicates(self, nums):
        """
        Remove duplicates in a sorted array in-place.

        :param nums: List[int] - Input sorted array
        :return: int - Count of unique elements
        """
        if not nums:
            return 0

        write_ptr = 1  # Initialize the write pointer

        for read_ptr in range(1, len(nums)):
            if nums[read_ptr] != nums[read_ptr - 1]:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1

        return write_ptr


# Example test cases
sol = Solution()
nums1 = [1, 1, 2]
print(sol.removeDuplicates(nums1))  # Output: 2, [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(sol.removeDuplicates(nums2))  # Output: 5, [0, 1, 2, 3, 4]
