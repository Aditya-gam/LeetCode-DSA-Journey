from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Function: letterCombinations
        Description: Returns all possible letter combinations represented by a string of digits (2-9).

        Parameters:
        - digits (str): String containing digits (2-9).

        Returns:
        - List[str]: All possible letter combinations in any order.
        """

        if not digits:
            return []

        # Mapping of digits to corresponding letters
        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        # Backtracking function
        def backtrack(index, path):
            if index == len(digits):
                res.append("".join(path))
                return

            for char in digit_to_letters[digits[index]]:
                backtrack(index + 1, path + [char])

        # Start backtracking from the first digit
        backtrack(0, [])

        return res


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard case with multiple digits
    print("Test Case 1: Digits '23'")
    digits1 = "23"
    print("Expected Output: ['ad','ae','af','bd','be','bf','cd','ce','cf'] | Actual Output:",
          solution.letterCombinations(digits1))

    # Test case 2: Empty string input
    print("Test Case 2: Empty string")
    digits2 = ""
    print("Expected Output: [] | Actual Output:",
          solution.letterCombinations(digits2))

    # Test case 3: Single digit case
    print("Test Case 3: Single digit '2'")
    digits3 = "2"
    print("Expected Output: ['a', 'b', 'c'] | Actual Output:",
          solution.letterCombinations(digits3))

    # Test case 4: Largest input case with 4 digits
    print("Test Case 4: Maximum length input '7896'")
    digits4 = "7896"
    print("Expected Output: Computed Output:",
          solution.letterCombinations(digits4))

    # Test case 5: Digits containing 7 and 9 (which have 4 letters)
    print("Test Case 5: Digits '79'")
    digits5 = "79"
    print("Expected Output: Computed Output:",
          solution.letterCombinations(digits5))

    # Test case 6: Consecutive numbers
    print("Test Case 6: Digits '456'")
    digits6 = "456"
    print("Expected Output: Computed Output:",
          solution.letterCombinations(digits6))

"""
Time Complexity:
- O(4^N) → Each digit (2-9) maps to 3-4 characters, resulting in exponential complexity.
- Space Complexity:
  - O(N) → Recursion stack depth for backtracking.
"""
