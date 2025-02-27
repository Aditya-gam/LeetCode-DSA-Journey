class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        This function calculates the maximum profit possible 
        by buying and selling the stock on different days, 
        ensuring the sell day comes after the buy day.
        """
        # If prices has only one day or is empty, we can't make a profit
        if len(prices) < 2:
            return 0

        min_price = prices[0]  # track the minimum price encountered so far
        max_profit = 0         # track the maximum profit

        # Iterate over prices starting from day 2 (index 1)
        for i in range(1, len(prices)):
            # Update min_price if current price is lower
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                # Calculate potential profit if sold today
                profit = prices[i] - min_price
                # Update max profit if this is better
                if profit > max_profit:
                    max_profit = profit

        return max_profit


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    # Buy at price=1 (day 2), sell at price=6 (day 5) => profit=5
    assert solution.maxProfit(prices1) == 5  # Expected: 5

    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    # Prices always decrease, max profit is 0
    assert solution.maxProfit(prices2) == 0  # Expected: 0

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate through the prices list once
# Space complexity: O(1) - We use a constant amount of extra space
