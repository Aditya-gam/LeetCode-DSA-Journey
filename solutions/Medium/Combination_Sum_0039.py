from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Function: combinationSum
        Description: Finds all unique combinations of candidates where chosen numbers sum to target.

        Parameters:
        - candidates (List[int]): A list of distinct integers.
        - target (int): The sum target value.

        Returns:
        - List[List[int]]: A list of all unique combinations that sum to target.
        """
        result = []

        def backtrack(start, combination, current_sum):
            # Base case: if current sum reaches the target, add to result
            if current_sum == target:
                result.append(list(combination))
                return
            if current_sum > target:
                return  # Stop the recursion if sum exceeds target

            for i in range(start, len(candidates)):
                # Include candidates[i] and recursively explore
                combination.append(candidates[i])
                # Allow same element reuse
                backtrack(i, combination, current_sum + candidates[i])
                combination.pop()  # Backtrack

        backtrack(0, [], 0)

        return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Simple case with multiple valid combinations
    print("Test Case 1: candidates = [2,3,6,7], target = 7")
    print("Expected Output: [[2,2,3],[7]] | Actual Output:",
          solution.combinationSum([2, 3, 6, 7], 7))

    # Test case 2: Multiple combinations with a different set
    print("Test Case 2: candidates = [2,3,5], target = 8")
    print("Expected Output: [[2,2,2,2],[2,3,3],[3,5]] | Actual Output:",
          solution.combinationSum([2, 3, 5], 8))

    # Test case 3: No valid combination
    print("Test Case 3: candidates = [2], target = 1")
    print("Expected Output: [] | Actual Output:",
          solution.combinationSum([2], 1))

    # Test case 4: Large number in candidates
    print("Test Case 4: candidates = [2,7,9], target = 14")
    print("Expected Output: [[2,2,2,2,2,2,2],[7,7]] | Actual Output:",
          solution.combinationSum([2, 7, 9], 14))

    # Test case 5: Single element repeated multiple times
    print("Test Case 5: candidates = [5], target = 10")
    print("Expected Output: [[5,5]] | Actual Output:",
          solution.combinationSum([5], 10))

    # Test case 6: Edge case with large elements
    print("Test Case 6: candidates = [3,5,8], target = 11")
    print("Expected Output: [[3,3,5],[3,8]] | Actual Output:",
          solution.combinationSum([3, 5, 8], 11))

"""
Time Complexity:
- O(2^N) → The worst case explores all subsets due to repeated choices.

Space Complexity:
- O(target/min(candidates)) → Depth of the recursion tree.
"""
