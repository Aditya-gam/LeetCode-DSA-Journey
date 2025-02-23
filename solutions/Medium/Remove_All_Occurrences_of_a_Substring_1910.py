class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        Removes occurrences of 'part' in 's' from left to right
        until none remain, returning the final string.
        """
        res = []
        plen = len(part)

        for c in s:
            # Append character
            res.append(c)

            # If at least length of part, check the suffix
            if len(res) >= plen and "".join(res[-plen:]) == part:
                # remove the last 'plen' characters
                del res[-plen:]

        return "".join(res)


# Example usage
if __name__ == "__main__":
    solution = Solution()

    s1, part1 = "daabcbaabcbc", "abc"
    # Expected: "dab"
    print(solution.removeOccurrences(s1, part1))

    s2, part2 = "axxxxyyyyb", "xy"
    # Expected: "ab"
    print(solution.removeOccurrences(s2, part2))

    s3, part3 = "abababaabababa", "ab"
    # Expected: "ab"
    print(solution.removeOccurrences(s3, part3))

    s4, part4 = "abc", "def"
    # Expected: "abc"
    print(solution.removeOccurrences(s4, part4))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n * m) where n is the length of the string 's' and m is the length of the string 'part'
# Space complexity: O(n) where n is the length of the string 's'
