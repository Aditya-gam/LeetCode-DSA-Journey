from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Function: combine
        Description: Returns all possible combinations of k numbers chosen from [1, n].

        Parameters:
        - n (int): The upper range of numbers.
        - k (int): The number of elements in each combination.

        Returns:
        - List[List[int]]: All possible combinations of k elements.
        """

        res = []

        def backtrack(start, path):
            # Base case: If the combination is of length k, store it
            if len(path) == k:
                res.append(path[:])  # Make a copy before adding
                return

            # Iterate from the current start position to n
            for i in range(start, n + 1):
                path.append(i)  # Choose
                backtrack(i + 1, path)  # Explore
                path.pop()  # Un-choose (backtrack)

        backtrack(1, [])

        return res


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard case with small n and k
    print("Test Case 1: n = 4, k = 2")
    print(
        "Expected Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]] | Actual Output:", solution.combine(4, 2))

    # Test case 2: Minimum input case
    print("Test Case 2: n = 1, k = 1")
    print("Expected Output: [[1]] | Actual Output:", solution.combine(1, 1))

    # Test case 3: Large n with k close to n
    print("Test Case 3: n = 5, k = 4")
    print("Expected Output: Computed Output:", solution.combine(5, 4))

    # Test case 4: k = 1 (should return all single-element lists)
    print("Test Case 4: n = 5, k = 1")
    print(
        "Expected Output: [[1], [2], [3], [4], [5]] | Actual Output:", solution.combine(5, 1))

    # Test case 5: n = k (should return one combination containing all numbers)
    print("Test Case 5: n = 4, k = 4")
    print("Expected Output: [[1,2,3,4]] | Actual Output:",
          solution.combine(4, 4))

    # Test case 6: Large n, small k
    print("Test Case 6: n = 10, k = 3")
    print("Expected Output: Computed Output:", solution.combine(10, 3))

"""
Time Complexity:
- O(C(n, k)) → The number of combinations is C(n, k) = n! / (k!(n-k)!).
- Space Complexity:
  - O(k) → Recursion stack depth is at most k.
"""
