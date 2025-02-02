class Solution(object):
    def singleNumber(self, nums):
        """
        Finds the single number in the array using XOR.

        Parameters:
        nums (List[int]): The input array where every element except one appears twice.

        Returns:
        int: The single number that appears only once.
        """

        result = 0
        for num in nums:
            result ^= num  # XOR accumulates to isolate the unique number

        return result


# Example test cases
def test_singleNumber():
    sol = Solution()

    # Test Case 1
    nums = [2, 2, 1]
    # Explanation: 2 ^ 2 ^ 1 = (2 ^ 2) ^ 1 = 0 ^ 1 = 1
    assert sol.singleNumber(nums) == 1

    # Test Case 2
    nums = [4, 1, 2, 1, 2]
    # 4 ^ 1 ^ 2 ^ 1 ^ 2 = 4 ^ (1 ^ 1) ^ (2 ^ 2) = 4 ^ 0 ^ 0 = 4
    assert sol.singleNumber(nums) == 4

    # Test Case 3
    nums = [1]
    # Only one element, so it is the single number
    assert sol.singleNumber(nums) == 1

    # Test Case 4
    # Negative and positive integers
    nums = [-1, -1, 2, 2, 3]
    # -1 ^ -1 = 0, 2 ^ 2 = 0 => leftover is 3
    assert sol.singleNumber(nums) == 3

    # Test Case 5
    # Larger array example
    nums = [0, 1, 0, 1, 99]
    # 0 ^ 1 ^ 0 ^ 1 = 0, leftover is 99
    assert sol.singleNumber(nums) == 99

    print("All test cases passed!")


test_singleNumber()


# Complexity Analysis
# Time Complexity: O(n)
# We iterate through the array once.

# Space Complexity: O(1)
# Only a single variable result is used for computation.
