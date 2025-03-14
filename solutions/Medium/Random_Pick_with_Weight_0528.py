import random
import bisect


class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        self.total = 0

        for weight in w:
            self.total += weight
            self.prefix_sums.append(self.total)  # Compute prefix sums

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix_sums, target)


# Example test cases
if __name__ == "__main__":
    solution = Solution([1, 3])
    assert solution.pickIndex() == 0
    assert solution.pickIndex() == 1

    print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(N), where N is the length of the w array.
# We compute the prefix sums of the w array in O(N) time.
# Space Complexity: O(N), where N is the length of the w array.
