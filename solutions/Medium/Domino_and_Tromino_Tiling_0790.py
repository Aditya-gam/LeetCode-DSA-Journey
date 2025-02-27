class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize dp and s arrays
        dp = [0] * (n + 1)
        s = [0] * (n + 1)

        # Base cases
        dp[1], dp[2] = 1, 2
        s[2] = 1

        for i in range(3, n + 1):
            dp[i] = (dp[i-1] + dp[i-2] + 2 * s[i-1]) % MOD
            s[i] = (s[i-1] + dp[i-2]) % MOD

        return dp[n]


# Example test cases
# Test case 1
assert Solution().numTilings(3) == 5

# Test case 2
assert Solution().numTilings(1) == 1

# Test case 3
assert Solution().numTilings(5) == 24

# Test case 4 (Edge case with a large n)
assert Solution().numTilings(1000) == 979232805

# Test case 5 (Edge case with the smallest input)
assert Solution().numTilings(0) == 1

print("All test cases pass")

# Complexity analysis
# Time complexity: O(n), where n is the input number n.
# Space complexity: O(n) since we are using an array of size n.
