class Solution(object):
    def isArraySpecial(self, nums):
        """
        Determines if the array nums is 'special', meaning
        every pair of adjacent elements have different parity.

        Parameters:
        nums (List[int]): The input array of integers.

        Returns:
        bool: True if the array is special, otherwise False.
        """

        # If the array has only one element, it's trivially special.
        if len(nums) == 1:
            return True

        # Check each pair of adjacent elements
        for i in range(len(nums) - 1):
            # If they have the same parity, the array is not special
            if (nums[i] % 2) == (nums[i + 1] % 2):
                return False

        # If we never find a pair with the same parity, it's special
        return True


# Example test cases
# Test case 1: Single element array
nums = [1]
# Expected output: True (no adjacent pairs to compare, so it's trivially special)
assert Solution().isArraySpecial(nums) == True

# Test case 2: Adjacent even-odd pairs
nums = [2, 1, 4]
# Pairs: (2,1) -> different parity, (1,4) -> different parity
# Expected output: True
assert Solution().isArraySpecial(nums) == True

# Test case 3: Contains same-parity adjacent elements
nums = [4, 3, 1, 6]
# Pairs: (4,3) different parity, (3,1) same parity (both odd), so False
assert Solution().isArraySpecial(nums) == False

# Additional Test: All evens
nums = [2, 4, 6]
# Adjacent pairs all have the same parity (even, even) -> False
assert Solution().isArraySpecial(nums) == False

# Additional Test: All odds
nums = [3, 5, 7]
# Adjacent pairs all have the same parity (odd, odd) -> False
assert Solution().isArraySpecial(nums) == False

print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n) - We iterate through the array once, where n is the length of the array.
# Space complexity: O(1) - We use a constant amount of extra space, regardless of the input size.
