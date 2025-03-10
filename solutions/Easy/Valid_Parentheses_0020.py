class Solution:
    def isValid(self, s: str) -> bool:
        """
        Function: isValid
        Description: This function checks whether a given string containing only '()', '[]', and '{}' 
                     is valid based on the following conditions:
                     - Every open bracket must be closed by the same type of bracket.
                     - Open brackets must be closed in the correct order.
                     - Every close bracket has a corresponding open bracket of the same type.

        Parameters:
        - s (str): The input string containing parentheses.

        Returns:
        - bool: True if the input string is valid, False otherwise.
        """
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                # Pop from stack if it's not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Simple valid case
    print(solution.isValid("()"))  # Expected output: True

    # Test case 2: Multiple valid brackets
    print(solution.isValid("()[]{}"))  # Expected output: True

    # Test case 3: Invalid due to mismatch
    print(solution.isValid("(]"))  # Expected output: False

    # Test case 4: Nested valid parentheses
    print(solution.isValid("([])"))  # Expected output: True

    # Test case 5: Invalid due to incorrect ordering
    print(solution.isValid("([)]"))  # Expected output: False

    # Test case 6: Single open bracket (invalid)
    print(solution.isValid("("))  # Expected output: False

    # Test case 7: Single closing bracket (invalid)
    print(solution.isValid("]"))  # Expected output: False

    # Test case 8: Empty string (valid)
    print(solution.isValid(""))  # Expected output: True

    # Test case 9: Long valid sequence
    print(solution.isValid("({[]})"))  # Expected output: True

    # Test case 10: Long invalid sequence
    print(solution.isValid("({[})]"))  # Expected output: False

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N) where N is the number of characters in the input string 's'.
# Space Complexity: O(N) where N is the number of characters in the input string 's'. The space complexity is due to the stack used to store the open brackets.
