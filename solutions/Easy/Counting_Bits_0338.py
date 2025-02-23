class Solution(object):
    def countBits(self, n):
        """
        Returns an array of length n + 1 such that ans[i] is the number
        of 1's in the binary representation of i.

        :type n: int
        :rtype: List[int]
        """
        # Initialize the result array
        ans = [0] * (n + 1)

        # Build the result using the relation:
        # ans[i] = ans[i >> 1] + (i & 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans

# Example test cases


def test_countBits():
    sol = Solution()

    # Test case 1
    # n = 2, binary representations:
    # 0 -> 0 -> 0 bits
    # 1 -> 1 -> 1 bit
    # 2 -> 10 -> 1 bit
    # Expected result: [0, 1, 1]
    assert sol.countBits(2) == [0, 1, 1]

    # Test case 2
    # n = 5:
    # 0 -> 0    -> 0 bits
    # 1 -> 1    -> 1 bit
    # 2 -> 10   -> 1 bit
    # 3 -> 11   -> 2 bits
    # 4 -> 100  -> 1 bit
    # 5 -> 101  -> 2 bits
    # Expected: [0, 1, 1, 2, 1, 2]
    assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]

    # Test case 3: n = 0
    # Only one number: 0 -> 0 bits
    assert sol.countBits(0) == [0]

    # Test case 4: Some random checks
    # n = 6:
    #   0 -> 0 bits
    #   1 -> 1 bit
    #   2 -> 10 (1 bit)
    #   3 -> 11 (2 bits)
    #   4 -> 100 (1 bit)
    #   5 -> 101 (2 bits)
    #   6 -> 110 (2 bits)
    # Expected: [0, 1, 1, 2, 1, 2, 2]
    assert sol.countBits(6) == [0, 1, 1, 2, 1, 2, 2]

    print("All test cases passed!")


test_countBits()

# Complexity analysis
# Time complexity: O(n) - We iterate over all numbers from 1 to n.
# Space complexity: O(n) - We store the result in an array of size n + 1.
