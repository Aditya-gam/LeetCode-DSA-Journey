# Not required here, but included for consistency
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        This function computes the maximum profit for as many transactions 
        as possible, provided you can only hold one share at a time.
        """
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += (prices[i] - prices[i - 1])

        return max_profit


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    # Explanation:
    # - Buy at 1, sell at 5 -> Profit = 4
    # - Buy at 3, sell at 6 -> Profit = 3
    # Total profit = 4 + 3 = 7
    assert solution.maxProfit(prices1) == 7  # Expected: 7

    # Test case 2
    prices2 = [1, 2, 3, 4, 5]
    # Increasing sequence: effectively buy at 1 and sell at 5 => Profit = 4
    # Summation approach: (2-1) + (3-2) + (4-3) + (5-4) = 4
    assert solution.maxProfit(prices2) == 4  # Expected: 4

    # Test case 3
    prices3 = [7, 6, 4, 3, 1]
    # No chance to profit since prices never rise
    assert solution.maxProfit(prices3) == 0  # Expected: 0

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate through the prices list once
# Space complexity: O(1) - We use a constant amount of extra space
