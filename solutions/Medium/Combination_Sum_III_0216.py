class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, combination, current_sum):
            # If combination has k numbers and the sum is n, add to the result
            if len(combination) == k:
                if current_sum == n:
                    result.append(list(combination))
                return

            # Iterate through numbers from `start` to 9
            for i in range(start, 10):
                # If the sum exceeds n, no point in continuing
                if current_sum + i > n:
                    break

                # Add the number to the combination
                combination.append(i)
                # Recurse with the updated sum and combination
                backtrack(i + 1, combination, current_sum + i)
                # Backtrack by removing the last number
                combination.pop()

        # Start backtracking with initial values
        backtrack(1, [], 0)
        return result


# Example test cases
solution = Solution()

# Test case 1
k = 3
n = 7
assert Solution().combinationSum3(k, n) == [[1, 2, 4]]

# Test case 2
k = 3
n = 9
assert sorted(Solution().combinationSum3(k, n)) == sorted(
    [[1, 2, 6], [1, 3, 5], [2, 3, 4]])

# Test case 3
k = 4
n = 1
assert Solution().combinationSum3(k, n) == []

# Test case 4
k = 2
n = 17
assert Solution().combinationSum3(k, n) == [[8, 9]]

# Test case 5
k = 1
n = 9
assert Solution().combinationSum3(k, n) == [[9]]

print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(C(N, k)) where C(N, k) is the number of combinations of choosing k numbers from N numbers.
# Space Complexity: O(k) for the recursion stack and output list.
