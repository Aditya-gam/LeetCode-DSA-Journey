class Solution(object):
    def maxProfit(self, prices, fee):
        """
        Calculate the maximum profit you can achieve given
        an array of stock prices and a transaction fee.

        :param prices: List[int] - List of stock prices, prices[i] is the price on day i
        :param fee: int - The transaction fee for each buy-sell transaction
        :return: int - Maximum profit
        """

        if not prices:
            return 0

        # Initialize hold and cash for day 0
        hold = -prices[0]  # If we buy on the first day
        cash = 0           # If we do nothing on the first day

        for i in range(1, len(prices)):
            # Update cash first to use the old hold state
            # If we sell today, we add prices[i] - fee to hold
            new_cash = max(cash, hold + prices[i] - fee)

            # Update hold by deciding if we buy today (cash - prices[i]) or continue holding
            new_hold = max(hold, cash - prices[i])

            cash, hold = new_cash, new_hold

        return cash

# Example test cases


def test_maxProfit():
    sol = Solution()

    # Test 1: Provided example 1
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    # Explanation: Best transactions are:
    # - Buy at 1, sell at 8 (profit = 7 - 2 = 5)
    # - Buy at 4, sell at 9 (profit = 5 - 2 = 3)
    # Total = 8
    assert sol.maxProfit(prices, fee) == 8

    # Test 2: Provided example 2
    prices = [1, 3, 7, 5, 10, 3]
    fee = 3
    # Explanation: For instance:
    # - Buy at 1, sell at 7 (profit = 6 - 3 = 3)
    # - Buy at 5, sell at 10 (profit = 5 - 3 = 2)
    # Or buy at 3, sell at 10, etc. We can find total = 6
    assert sol.maxProfit(prices, fee) == 6

    # Test 3: Fee = 0 (special case)
    prices = [1, 2, 3, 4, 5]
    fee = 0
    # We can buy at 1, sell at 5 => profit = 4
    # Or do multiple transactions but it sums up the same or more
    # Actually in a scenario with no fee, the best strategy is to capture all ascending moves
    # So we end up with (5 - 1) = 4
    assert sol.maxProfit(prices, fee) == 4

    # Test 4: Descending prices
    prices = [10, 9, 8, 7, 6]
    fee = 2
    # No profitable transaction, best is to not trade at all
    assert sol.maxProfit(prices, fee) == 0

    # Test 5: Single day
    prices = [5]
    fee = 2
    # Can't sell after buying on the same day for profit, so 0
    assert sol.maxProfit(prices, fee) == 0

    print("All test cases passed!")


test_maxProfit()

# Complexity analysis
# Time complexity: O(n) - We iterate through the prices array once, where n is the length of the array.
# Space complexity: O(1) - We use a constant amount of extra space, regardless of the input size.
