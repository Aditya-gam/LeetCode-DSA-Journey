from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Function: generateParenthesis
        Description: Generates all valid combinations of n pairs of parentheses.

        Parameters:
        - n (int): Number of pairs of parentheses.

        Returns:
        - List[str]: A list of all well-formed parentheses combinations.
        """
        def backtrack(s, open_count, close_count):
            # Base Case: Valid combination found
            if len(s) == 2 * n:
                result.append(s)
                return

            # Add an open parenthesis if we haven't reached the limit
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            # Add a closing parenthesis if it does not exceed open count
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        result = []
        backtrack("", 0, 0)

        return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Smallest case with n = 1
    print("Test Case 1: n = 1")
    print("Expected Output: ['()'] | Actual Output:",
          solution.generateParenthesis(1))

    # Test Case 2: Standard case with n = 2
    print("Test Case 2: n = 2")
    print("Expected Output: ['(())', '()()'] | Actual Output:",
          solution.generateParenthesis(2))

    # Test Case 3: n = 3 (More complex case)
    print("Test Case 3: n = 3")
    print("Expected Output: ['((()))', '(()())', '(())()', '()(())', '()()()'] | Actual Output:",
          solution.generateParenthesis(3))

    # Test Case 4: Edge case with n = 4
    print("Test Case 4: n = 4")
    print("Expected Output: 14 unique combinations | Actual Output:",
          len(solution.generateParenthesis(4)))

    # Test Case 5: Larger input (n = 5)
    print("Test Case 5: n = 5")
    print("Expected Output: 42 unique combinations | Actual Output:",
          len(solution.generateParenthesis(5)))

    # Test Case 6: Maximum constraint (n = 8)
    print("Test Case 6: n = 8")
    print("Expected Output: A large number of valid combinations | Actual Output:", len(
        solution.generateParenthesis(8)))

"""
Time Complexity:
- O(4^n / sqrt(n)) → Catalan number growth rate for valid sequences.

Space Complexity:
- O(4^n / sqrt(n)) → To store all valid sequences.
"""
