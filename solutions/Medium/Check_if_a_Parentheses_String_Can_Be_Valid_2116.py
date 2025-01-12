class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        # Early return if length of s is odd (impossible to balance)
        if len(s) % 2 != 0:
            return False

        # Left-to-right pass
        balance = 0
        unlocked = 0
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked += 1  # Can adjust this character
            elif s[i] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:  # Not enough open to balance close
                if unlocked > 0:
                    unlocked -= 1  # Use an unlocked char to balance
                    balance += 1
                else:
                    return False  # Invalid

        # Right-to-left pass
        balance = 0
        unlocked = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                unlocked += 1  # Can adjust this character
            elif s[i] == ')':
                balance += 1
            else:
                balance -= 1

            if balance < 0:  # Not enough close to balance open
                if unlocked > 0:
                    unlocked -= 1  # Use an unlocked char to balance
                    balance += 1
                else:
                    return False  # Invalid

        return True


# Example test cases
sol = Solution()

# Test case 1
s = "))()))"
locked = "010100"
print(sol.canBeValid(s, locked))  # Output: true

# Test case 2
s = "()()"
locked = "0000"
print(sol.canBeValid(s, locked))  # Output: true

# Test case 3
s = "())("
locked = "1001"
print(sol.canBeValid(s, locked))  # Output: false

# Test case 4
s = "((()))"
locked = "000000"
print(sol.canBeValid(s, locked))  # Output: true

# Test case 5
s = "(()))("
locked = "000010"
print(sol.canBeValid(s, locked))  # Output: true

# Test case 6
s = "(()())"
locked = "111111"
print(sol.canBeValid(s, locked))  # Output: true

# Complexity analysis
# Time complexity: O(n) where n is the length of the string. We perform two linear passes (left-to-right and right-to-left).

# Space complexity: O(1) Only a few variables are used.
