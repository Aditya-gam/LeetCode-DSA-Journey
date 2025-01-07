class Solution(object):
    def isPalindrome(self, s):
        """
        Check if the given string is a valid palindrome.

        :param s: str - Input string
        :return: bool - True if the string is a palindrome, False otherwise
        """
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered = ''.join(char.lower() for char in s if char.isalnum())

        # Use two pointers to check for palindrome
        left, right = 0, len(filtered) - 1
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1

        return True


# Example test cases
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(sol.isPalindrome("race a car"))                     # Output: False
print(sol.isPalindrome(" "))                              # Output: True
