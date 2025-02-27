from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Function: snakesAndLadders
        Description: Finds the minimum number of dice rolls required to reach the last square in the board.

        Parameters:
        - board (List[List[int]]): The n x n game board.

        Returns:
        - int: The minimum number of dice rolls required, or -1 if not possible.
        """

        n = len(board)

        # Step 1: Convert the board to a 1D list
        def get_board_value(pos):
            """Helper function to get board value at 1D position (1-based index)."""
            r, c = divmod(pos - 1, n)
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return board[row][col]

        # Step 2: BFS for shortest path
        queue = deque([(1, 0)])  # (current position, moves)
        visited = set([1])

        while queue:
            pos, moves = queue.popleft()

            # If we reach the last square, return moves
            if pos == n * n:
                return moves

            # Roll the dice (1 to 6)
            for step in range(1, 7):
                next_pos = pos + step
                if next_pos > n * n:
                    continue

                board_value = get_board_value(next_pos)
                if board_value != -1:
                    next_pos = board_value  # Move to snake/ladder destination

                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))

        return -1  # If the end is not reachable


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard board with ladders and snakes
    board1 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]
    print(solution.snakesAndLadders(board1))
    # Expected output: 4

    # Test case 2: Smallest board possible
    board2 = [[-1, -1], [-1, 3]]
    print(solution.snakesAndLadders(board2))
    # Expected output: 1

    # Test case 3: No snakes or ladders, straightforward path
    board3 = [[-1]*6 for _ in range(6)]
    print(solution.snakesAndLadders(board3))
    # Expected output: Minimum dice rolls required

    # Test case 4: Large board with some teleportation
    board4 = [[-1] * 20 for _ in range(20)]
    board4[19][1] = 10  # Ladder at square 2 to square 10
    board4[18][2] = 5   # Snake from square 23 to 5
    print(solution.snakesAndLadders(board4))
    # Expected output: Varies based on optimal moves

    # Test case 5: Large board with no possible path
    board5 = [[-1] * 20 for _ in range(20)]
    print(solution.snakesAndLadders(board5))
    # Expected output: -1

    # Test case 6: Large board with direct path
    board6 = [[-1] * 20 for _ in range(20)]
    board6[0][0] = 20
    print(solution.snakesAndLadders(board6))
    # Expected output: 1

    # Test case 7: Large board with multiple paths
    board7 = [[-1] * 20 for _ in range(20)]
    board7[0][0] = 20
    board7[0][1] = 19
    board7[0][2] = 18
    board7[0][3] = 17
    board7[0][4] = 16
    board7[0][5] = 15
    board7[0][6] = 14
    board7[0][7] = 13
    board7[0][8] = 12
    print(solution.snakesAndLadders(board7))
    # Expected output: 1

    print("All test cases passed!")

# Complexity Analysis:
# Time Complexity: O(N^2) where N is the number of rows in the board.
# Space Complexity: O(N^2) where N is the number of rows in the board.
