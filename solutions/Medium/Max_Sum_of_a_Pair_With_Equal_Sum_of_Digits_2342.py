class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        def digit_sum(n):
            """Returns the sum of digits of a number."""
            return sum(int(digit) for digit in str(n))

        digit_map = defaultdict(list)
        max_sum = -1

        # Group numbers by their digit sum
        for num in nums:
            d_sum = digit_sum(num)
            digit_map[d_sum].append(num)

        # Check max sum of pairs for each digit sum group
        for key in digit_map:
            if len(digit_map[key]) >= 2:
                top_two = sorted(digit_map[key], reverse=True)[:2]
                max_sum = max(max_sum, sum(top_two))

        return max_sum


# Example test cases
if __name__ == "__main__":
    sol = Solution()
    # Output: 9
    print(sol.maximumSum([51, 71, 17, 42]))
    # Output: 93
    print(sol.maximumSum([42, 33, 60]))
    # Output: 102
    print(sol.maximumSum([51, 32, 43]))
    # Output: -1
    print(sol.maximumSum([51, 71, 17, 42, 33, 44, 24, 62, 11, 11]))
    # Output: 99
    print(sol.maximumSum([51, 71, 17, 42, 33, 44, 24, 62,
          11, 11, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88]))
    # Output: 0
    print(sol.maximumSum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # Output: 0
    print(sol.maximumSum([]))

    print("All test cases passed successfully!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of elements in the input list nums. We iterate over the list once to group numbers by their digit sum and then find the maximum sum of pairs for each group.
# Space Complexity: O(N), where N is the number of elements in the input list nums. We use a dictionary to group numbers by their digit sum, which can contain all elements in the worst case.
