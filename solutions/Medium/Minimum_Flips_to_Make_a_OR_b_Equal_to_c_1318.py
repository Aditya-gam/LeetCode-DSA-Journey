class Solution(object):
    def minFlips(self, a, b, c):
        """
        Returns the minimum number of bit flips required 
        to make (a OR b == c).

        :param a: int
        :param b: int
        :param c: int
        :rtype: int
        """

        flips = 0
        for i in range(32):  # up to 31st bit for 32-bit integers
            # Extract the i-th bit of a, b, c
            a_i = (a >> i) & 1
            b_i = (b >> i) & 1
            c_i = (c >> i) & 1

            # Case 1: c_i = 1 => a_i | b_i should be 1
            if c_i == 1:
                # If both a_i and b_i are 0, need 1 flip (flip either bit to 1)
                if a_i == 0 and b_i == 0:
                    flips += 1

            # Case 2: c_i = 0 => a_i | b_i should be 0 => both a_i and b_i = 0
            else:  # c_i == 0
                if a_i == 1 and b_i == 1:
                    # Need 2 flips: flip both bits to 0
                    flips += 2
                elif a_i == 1 and b_i == 0:
                    # Need 1 flip: flip a_i to 0
                    flips += 1
                elif a_i == 0 and b_i == 1:
                    # Need 1 flip: flip b_i to 0
                    flips += 1
                # If both are already 0, no flips needed

        return flips

# Example test cases


def test_minFlips():
    sol = Solution()

    # Test Case 1
    a, b, c = 2, 6, 5
    # a = 010, b = 110, c = 101
    # 1 flip needed for a, 1 flip needed for b
    # Total flips = 2
    assert sol.minFlips(a, b, c) == 2

    # Test Case 2
    a, b, c = 4, 2, 7
    # a = 100, b = 010, c = 111
    # 2 flips needed for a, 1 flip needed for b
    # Total flips = 3
    assert sol.minFlips(a, b, c) == 3

    # Test Case 3
    a, b, c = 1, 2, 3
    # a = 001, b = 010, c = 011
    # 1 flip needed for a, 1 flip needed for b
    # Total flips = 2
    assert sol.minFlips(a, b, c) == 2

    # Test Case 4
    a, b, c = 0, 0, 0
    # a = 000, b = 000, c = 000
    # No flips needed
    assert sol.minFlips(a, b, c) == 0

    # Test Case 5
    a, b, c = 7, 7, 7
    # a = 111, b = 111, c = 111
    # No flips needed
    assert sol.minFlips(a, b, c) == 0

    # Test Case 6
    a, b, c = 0, 0, 1
    # a = 000, b = 000, c = 001
    # 1 flip needed for a, 1 flip needed for b
    # Total flips = 2
    assert sol.minFlips(a, b, c) == 2

    # Test Case 7
    a, b, c = 0, 0, 2
    # a = 000, b = 000, c = 010
    # 1 flip needed for a, 1 flip needed for b
    # Total flips = 2
    assert sol.minFlips(a, b, c) == 2

    print("All test cases passed!")


test_minFlips()

# Complexity Analysis
# Time Complexity: O(1) since we iterate over 32 bits for 32-bit integers.
# Space Complexity: O(1) since we use a constant amount of space.
