class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """

        return sum(1 for word in words if word.startswith(pref))


sol = Solution()
print(sol.prefixCount(["dog", "cat", "app", "apple", "doggy"], "app"))  # 2
print(sol.prefixCount(["dog", "cat", "app", "apple", "doggy"], "dog"))  # 2
print(sol.prefixCount(["dog", "cat", "app", "apple", "doggy"], "c"))  # 1
print(sol.prefixCount(["dog", "cat", "app", "apple", "doggy"], "d"))  # 2

# Complexity Analysis
# Time complexity : O(n). We iterate over the list of words of length n once.
# Space complexity : O(1). We are using a constant amount of space.
