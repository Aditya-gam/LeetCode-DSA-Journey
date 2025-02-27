import bisect


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0

        # Step 1: Sort envelopes by width ASC, then by height DESC if width is the same
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Step 2: Find LIS on heights
        dp = []  # This will store the LIS

        for _, h in envelopes:
            idx = bisect.bisect_left(dp, h)  # Binary search

            if idx == len(dp):
                dp.append(h)  # Append to LIS
            else:
                dp[idx] = h  # Replace value

        # The length of dp is the maximum number of nested envelopes
        return len(dp)


# Example test cases
if __name__ == "__main__":
    solution = Solution()
    # Test on the example in the problem statement
    assert solution.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3
    # Additional test cases
    assert solution.maxEnvelopes([[1, 1], [1, 1], [1, 1]]) == 1
    assert solution.maxEnvelopes([[1, 1], [1, 1], [1, 1], [1, 1]]) == 1
    assert solution.maxEnvelopes([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]) == 1
    assert solution.maxEnvelopes(
        [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]) == 1

    print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(N log N), where N is the length of the envelopes array.
# We sort the envelopes array based on the width and height.
# We then find the LIS based on the height, which takes O(N log N) time.
# Space Complexity: O(N), where N is the length of the envelopes array.
