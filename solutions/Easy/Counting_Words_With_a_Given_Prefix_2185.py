class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """

        return sum(1 for word in words if word.startswith(pref))


sol = Solution()
# Output: 2
print(sol.prefixCount(["dog", "cat", "app", "apple", "doggy"], "app"))
# Output: 2
print(sol.prefixCount(["dog", "cat", "app", "apple", "doggy"], "dog"))
# Output: 1
print(sol.prefixCount(["dog", "cat", "app", "apple", "doggy"], "c"))
# Output: 2
print(sol.prefixCount(["dog", "cat", "app", "apple", "doggy"], "d"))
# Output: 2
print(sol.prefixCount(["pay", "attention", "practice", "attend"], "at"))
# Output: 0
print(sol.prefixCount(["leetcode", "win", "loops", "success"], "code"))

# Complexity Analysis
# Time complexity : O(n). We iterate over the list of words of length n once.
# Space complexity : O(1). We are using a constant amount of space.
