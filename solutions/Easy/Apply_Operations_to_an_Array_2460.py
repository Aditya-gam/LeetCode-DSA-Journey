from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        Function: applyOperations
        Description: Modifies the array based on given operations and shifts all zeros to the end.

        Parameters:
        - nums (List[int]): List of non-negative integers.

        Returns:
        - List[int]: The modified list after applying the operations.
        """

        n = len(nums)

        # Step 1: Apply the operations as per the given conditions
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Step 2: Move all zeros to the end while maintaining order
        result = [num for num in nums if num != 0] + [0] * nums.count(0)

        return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: General case with consecutive identical numbers
    nums = [1, 2, 2, 1, 1, 0]
    # Expected Output: [1, 4, 2, 0, 0, 0]
    print("Test Case 1:", solution.applyOperations(nums))

    # Test Case 2: Already processed case, no changes needed
    nums = [0, 1]
    # Expected Output: [1, 0]
    print("Test Case 2:", solution.applyOperations(nums))

    # Test Case 3: Large input with multiple consecutive pairs
    nums = [2, 2, 4, 4, 8, 8]
    # Expected Output: [4, 8, 16, 0, 0, 0]
    print("Test Case 3:", solution.applyOperations(nums))

    # Test Case 4: No identical consecutive numbers
    nums = [1, 3, 5, 7, 9]
    # Expected Output: [1, 3, 5, 7, 9]
    print("Test Case 4:", solution.applyOperations(nums))

    # Test Case 5: All zeros
    nums = [0, 0, 0, 0, 0]
    # Expected Output: [0, 0, 0, 0, 0]
    print("Test Case 5:", solution.applyOperations(nums))

    # Test Case 6: Alternating zeros and numbers
    nums = [1, 0, 2, 0, 3, 0]
    # Expected Output: [1, 2, 3, 0, 0, 0]
    print("Test Case 6:", solution.applyOperations(nums))

"""
Time Complexity:
- O(n) for iterating and applying operations.
- O(n) for moving zeros to the end.
- Total: O(n)

Space Complexity:
- O(n) for storing the result.
- Total: O(n)
"""
