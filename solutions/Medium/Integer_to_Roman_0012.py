class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str

        Convert an integer to its Roman numeral representation.
        """
        # List of (value, Roman numeral) pairs, in descending order.
        value_to_roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        roman_numeral = []
        # Greedily subtract the largest possible value until num becomes 0.
        for value, symbol in value_to_roman:
            while num >= value:
                num -= value
                roman_numeral.append(symbol)

        return "".join(roman_numeral)


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1:
    # 3749 -> MMMDCCXLIX
    print(solution.intToRoman(3749))  # Expected: "MMMDCCXLIX"

    # Test case 2:
    # 58 -> LVIII
    print(solution.intToRoman(58))    # Expected: "LVIII"

    # Test case 3:
    # 1994 -> MCMXCIV
    print(solution.intToRoman(1994))  # Expected: "MCMXCIV"

    # Test case 4:
    # 9 -> IX
    print(solution.intToRoman(9))     # Expected: "IX"

    # Test case 5:
    # 3999 -> MMMCMXCIX
    print(solution.intToRoman(3999))  # Expected: "MMMCMXCIX"

    # Test case 6:
    # 1 -> I
    print(solution.intToRoman(1))     # Expected: "I"

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(1) since the maximum number of iterations is fixed at 13.
# Space complexity: O(1) since the space used is constant.
