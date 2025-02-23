class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        Converts a valid Roman numeral string to its integer value.
        """
        # Map Roman characters to their values
        values = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n - 1):
            # If a smaller value precedes a bigger one, subtract it
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        # Add the value of the last symbol
        total += values[s[-1]]

        return total


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "III"
    # III = 1 + 1 + 1 = 3
    assert solution.romanToInt(s1) == 3

    # Test case 2
    s2 = "LVIII"
    # L=50, V=5, I=1, I=1, I=1 => 58
    assert solution.romanToInt(s2) == 58

    # Test case 3
    s3 = "MCMXCIV"
    # M=1000, CM=900, XC=90, IV=4 => 1994
    assert solution.romanToInt(s3) == 1994

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate over the string once.
# Space complexity: O(1) - We use a constant amount of extra space.
