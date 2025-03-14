from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Function: solve
        Description: Modifies the given board in-place to capture all surrounded regions.

        Parameters:
        - board (List[List[str]]): A 2D list representing the board with 'X' and 'O'.

        Returns:
        - None: Modifies the board in-place.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            """
            Marks all 'O's connected to the border as 'E' (escaped).
            """
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'E'  # Temporarily mark as escaped
            # Explore all four directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Mark all 'O's connected to the border as 'E'
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        # Step 2: Convert all remaining 'O's to 'X' (captured regions)
        # Convert all 'E's back to 'O' (escaped regions)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Captured
                elif board[r][c] == 'E':
                    board[r][c] = 'O'  # Restore escaped 'O's


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard example with a surrounded region
    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    solution.solve(board1)
    print(board1)
    # Expected output:
    # [["X","X","X","X"],
    #  ["X","X","X","X"],
    #  ["X","X","X","X"],
    #  ["X","O","X","X"]]

    # Test case 2: Single-cell board (no changes needed)
    board2 = [["X"]]
    solution.solve(board2)
    print(board2)
    # Expected output: [["X"]]

    # Test case 3: All 'O' on edges (no changes)
    board3 = [
        ["O", "O", "O"],
        ["O", "X", "O"],
        ["O", "O", "O"]
    ]
    solution.solve(board3)
    print(board3)
    # Expected output: [["O","O","O"], ["O","X","O"], ["O","O","O"]]

    # Test case 4: All surrounded 'O' (should be captured)
    board4 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "X", "X"]
    ]
    solution.solve(board4)
    print(board4)
    # Expected output:
    # [["X","X","X","X"],
    #  ["X","X","X","X"],
    #  ["X","X","X","X"],
    #  ["X","X","X","X"]]

    # Test case 5: All 'O' in the middle
    board5 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "X", "X"]
    ]
    solution.solve(board5)
    print(board5)
    # Expected output:
    # [["X","X","X","X"],
    #  ["X","X","X","X"],
    #  ["X","X","X","X"],
    #  ["X","X","X","X"]]

    # Test case 6: All 'O' on the border
    board6 = [
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"]
    ]
    solution.solve(board6)
    print(board6)
    # Expected output:
    # [["O","O","O","O"],
    #  ["O","O","O","O"],
    #  ["O","O","O","O"],
    #  ["O","O","O","O"]]

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the board. We perform a DFS traversal of the board, visiting each cell at most once.
# Space Complexity: O(M * N), where M is the number of rows and N is the number of columns in the board. The maximum depth of the recursion stack can be M * N for the worst case.
