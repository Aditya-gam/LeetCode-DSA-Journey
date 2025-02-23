class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # Count set bits in num2
        count_bits_num2 = bin(num2).count('1')

        # Initialize result and count of set bits in result
        x = 0

        # Use bits from num1 as much as possible
        for i in range(31, -1, -1):
            if count_bits_num2 == 0:
                break
            if num1 & (1 << i):
                x |= (1 << i)
                count_bits_num2 -= 1

        # If more set bits are needed, add from lower bits
        for i in range(32):
            if count_bits_num2 == 0:
                break
            if not (x & (1 << i)):
                x |= (1 << i)
                count_bits_num2 -= 1

        return x


# Test cases
solution = Solution()

assert solution.minimizeXor(3, 5) == 3  # Example 1
assert solution.minimizeXor(1, 12) == 3  # Example 2
assert solution.minimizeXor(8, 7) == 7   # Case with different set bit counts
assert solution.minimizeXor(0, 15) == 15  # Case with num1 = 0
assert solution.minimizeXor(15, 1) == 1  # Case with minimal num2 set bits
assert solution.minimizeXor(15, 15) == 0  # Case with equal numbers

# Complexity Analysis
# Time Complexity: O(1), as we are iterating over 32 bits.
# Space Complexity: O(1), as we are using a constant amount of space.
