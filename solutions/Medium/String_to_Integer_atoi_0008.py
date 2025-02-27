class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Function: myAtoi
        Description: Converts a given string into a 32-bit signed integer, following the rules of the atoi function.

        Parameters:
        - s (str): The input string.

        Returns:
        - int: The converted integer within the 32-bit signed integer range.
        """
        # Define integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Step 1: Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0  # Empty string after trimming whitespace

        # Step 2: Handle sign
        sign = 1
        index = 0
        if s[index] in ["+", "-"]:
            if s[index] == "-":
                sign = -1
            index += 1  # Move to the next character

        # Step 3: Convert numeric characters to integer
        num = 0
        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1

        # Apply the sign
        num *= sign

        # Step 4: Clamp the number within 32-bit signed integer range
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Simple integer
    print(solution.myAtoi("42"))
    # Expected output: 42

    # Test case 2: Negative integer with leading zeros
    print(solution.myAtoi("   -042"))
    # Expected output: -42

    # Test case 3: Number followed by letters
    print(solution.myAtoi("1337c0d3"))
    # Expected output: 1337

    # Test case 4: Zero with trailing non-numeric characters
    print(solution.myAtoi("0-1"))
    # Expected output: 0

    # Test case 5: Non-numeric characters first
    print(solution.myAtoi("words and 987"))
    # Expected output: 0

    # Test case 6: Large number exceeding 32-bit signed integer
    print(solution.myAtoi("9999999999"))
    # Expected output: 2147483647 (INT_MAX)

    # Test case 7: Large negative number exceeding 32-bit signed integer
    print(solution.myAtoi("-9999999999"))
    # Expected output: -2147483648 (INT_MIN)

    # Test case 8: Empty string
    print(solution.myAtoi(""))
    # Expected output: 0

    # Test case 9: String with only spaces
    print(solution.myAtoi("    "))
    # Expected output: 0

    # Test case 10: Valid integer followed by non-numeric characters
    print(solution.myAtoi("   +42abc"))
    # Expected output: 42

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(n), where n is the length of the input string.
# Space Complexity: O(1), since we are using only a constant amount of space.
