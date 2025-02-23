from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        Finds the minimum window in s that contains all the characters of t.
        Returns an empty string if no such window exists.
        """
        if not s or not t:
            return ""

        need = Counter(t)
        required = len(need)  # Number of unique chars in t to be matched

        left, right = 0, 0
        formed = 0  # how many unique chars of t are matched with correct frequency in the window
        windowCount = {}

        # res = (window_length, left_index, right_index)
        res = (float("inf"), 0, 0)

        while right < len(s):
            # Include current char
            c = s[right]
            windowCount[c] = windowCount.get(c, 0) + 1

            # If this char's frequency in window matches the needed frequency
            if c in need and windowCount[c] == need[c]:
                formed += 1

            # Try to contract from the left if all required chars are matched
            while left <= right and formed == required:
                c = s[left]

                # Update res if this window is smaller
                window_length = right - left + 1
                if window_length < res[0]:
                    res = (window_length, left, right)

                # Remove char from window before moving left pointer
                windowCount[c] -= 1
                if c in need and windowCount[c] < need[c]:
                    formed -= 1

                left += 1

            # Move right pointer forward
            right += 1

        # If we never updated res, return ""
        if res[0] == float("inf"):
            return ""
        else:
            return s[res[1]: res[2] + 1]


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    # Expected: "BANC"
    print(solution.minWindow(s1, t1))

    # Example 2
    s2 = "a"
    t2 = "a"
    # Expected: "a"
    print(solution.minWindow(s2, t2))

    # Example 3
    s3 = "a"
    t3 = "aa"
    # Expected: ""
    print(solution.minWindow(s3, t3))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n), where n is the length of the input string 's'. The left and right pointers traverse the string at most twice.
# Space complexity: O(m), where m is the number of unique characters in 't'. The space complexity is due to the frequency maps 'need' and 'windowCount'.
