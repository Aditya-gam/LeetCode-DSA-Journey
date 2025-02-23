class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Mapping of digits to letters
        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = []

        def backtrack(index, path):
            # Base case: if the current combination is complete
            if index == len(digits):
                result.append("".join(path))
                return

            # Get the letters corresponding to the current digit
            possible_letters = digit_to_letters[digits[index]]
            for letter in possible_letters:
                # Append the letter and recurse
                path.append(letter)
                backtrack(index + 1, path)
                # Backtrack by removing the last letter
                path.pop()

        # Start backtracking from the first digit
        backtrack(0, [])
        return result


# Example test cases
solution = Solution()

# Test case 1
digits = "23"
assert Solution().letterCombinations(digits) == [
    "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"
]

# Test case 2
digits = ""
assert Solution().letterCombinations(digits) == []

# Test case 3
digits = "2"
assert Solution().letterCombinations(digits) == ["a", "b", "c"]

# Test case 4: Maximum input length
digits = "234"
result = Solution().letterCombinations(digits)
assert len(result) == 27  # 3 * 3 * 3 = 27 combinations

print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(4^n * n) where n is the number of digits in the input string. This is because each digit can represent 4 letters in the worst case, and we have n digits.
# Space Complexity: O(n) where n is the number of digits in the input string. This is the space used for the recursion stack.
