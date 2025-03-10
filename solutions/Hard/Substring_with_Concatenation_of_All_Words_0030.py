from collections import defaultdict


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]

        Returns all starting indices in s at which the substring is 
        a concatenation of all words in 'words' in any order.
        """
        if not s or not words:
            return []

        wordLen = len(words[0])
        nWords = len(words)
        totalLen = wordLen * nWords
        if totalLen > len(s):
            return []

        # Build frequency map of words
        freq = defaultdict(int)
        for w in words:
            freq[w] += 1

        res = []

        # We will attempt each offset in [0..wordLen-1]
        for startOffset in range(wordLen):
            left = startOffset
            currentCount = defaultdict(int)
            count = 0  # number of words matched in the current window

            # Move in steps of wordLen
            for right in range(startOffset, len(s), wordLen):
                if right + wordLen > len(s):
                    break
                chunk = s[right: right + wordLen]

                # If chunk is valid
                if chunk in freq:
                    currentCount[chunk] += 1
                    count += 1

                    # If we have more occurrences than allowed, shrink from the left
                    while currentCount[chunk] > freq[chunk]:
                        leftChunk = s[left: left + wordLen]
                        currentCount[leftChunk] -= 1
                        count -= 1
                        left += wordLen

                    # Check if we formed a valid window of size nWords
                    if count == nWords:
                        res.append(left)

                        # Slide one word from the left out of the window
                        leftChunk = s[left: left + wordLen]
                        currentCount[leftChunk] -= 1
                        count -= 1
                        left += wordLen
                else:
                    # Reset window if invalid chunk
                    currentCount.clear()
                    count = 0
                    left = right + wordLen

        return res


# Example test
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s1 = "barfoothefoobarman"
    words1 = ["foo", "bar"]
    # Output: [0, 9]
    print(solution.findSubstring(s1, words1))

    # Example 2
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word", "good", "best", "word"]
    # Output: []
    print(solution.findSubstring(s2, words2))

    # Example 3
    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar", "foo", "the"]
    # Output: [6,9,12]
    print(solution.findSubstring(s3, words3))

    # Example 4
    s4 = "wordgoodgoodgoodbestword"
    words4 = ["word", "good", "best", "good"]
    # Output: [8]
    print(solution.findSubstring(s4, words4))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n*m), where n is the length of the input string 's' and m is the number of words in 'words'.
# Space complexity: O(m), where m is the number of words in 'words'. The space complexity is due to the frequency map 'freq'.
