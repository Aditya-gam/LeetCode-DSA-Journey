class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def canFinish(speed):
            # Calculate total hours needed at this speed
            total_hours = 0
            for pile in piles:
                total_hours += (pile + speed - 1) // speed  # Ceiling division
            return total_hours <= h

        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if canFinish(mid):
                high = mid  # Try a smaller speed
            else:
                low = mid + 1  # Increase speed

        return low


# Example test cases
solution = Solution()

# Example 1
piles = [3, 6, 7, 11]
h = 8
assert Solution().minEatingSpeed(piles, h) == 4

# Example 2
piles = [30, 11, 23, 4, 20]
h = 5
assert Solution().minEatingSpeed(piles, h) == 30

# Example 3
piles = [30, 11, 23, 4, 20]
h = 6
assert Solution().minEatingSpeed(piles, h) == 23

# Edge Case: Single pile
piles = [1000000000]
h = 1
assert Solution().minEatingSpeed(piles, h) == 1000000000

# Edge Case: Maximum piles and hours
piles = [1] * 10000
h = 10000
assert Solution().minEatingSpeed(piles, h) == 1

print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(N * log M) where N is the number of piles and M is the maximum number of bananas in a pile.
# Space Complexity: O(1) since we are using a constant amount of space.
