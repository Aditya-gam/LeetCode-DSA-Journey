class StockSpanner(object):

    def __init__(self):
        """
        Initialize a stack to maintain (price, span) tuples.
        The stack is maintained in a monotonically decreasing
        order of price, ensuring we can pop smaller/equal prices
        to accumulate spans efficiently.
        """
        self.stack = []  # will store tuples: (price, span)

    def next(self, price):
        """
        Returns the span of the stock's price for the current day.

        :type price: int
        :rtype: int
        """
        span = 1  # The span at least covers the current day

        # Pop from the stack while the top's price is <= current price
        while self.stack and self.stack[-1][0] <= price:
            top_price, top_span = self.stack.pop()
            span += top_span

        # Push the current price and its total span
        self.stack.append((price, span))

        # The span for this day is the sum of all popped spans plus 1
        return span

# Example test cases


def test_StockSpanner():
    S = StockSpanner()
    assert S.next(100) == 1
    assert S.next(80) == 1
    assert S.next(60) == 1
    assert S.next(70) == 2
    assert S.next(60) == 1
    assert S.next(75) == 4
    assert S.next(85) == 6

    # Additional test case: increasing prices
    S = StockSpanner()
    assert S.next(10) == 1
    assert S.next(20) == 2
    assert S.next(30) == 3
    assert S.next(40) == 4
    assert S.next(50) == 5

    # Additional test case: decreasing prices
    S = StockSpanner()
    assert S.next(50) == 1
    assert S.next(40) == 1
    assert S.next(30) == 1
    assert S.next(20) == 1
    assert S.next(10) == 1

    # Additional test case: random prices
    S = StockSpanner()
    assert S.next(100) == 1
    assert S.next(80) == 1
    assert S.next(90) == 2
    assert S.next(70) == 1
    assert S.next(60) == 1
    assert S.next(75) == 2

    assert S.next(110) == 10
    assert S.next(115) == 11
    assert S.next(120) == 12

    assert S.next(140) == 16
    assert S.next(145) == 17
    assert S.next(150) == 18
    assert S.next(155) == 19
    assert S.next(160) == 20
    assert S.next(165) == 21
    assert S.next(170) == 22
    assert S.next(175) == 23
    assert S.next(180) == 24
    assert S.next(185) == 25

    assert S.next(205) == 29
    assert S.next(210) == 30
    assert S.next(215) == 31
    assert S.next(220) == 32
    assert S.next(225) == 33
    assert S.next(230) == 34
    assert S.next(235) == 35

    print("All test cases passed!")


test_StockSpanner()

# Time complexity analysis:
# Time complexity: O(n) for n calls to next().
# Each price is pushed and popped from the stack at most once.
# Therefore, the time complexity is O(n).

# Space complexity analysis: O(n) for n calls to next().
# The stack maintains a monotonically decreasing sequence of prices.
# The total number of prices added to the stack is at most n.
# Therefore, the space complexity is O(n).
