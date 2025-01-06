class Solution(object):
    def check(self, nums):
        """
        Check if an array is sorted and rotated.

        :param nums: List[int] - Input array
        :return: bool - True if sorted and rotated, False otherwise
        """
        count = 0
        n = len(nums)

        # Count the number of drops
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Handle wraparound using modulo
                count += 1

        # If there's at most one drop, it's valid
        return count <= 1


# Example test cases
sol = Solution()
print(sol.check([3, 4, 5, 1, 2]))  # Output: True
print(sol.check([2, 1, 3, 4]))     # Output: False
print(sol.check([1, 2, 3]))        # Output: True
