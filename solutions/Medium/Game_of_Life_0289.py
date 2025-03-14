class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None
        Modifies the board in-place to the next state of Game of Life.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def count_live_neighbors(r, c):
            live_count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        # If original state was live => abs(board[nr][nc]) == 1
                        if abs(board[nr][nc]) == 1:
                            live_count += 1
            return live_count

        # 1. Mark transitions using in-place encoding:
        #    1 -> 0 => -1
        #    0 -> 1 => 2
        for i in range(m):
            for j in range(n):
                ln = count_live_neighbors(i, j)

                if board[i][j] == 1:  # cell is currently live
                    if ln < 2 or ln > 3:
                        board[i][j] = -1  # live -> dead
                else:  # cell is currently dead
                    if ln == 3:
                        board[i][j] = 2   # dead -> live

        # 2. Finalize: -1 => 0, 2 => 1
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    board1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    # Expected: [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    solution.gameOfLife(board1)
    print(board1)

    board2 = [[1, 1], [1, 0]]
    # Expected: [[1, 1], [1, 1]]
    solution.gameOfLife(board2)
    print(board2)

    board3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # Expected: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    solution.gameOfLife(board3)

    board4 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    # Expected: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    solution.gameOfLife(board4)

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(m * n) where m is the number of rows and n is the number of columns in the board
# Space complexity: O(1) since we are modifying the board in-place
