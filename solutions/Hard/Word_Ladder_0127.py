from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Function: ladderLength
        Description: Finds the shortest transformation sequence from beginWord to endWord.

        Parameters:
        - beginWord (str): The starting word.
        - endWord (str): The target word.
        - wordList (List[str]): A list of allowed words for transformation.

        Returns:
        - int: The length of the shortest transformation sequence, or 0 if no transformation is possible.
        """

        wordSet = set(wordList)  # Convert list to set for O(1) lookup
        if endWord not in wordSet:
            return 0  # If endWord is not in wordList, transformation is impossible

        queue = deque([(beginWord, 1)])  # (current_word, transformation_steps)

        while queue:
            current_word, steps = queue.popleft()

            if current_word == endWord:
                return steps  # Found the shortest path

            # Try all possible single-letter mutations
            for i in range(len(current_word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char != current_word[i]:  # Change one letter at a time
                        new_word = current_word[:i] + char + current_word[i+1:]

                        if new_word in wordSet:
                            queue.append((new_word, steps + 1))
                            # Remove from set to prevent revisiting
                            wordSet.remove(new_word)

        return 0  # No transformation path found


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard case with a valid transformation
    print("Test Case 1: Standard valid transformation")
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    print("Expected Output: 5 | Actual Output:",
          solution.ladderLength(beginWord1, endWord1, wordList1))

    # Test case 2: No valid transformation path
    print("Test Case 2: No valid transformation path")
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    print("Expected Output: 0 | Actual Output:",
          solution.ladderLength(beginWord2, endWord2, wordList2))

    # Test case 3: Single-step transformation
    print("Test Case 3: Direct transformation available")
    beginWord3 = "hit"
    endWord3 = "hot"
    wordList3 = ["hot"]
    print("Expected Output: 2 | Actual Output:",
          solution.ladderLength(beginWord3, endWord3, wordList3))

    # Test case 4: Large dictionary with a valid path
    print("Test Case 4: Large dictionary with valid path")
    beginWord4 = "cat"
    endWord4 = "dog"
    wordList4 = ["bat", "cot", "cog", "dog", "dot", "dat", "dag"]
    print("Expected Output: 4 | Actual Output:",
          solution.ladderLength(beginWord4, endWord4, wordList4))

    # Test case 5: Words that have no transformation path
    print("Test Case 5: No valid transformations")
    beginWord5 = "abc"
    endWord5 = "xyz"
    wordList5 = ["aaa", "bbb", "ccc"]
    print("Expected Output: 0 | Actual Output:",
          solution.ladderLength(beginWord5, endWord5, wordList5))

    # Test case 6: Longest possible transformation path
    print("Test Case 6: Longest possible transformation path")
    beginWord6 = "aaaa"
    endWord6 = "zzzz"
    wordList6 = ["aaaz", "aazz", "azzz", "zzzz"]
    print("Expected Output: 5 | Actual Output:",
          solution.ladderLength(beginWord6, endWord6, wordList6))

"""
Time Complexity:
- The worst-case scenario is checking all possible transformations.
- Each word has L positions, and for each position, there are 25 possible changes.
- BFS ensures each word is processed once.
- Time Complexity: O(N * L * 26), where N is the number of words and L is word length.
- Space Complexity: O(N) for storing visited words and queue.
"""
