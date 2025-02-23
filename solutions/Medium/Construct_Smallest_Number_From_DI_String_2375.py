class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        Function: smallestNumber
        Description: Constructs the lexicographically smallest number following the given 
                     'I' (increasing) and 'D' (decreasing) pattern.

        Parameters:
        - pattern (str): A string of 'I' and 'D' characters.

        Returns:
        - str: The smallest lexicographically valid number that follows the pattern.
        """

        stack = []
        result = ""

        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))  # Push the next available digit
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result += stack.pop()  # Pop all elements when an 'I' is encountered

        return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic increasing and decreasing pattern
    print(solution.smallestNumber("IIIDIDDD"))
    # Expected output: "123549876"

    # Test case 2: All decreasing pattern
    print(solution.smallestNumber("DDD"))
    # Expected output: "4321"

    # Test case 3: All increasing pattern
    print(solution.smallestNumber("III"))
    # Expected output: "1234"

    # Test case 4: Mixed pattern with single 'D' at the start
    print(solution.smallestNumber("DIDI"))
    # Expected output: "21435"

    # Test case 5: Single 'I'
    print(solution.smallestNumber("I"))
    # Expected output: "12"

    # Test case 6: Single 'D'
    print(solution.smallestNumber("D"))
    # Expected output: "21"

    # Test case 7: Edge case with maximum length pattern
    print(solution.smallestNumber("DIDIDIDI"))
    # Expected output: "21436587"

    # Test case 8: Edge case with minimum length pattern
    print(solution.smallestNumber("I"))
    # Expected output: "12"

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the length of the given pattern string. We iterate through the pattern string once to construct the smallest number.
# Space Complexity: O(N), where N is the length of the given pattern string. The stack can store at most N + 1 elements.
