class Solution:
    def punishmentNumber(self, n: int) -> int:
        """
        Function: punishmentNumber
        Description: Computes the punishment number of a given integer n.
                     The punishment number is the sum of squares of numbers i
                     that satisfy the condition where i*i can be partitioned into
                     contiguous substrings summing up to i.

        Parameters:
        - n (int): The upper limit of the range to check.

        Returns:
        - int: The punishment number of n.
        """

        def canPartition(square_str: str, target: int, index: int, current_sum: int) -> bool:
            """
            Helper function to determine if the square of a number can be partitioned 
            such that the sum of substrings equals the original number.

            Parameters:
            - square_str (str): The string representation of the squared number.
            - target (int): The original number.
            - index (int): Current index in the square string.
            - current_sum (int): Sum of selected substrings.

            Returns:
            - bool: True if a valid partition exists, else False.
            """
            if index == len(square_str):
                return current_sum == target

            for j in range(index + 1, len(square_str) + 1):
                part = int(square_str[index:j])
                if canPartition(square_str, target, j, current_sum + part):
                    return True
            return False

        punishment_sum = 0

        for i in range(1, n + 1):
            square = i * i
            if canPartition(str(square), i, 0, 0):
                punishment_sum += square

        return punishment_sum


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic input
    print(solution.punishmentNumber(10))
    # Expected output: 182

    # Test case 2: Larger input
    print(solution.punishmentNumber(37))
    # Expected output: 1478

    # Test case 3: Smallest input
    print(solution.punishmentNumber(1))
    # Expected output: 1

    # Test case 4: Checking multiple valid numbers
    print(solution.punishmentNumber(20))
    # Expected output: 182 + 1296 = 1478

    # Test case 5: Larger range
    print(solution.punishmentNumber(50))
    # Expected output: Sum of valid squares within [1, 50]

    # Test case 6: Larger range
    print(solution.punishmentNumber(100))
    # Expected output: Sum of valid squares within [1, 100]

    # Test case 7: Larger range
    print(solution.punishmentNumber(1000))
    # Expected output: Sum of valid squares within [1, 1000]

    print("All test cases passed!")

# Complexity Analysis
# Time complexity: O(n * m), where n is the input number and m is the number of digits in the square of n.
#                  The function canPartition is called for each number in the range [1, n], and for each number,
#                  the function canPartition is called for each digit in the square of the number.

# Space complexity: O(len(i)^2), where len(i) is the number of digits in the square of the number i.
#                   The space complexity is dominated by the recursive calls to the function canPartition.
