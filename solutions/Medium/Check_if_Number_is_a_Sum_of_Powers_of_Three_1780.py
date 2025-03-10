class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Function: checkPowersOfThree
        Description: Determines whether the given number `n` can be represented as a sum of distinct powers of three.

        Parameters:
        - n (int): The integer to check.

        Returns:
        - bool: True if `n` can be expressed as a sum of distinct powers of three, otherwise False.
        """

        while n > 0:
            if n % 3 == 2:
                return False  # If remainder is 2, we cannot represent it using distinct powers of 3
            n //= 3  # Reduce `n` by dividing by 3

        return True


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Can be represented using 3^1 + 3^2
    n = 12
    print("Test Case 1:", solution.checkPowersOfThree(n))
    # Expected Output: True

    # Test Case 2: Can be represented using 3^0 + 3^2 + 3^4
    n = 91
    print("Test Case 2:", solution.checkPowersOfThree(n))
    # Expected Output: True

    # Test Case 3: Cannot be represented as sum of distinct powers of three
    n = 21
    print("Test Case 3:", solution.checkPowersOfThree(n))
    # Expected Output: False

    # Test Case 4: Smallest number, should return True
    n = 1  # 3^0 = 1
    print("Test Case 4:", solution.checkPowersOfThree(n))
    # Expected Output: True

    # Test Case 5: Large number which is sum of distinct powers of three
    n = 104  # 3^0 + 3^3 + 3^4 = 1 + 27 + 81 = 104
    print("Test Case 5:", solution.checkPowersOfThree(n))
    # Expected Output: True

    # Test Case 6: Large number that cannot be represented
    n = 10000000  # Not expressible as a sum of distinct powers of three
    print("Test Case 6:", solution.checkPowersOfThree(n))
    # Expected Output: False

"""
Time Complexity:
- O(log₃(n)), as we divide `n` by 3 in each iteration.

Space Complexity:
- O(1), as we use only a few integer variables.
"""
