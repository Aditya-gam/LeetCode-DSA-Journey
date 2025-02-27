class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # Initialize the first three numbers
        t0, t1, t2 = 0, 1, 1

        # Compute Tribonacci iteratively
        for i in range(3, n + 1):
            t_next = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t_next

        return t2


#  Example test cases
# Test case 1
n = 4
assert Solution().tribonacci(n) == 4

# Test case 2
n = 25
assert Solution().tribonacci(n) == 1389537

# Test case 3 (smallest input)
n = 0
assert Solution().tribonacci(n) == 0

# Test case 4 (smallest input for base case)
n = 1
assert Solution().tribonacci(n) == 1

# Test case 5 (second base case)
n = 2
assert Solution().tribonacci(n) == 1

print("All test cases pass")

# Complexity analysis
# Time complexity: O(n), where n is the input number n.

# Space complexity: O(1) since we are using a constant amount of space.
