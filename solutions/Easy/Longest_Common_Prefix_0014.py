class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Edge case: if the list is empty, return an empty string
        if not strs:
            return ""

        # Sort the strings lexicographically
        strs.sort()

        # Compare the first and last strings in the sorted list
        first, last = strs[0], strs[-1]

        # Find the common prefix between the first and last strings
        common_prefix = []
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                common_prefix.append(first[i])
            else:
                break

        # Join the common prefix list into a string
        return ''.join(common_prefix)


# Example test cases
sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
print(sol.longestCommonPrefix(["ab", "a"]))                   # Output: "a"
print(sol.longestCommonPrefix(["a", "b"]))                    # Output: ""
print(sol.longestCommonPrefix(["a", "a"]))                    # Output: "a"
print(sol.longestCommonPrefix(["a", ""]))                     # Output: ""
print(sol.longestCommonPrefix(["", ""]))                      # Output: ""
print(sol.longestCommonPrefix(["", "a"]))                     # Output: ""
print(sol.longestCommonPrefix(["", "a", "b"]))                # Output: ""
print(sol.longestCommonPrefix(["", "a", "ab"]))               # Output: ""
print(sol.longestCommonPrefix(["", "ab", "a"]))               # Output: ""
print(sol.longestCommonPrefix(["", "ab", "ab"]))              # Output: "ab"
print(sol.longestCommonPrefix(["ab", "ab", "ab"]))            # Output: "ab"
print(sol.longestCommonPrefix(["ab", "ab", "a"]))             # Output: "a"
print(sol.longestCommonPrefix(["ab", "a", "ab"]))             # Output: "a"
print(sol.longestCommonPrefix(["a", "ab", "ab"]))             # Output: "a"

# Complexity Analysis
# Time complexity: O(n*log(n) + k)
# Sorting the array: O(nlogn), where n is the number of strings.
# Comparing the first and last strings: O(k), where k is the length of the shortest string.

# Space complexity: O(1) since we are using a constant amount of space.
