from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # Store the complete word at the last node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Function: findWords
        Description: Returns all words found in the board using DFS and Trie.

        Parameters:
        - board (List[List[str]]): 2D character grid.
        - words (List[str]): List of words to find in the board.

        Returns:
        - List[str]: Words found on the board.
        """

        # Build Trie from words
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        rows, cols = len(board), len(board[0])

        def dfs(node, r, c):
            char = board[r][c]
            if char not in node.children:
                return

            next_node = node.children[char]
            if next_node.word:
                result.add(next_node.word)
                next_node.word = None  # Avoid duplicates

            # Mark visited
            board[r][c] = "#"

            # Explore neighbors (up, down, left, right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in next_node.children:
                    dfs(next_node, nr, nc)

            # Restore state
            board[r][c] = char

            # Optimization: Remove leaf nodes in Trie to save memory
            if not next_node.children:
                del node.children[char]

        # Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie.root.children:
                    dfs(trie.root, r, c)

        return list(result)


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard case with multiple words found
    print("Test Case 1: Words present in board")
    board1 = [["o", "a", "a", "n"],
              ["e", "t", "a", "e"],
              ["i", "h", "k", "r"],
              ["i", "f", "l", "v"]]
    words1 = ["oath", "pea", "eat", "rain"]
    print("Expected Output: ['eat', 'oath'] | Actual Output:",
          solution.findWords(board1, words1))

    # Test case 2: Words not present in board
    print("Test Case 2: No words found")
    board2 = [["a", "b"],
              ["c", "d"]]
    words2 = ["abcb"]
    print("Expected Output: [] | Actual Output:",
          solution.findWords(board2, words2))

    # Test case 3: Board with a single row
    print("Test Case 3: Single row board")
    board3 = [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]]
    words3 = ["abc", "def", "ghi", "cd"]
    print("Expected Output: ['abc', 'def', 'cd'] | Actual Output:",
          solution.findWords(board3, words3))

    # Test case 4: Board with a single column
    print("Test Case 4: Single column board")
    board4 = [["a"], ["b"], ["c"], ["d"], ["e"]]
    words4 = ["abc", "de", "ae"]
    print("Expected Output: ['abc', 'de'] | Actual Output:",
          solution.findWords(board4, words4))

    # Test case 5: Large board with overlapping words
    print("Test Case 5: Large board with multiple word paths")
    board5 = [
        ["t", "h", "i", "s"],
        ["w", "a", "t", "s"],
        ["o", "a", "h", "g"],
        ["f", "g", "d", "t"]
    ]
    words5 = ["this", "what", "fat", "dog"]
    print("Expected Output: ['this', 'what', 'fat', 'dog'] | Actual Output:",
          solution.findWords(board5, words5))

    # Test case 6: Edge case with max constraints
    print("Test Case 6: Large board (12x12) with complex word paths")
    board6 = [["a" for _ in range(12)] for _ in range(12)]
    words6 = ["a"*10, "a"*12, "aa"]
    print("Expected Output: Computed Output:",
          solution.findWords(board6, words6))

"""
Time Complexity:
- O(W * L + M * N * 4^L) → Trie insertion takes O(W * L), and DFS searches for each cell in the worst case 4^L.
- Space Complexity:
  - O(W * L) → Trie storage.
  - O(M * N) → Recursive DFS calls.
"""
