from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Function: exist
        Description: Checks if the given word exists in the board by searching adjacent cells.

        Parameters:
        - board (List[List[str]]): 2D grid of characters.
        - word (str): Word to search in the grid.

        Returns:
        - bool: True if the word exists, otherwise False.
        """

        # Board dimensions
        rows, cols = len(board), len(board[0])

        # DFS function for backtracking
        def dfs(r, c, index):
            # If all characters in word matched, return True
            if index == len(word):
                return True

            # Out of bounds or character mismatch or already visited
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]):
                return False

            # Mark as visited
            temp, board[r][c] = board[r][c], "#"

            # Explore 4 directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))

            # Restore original state
            board[r][c] = temp

            return found

        # Start DFS from every cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic match from top-left
    board1 = [["A", "B", "C", "E"],
              ["S", "F", "C", "S"],
              ["A", "D", "E", "E"]]
    word1 = "ABCCED"
    print("Test Case 1:", solution.exist(
        board1, word1))  # Expected Output: True

    # Test Case 2: Word found in different order
    word2 = "SEE"
    print("Test Case 2:", solution.exist(
        board1, word2))  # Expected Output: True

    # Test Case 3: Word cannot be formed due to repetition constraint
    word3 = "ABCB"
    # Expected Output: False
    print("Test Case 3:", solution.exist(board1, word3))

    # Test Case 4: Single letter match
    board4 = [["A"]]
    word4 = "A"
    print("Test Case 4:", solution.exist(
        board4, word4))  # Expected Output: True

    # Test Case 5: Single row board
    board5 = [["A", "B", "C", "D"]]
    word5 = "BCD"
    print("Test Case 5:", solution.exist(
        board5, word5))  # Expected Output: True

    # Test Case 6: Larger board, no match
    board6 = [["A", "B", "C", "D"],
              ["E", "F", "G", "H"],
              ["I", "J", "K", "L"],
              ["M", "N", "O", "P"]]
    word6 = "XYZ"
    # Expected Output: False
    print("Test Case 6:", solution.exist(board6, word6))

"""
Time Complexity:
- O(m * n * 4^k) in the worst case where k is the length of the word.
- Each cell is visited once and explores up to 4 directions.

Space Complexity:
- O(k) due to recursion depth (maximum word length).
"""
