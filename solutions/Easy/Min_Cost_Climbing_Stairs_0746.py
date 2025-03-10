class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Initialize the two base cases
        prev2, prev1 = 0, 0

        # Iterate through the steps
        for i in range(2, len(cost) + 1):
            # Compute the cost to reach step i
            curr = min(prev1 + cost[i-1], prev2 + cost[i-2])
            # Update previous states
            prev2, prev1 = prev1, curr

        return prev1


#  Example test cases
# Test case 1
cost = [10, 15, 20]
assert Solution().minCostClimbingStairs(cost) == 15

# Test case 2
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
assert Solution().minCostClimbingStairs(cost) == 6

# Test case 3
cost = [0, 0, 0, 0]
assert Solution().minCostClimbingStairs(cost) == 0

# Test case 4
cost = [10, 10, 10, 10]
assert Solution().minCostClimbingStairs(cost) == 20

# Test case 5 (edge case with smallest input)
cost = [10, 15]
assert Solution().minCostClimbingStairs(cost) == 10

print("All test cases pass")

# Complexity analysis
# Time complexity: O(n), where n is the length of the input list cost.

# Space complexity: O(1) since we are using a constant amount of space.
