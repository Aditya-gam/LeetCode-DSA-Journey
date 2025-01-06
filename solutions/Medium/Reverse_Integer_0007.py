class Solution(object):
    def reverse(self, x):
        """
        Reverse the digits of a 32-bit signed integer.

        :param x: int - Input integer
        :return: int - Reversed integer or 0 if out of bounds
        """
        _, INT_MAX = -2**31, 2**31 - 1

        # Determine the sign and use absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse the digits
        reversed_num = 0
        while x != 0:
            digit = x % 10
            x //= 10
            # Check for overflow before multiplying by 10
            if (reversed_num > (INT_MAX - digit) // 10):
                return 0
            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num


# Example test cases
sol = Solution()
print(sol.reverse(123))   # Output: 321
print(sol.reverse(-123))  # Output: -321
print(sol.reverse(120))   # Output: 21
print(sol.reverse(0))     # Output: 0
print(sol.reverse(1534236469))  # Output: 0 (overflow case)
