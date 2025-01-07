class Solution(object):
    def plusOne(self, digits):
        """
        Increment the large integer represented by digits by one.

        :param digits: List[int] - List of digits representing the integer
        :return: List[int] - Resulting digits after incrementing by one
        """
        n = len(digits)

        # Traverse from the last digit to the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                # If digit is 9, set it to 0 and carry over
                digits[i] = 0

        # If we finished the loop, it means we had a carry at the most significant digit
        return [1] + digits


# Example test cases
sol = Solution()
print(sol.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(sol.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(sol.plusOne([9]))  # Output: [1, 0]
print(sol.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]

# Complexity Analysis
# Time Complexity: O(n) We traverse the list once from right to left.
# Space Complexity: O(1) We modify the input list in place and use constant extra space, except for the case where we prepend a digit, which requires O(n) space.
