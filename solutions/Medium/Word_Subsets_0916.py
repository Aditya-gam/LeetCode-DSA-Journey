from collections import Counter


class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        # Calculate the maximum frequency requirements for words2
        max_freq = Counter()
        for word in words2:
            freq = Counter(word)
            for char in freq:
                max_freq[char] = max(max_freq[char], freq[char])

        # Check each word in words1
        result = []
        for word in words1:
            freq = Counter(word)
            if all(freq[char] >= max_freq[char] for char in max_freq):
                result.append(word)

        return result


# Example test cases
sol = Solution()
print(sol.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], [
      "e", "o"]))  # Output: ["facebook", "google", "leetcode"]
print(sol.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], [
      "l", "e"]))  # Output: ["apple", "google", "leetcode"]
print(sol.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], [
      "e", "oo"]))  # Output: ["facebook", "google"]
print(sol.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], [
      "lo", "eo"]))  # Output: ["google", "leetcode"]
print(sol.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], [
      "ec", "oc", "ceo"]))  # Output: ["facebook", "leetcode"]
print(sol.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], [
      "e", "oo"]))  # Output: ["facebook", "google"]

# Complexity Analysis
# Time Complexity: O(m×L2+n×L1)
# Preprocessing words2: O(m×L2), where m is the length of words2 and L2 is the average length of strings in words2.
# Checking words1: O(n×L1), where n is the length of words1 and L1 is the average length of strings in words1.

# Space Complexity: O(26) for the character frequency dictionary (constant space for the alphabet).
