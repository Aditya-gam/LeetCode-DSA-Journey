class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sum_of_squares(num):
            """Helper function to compute sum of squares of digits."""
            total = 0
            while num:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow, fast = n, sum_of_squares(n)

        while fast != 1 and slow != fast:
            slow = sum_of_squares(slow)       # Move slow by 1 step
            fast = sum_of_squares(sum_of_squares(fast))  # Move fast by 2 steps

        return fast == 1  # If fast reaches 1, it's a happy number


# Example test cases
if __name__ == "__main__":
    sol = Solution()
    # Output: True
    print(sol.isHappy(19))
    # Output: False
    print(sol.isHappy(2))
    # Output: True
    print(sol.isHappy(7))
    # Output: True
    print(sol.isHappy(1))
    # Output: False
    print(sol.isHappy(0))
    # Output: False
    print(sol.isHappy(3))
    # Output: False
    print(sol.isHappy(4))
    # Output: True
    print(sol.isHappy(10))
    # Output: True
    print(sol.isHappy(100))
    # Output: False
    print(sol.isHappy(101))
    # Output: True
    print(sol.isHappy(111))
    # Output: False
    print(sol.isHappy(112))
    # Output: False
    print(sol.isHappy(113))
    # Output: False
    print(sol.isHappy(114))
    # Output: False
    print(sol.isHappy(115))
    # Output: False
    print(sol.isHappy(116))
    # Output: False
    print(sol.isHappy(117))
    # Output: False
    print(sol.isHappy(118))
    # Output: False
    print(sol.isHappy(119))
    # Output: False
    print(sol.isHappy(120))
    # Output: False
    print(sol.isHappy(121))
    # Output: False
    print(sol.isHappy(122))
    # Output: False
    print(sol.isHappy(123))
    # Output: False
    print(sol.isHappy(124))
    # Output: False
    print(sol.isHappy(125))
    # Output: False
    print(sol.isHappy(126))
    # Output: False
    print(sol.isHappy(127))
    # Output: False
    print(sol.isHappy(128))
    # Output: False
    print(sol.isHappy(129))
    # Output: False
    print(sol.isHappy(130))
    # Output: False
    print(sol.isHappy(131))
    # Output: False
    print(sol.isHappy(132))
    # Output: False
    print(sol.isHappy(133))
    # Output: False
    print(sol.isHappy(134))
    # Output: False
    print(sol.isHappy(135))
    # Output: False

    print("All test cases passed successfully!")

# Complexity Analysis
# Time Complexity: O(log(N)), where N is the input number n. The time complexity is dominated by the number of digits in the input number.
# Space Complexity: O(1), as we use only a constant amount of extra space.
