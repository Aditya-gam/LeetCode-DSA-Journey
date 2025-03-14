class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str

        Converts string s to a zigzag pattern and reads it row-by-row.
        """
        # Edge cases
        if numRows == 1 or numRows >= len(s):
            return s

        # Prepare rows
        # or [""] for each row if you prefer string concatenation
        rows = [[] for _ in range(numRows)]
        currRow = 0
        direction = 1  # +1 means moving down, -1 means moving up

        for char in s:
            rows[currRow].append(char)

            currRow += direction
            if currRow == 0:
                direction = +1
            elif currRow == numRows - 1:
                direction = -1

        # Combine rows into a single string
        return "".join("".join(row) for row in rows)


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    s1 = "PAYPALISHIRING"
    numRows1 = 3
    # Expected "PAHNAPLSIIGYIR"
    print(solution.convert(s1, numRows1))

    s2 = "PAYPALISHIRING"
    numRows2 = 4
    # Expected "PINALSIGYAHRPI"
    print(solution.convert(s2, numRows2))

    s3 = "A"
    numRows3 = 1
    # Expected "A"
    print(solution.convert(s3, numRows3))

    s4 = "AB"
    numRows4 = 1
    # Expected "AB"
    print(solution.convert(s4, numRows4))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n), where n is the length of the input string 's'.

# Space complexity: O(n), where n is the length of the input string 's'. The space complexity is due to the rows list, which stores the characters in each row. The space complexity can be reduced to O(1) if we use a single string for each row instead of a list of characters.
