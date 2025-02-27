from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        Function: numOfSubarrays
        Description: Returns the count of subarrays with an odd sum.

        Parameters:
        - arr (List[int]): List of positive integers.

        Returns:
        - int: Count of subarrays with odd sum modulo (10^9 + 7).
        """

        MODULO = 10**9 + 7
        odd_count = 0  # Tracks prefix sums with odd value
        # Tracks prefix sums with even value (initially 1 to count empty prefix)
        even_count = 1
        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num  # Update prefix sum

            if prefix_sum % 2 == 0:
                result += odd_count  # Adding an even prefix sum to an odd one creates an odd sum
                even_count += 1  # Increment even count
            else:
                result += even_count  # Adding an odd prefix sum to an even one creates an odd sum
                odd_count += 1  # Increment odd count

            result %= MODULO  # Modulo operation to prevent overflow

        return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic example with all odd numbers
    print("Test Case 1: All odd numbers")
    arr1 = [1, 3, 5]
    print("Expected Output: 4 | Actual Output:", solution.numOfSubarrays(arr1))

    # Test case 2: All even numbers
    print("Test Case 2: All even numbers")
    arr2 = [2, 4, 6]
    print("Expected Output: 0 | Actual Output:", solution.numOfSubarrays(arr2))

    # Test case 3: Mixed odd and even numbers
    print("Test Case 3: Mixed odd and even numbers")
    arr3 = [1, 2, 3, 4, 5, 6, 7]
    print("Expected Output: 16 | Actual Output:", solution.numOfSubarrays(arr3))

    # Test case 4: Single element odd
    print("Test Case 4: Single odd number")
    arr4 = [7]
    print("Expected Output: 1 | Actual Output:", solution.numOfSubarrays(arr4))

    # Test case 5: Single element even
    print("Test Case 5: Single even number")
    arr5 = [8]
    print("Expected Output: 0 | Actual Output:", solution.numOfSubarrays(arr5))

    # Test case 6: Large alternating sequence
    print("Test Case 6: Large alternating sequence")
    arr6 = [1, 2] * 50000  # Alternating 1 and 2, size = 100000
    print("Expected Output: Computed Output:", solution.numOfSubarrays(arr6))

"""
Time Complexity:
- O(N) → We iterate through `arr` once while maintaining count of even and odd prefix sums.
- Space Complexity:
  - O(1) → Only a few integer variables are used (constant space).
"""
