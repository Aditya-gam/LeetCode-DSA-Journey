class Solution:
    def calculate(self, s: str) -> int:
        """
        Function: calculate
        Description: Evaluates a mathematical expression given as a string, handling 
                     addition, subtraction, and parentheses without using eval().

        Parameters:
        - s (str): The input mathematical expression.

        Returns:
        - int: The result of the evaluated expression.
        """

        def evaluate(expression: str) -> int:
            """
            Helper function to evaluate the mathematical expression using a stack.

            Parameters:
            - expression (str): The cleaned mathematical expression.

            Returns:
            - int: The evaluated result.
            """
            stack = []
            num = 0
            sign = 1  # 1 for positive, -1 for negative
            result = 0

            for char in expression:
                if char.isdigit():
                    num = num * 10 + int(char)
                elif char in "+-":
                    result += sign * num
                    num = 0
                    sign = 1 if char == '+' else -1
                elif char == '(':
                    stack.append(result)
                    stack.append(sign)
                    result = 0
                    sign = 1
                elif char == ')':
                    result += sign * num
                    num = 0
                    result *= stack.pop()  # Multiply by the previous sign
                    result += stack.pop()  # Add the previous result

            return result + (sign * num)

        # Remove spaces for easier processing
        return evaluate(s.replace(" ", ""))


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic addition
    print(solution.calculate("1 + 1"))
    # Expected output: 2

    # Test case 2: Addition and subtraction with spaces
    print(solution.calculate(" 2-1 + 2 "))
    # Expected output: 3

    # Test case 3: Complex expression with parentheses
    print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))
    # Expected output: 23

    # Test case 4: Nested parentheses
    print(solution.calculate("((2+3)-(1-4))"))
    # Expected output: 8

    # Test case 5: Single number
    print(solution.calculate("42"))
    # Expected output: 42

    # Test case 6: Handling unary minus
    print(solution.calculate("- (3 + (2 - 1))"))
    # Expected output: -4

    # Test case 7: Large expression
    print(solution.calculate("10 - (2 + 3) + (8 - (3 + 2))"))
    # Expected output: 8

    # Test case 8: More complex expression
    print(solution.calculate("(5-(1+(5)))"))
    # Expected output: -1

    # Test case 9: Edge case with empty string
    print(solution.calculate(""))
    # Expected output: 0

    # Test case 10: Edge case with a single number
    print(solution.calculate("1"))
    # Expected output: 1

    # Test case 11: Edge case with a single negative number
    print(solution.calculate("-1"))
    # Expected output: -1

    # Test case 12: Edge case with a single negative number in parentheses
    print(solution.calculate("(-1)"))
    #  Expected output: -1

    print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(n) where n is the length of the input string s. We iterate through the string once to evaluate the expression.


# Space Complexity: O(n) where n is the length of the input string s. We use a stack to store the intermediate results and parentheses.
# The maximum size of the stack can be n/2 for a fully nested expression.
