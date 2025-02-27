from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        Function: lenLongestFibSubseq
        Description: Finds the length of the longest Fibonacci-like subsequence.

        Parameters:
        - arr (List[int]): A strictly increasing array of positive integers.

        Returns:
        - int: Length of the longest Fibonacci-like subsequence, or 0 if not found.
        """

        index_map = {num: i for i, num in enumerate(arr)}
        dp = {}
        max_length = 0

        # Iterate through all pairs (j, k) to check Fibonacci-like sequences
        for k in range(len(arr)):
            for j in range(k):
                # The previous Fibonacci-like element should be arr[k] - arr[j]
                i = index_map.get(arr[k] - arr[j])

                # Check if a valid Fibonacci sequence exists
                if i is not None and i < j:
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    max_length = max(max_length, dp[(j, k)])

        return max_length if max_length >= 3 else 0


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard Fibonacci-like sequence
    print("Test Case 1: arr = [1,2,3,4,5,6,7,8]")
    print("Expected Output: 5 | Actual Output:",
          solution.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))

    # Test case 2: No Fibonacci-like subsequence
    print("Test Case 2: arr = [1,3,7,11,12,14,18]")
    print("Expected Output: 3 | Actual Output:",
          solution.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))

    # Test case 3: Only two numbers (not a valid sequence)
    print("Test Case 3: arr = [1,2]")
    print("Expected Output: 0 | Actual Output:",
          solution.lenLongestFibSubseq([1, 2]))

    # Test case 4: All elements forming a Fibonacci-like sequence
    print("Test Case 4: arr = [1,2,3,5,8,13,21,34,55]")
    print("Expected Output: 9 | Actual Output:",
          solution.lenLongestFibSubseq([1, 2, 3, 5, 8, 13, 21, 34, 55]))

    # Test case 5: Large numbers with gaps
    print("Test Case 5: arr = [10,22,33,55,88,143,231,374,605,979]")
    print("Expected Output: Computed Output:", solution.lenLongestFibSubseq(
        [10, 22, 33, 55, 88, 143, 231, 374, 605, 979]))

    # Test case 6: Edge case with large numbers but no valid sequence
    print("Test Case 6: arr = [1,100,200,300,400,500,600,700]")
    print("Expected Output: 0 | Actual Output:", solution.lenLongestFibSubseq(
        [1, 100, 200, 300, 400, 500, 600, 700]))

"""
Time Complexity:
- O(N^2) → We check pairs (j, k) and update the longest Fibonacci-like subsequence.

Space Complexity:
- O(N^2) → We store dp states for each (j, k) pair.
"""
