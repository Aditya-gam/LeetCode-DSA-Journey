class Solution(object):
    def minimumAverage(self, nums):
        """
        Calculate the minimum average of the smallest and largest elements.

        :param nums: List[int] - Input array
        :return: float - Minimum average
        """
        # Sort the input array
        nums.sort()

        # Initialize two pointers for the smallest and largest elements
        left = 0
        right = len(nums) - 1

        # List to store averages
        averages = []

        # Calculate averages for n / 2 iterations
        while left < right:
            avg = (nums[left] + nums[right]) / 2.0
            averages.append(avg)
            left += 1
            right -= 1

        # Return the minimum average
        return min(averages)


# Example test cases
sol = Solution()
print(sol.minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]))  # Output: 5.5
print(sol.minimumAverage([1, 9, 8, 3, 10, 5]))         # Output: 5.5
print(sol.minimumAverage([1, 2, 3, 7, 8, 9]))          # Output: 5.0
