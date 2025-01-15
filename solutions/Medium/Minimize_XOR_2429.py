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
