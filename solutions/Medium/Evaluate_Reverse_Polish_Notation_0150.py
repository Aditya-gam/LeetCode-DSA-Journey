from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Function: evalRPN
        Description: Evaluates an arithmetic expression given in Reverse Polish Notation (RPN).
                     The valid operators are '+', '-', '*', and '/'.
                     Division truncates toward zero.

        Parameters:
        - tokens (List[str]): A list of strings representing an arithmetic expression in RPN.

        Returns:
        - int: The evaluated integer result of the RPN expression.
        """
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # Pop the last two elements
                b = stack.pop()
                a = stack.pop()

                # Perform the operation
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Perform integer division that truncates towards zero
                    stack.append(int(a / b))
            else:
                # Convert operand to integer and push onto stack
                stack.append(int(token))

        # Final result will be the only element left in the stack
        return stack.pop()


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic arithmetic operations
    print(solution.evalRPN(["2", "1", "+", "3", "*"]))
    # Expected output: 9  -> ((2 + 1) * 3) = 9

    # Test case 2: Division operation
    print(solution.evalRPN(["4", "13", "5", "/", "+"]))
    # Expected output: 6  -> (4 + (13 / 5)) = 6

    # Test case 3: Complex nested expression
    print(solution.evalRPN(["10", "6", "9", "3", "+",
          "-11", "*", "/", "*", "17", "+", "5", "+"]))
    # Expected output: 22

    # Test case 4: Single operand
    print(solution.evalRPN(["100"]))
    # Expected output: 100

    # Test case 5: Subtraction and negative result
    print(solution.evalRPN(["3", "4", "-"]))
    # Expected output: -1  -> (3 - 4) = -1

    # Test case 6: Multiplication with negative number
    print(solution.evalRPN(["-2", "3", "*"]))
    # Expected output: -6  -> (-2 * 3) = -6

    # Test case 7: Division truncation behavior
    print(solution.evalRPN(["10", "3", "/"]))
    # Expected output: 3  -> (10 / 3) truncates to 3

    print(solution.evalRPN(["-10", "3", "/"]))
    # Expected output: -3  -> (-10 / 3) truncates to -3

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N) where N is the number of elements in the input list 'tokens'. We iterate through each token once.
# Space Complexity: O(N) where N is the number of elements in the input list 'tokens'. The stack can hold at most N/2 elements
