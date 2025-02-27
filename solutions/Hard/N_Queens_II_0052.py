class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Function: totalNQueens
        Description: Computes the number of distinct solutions for placing N queens on an N×N chessboard.

        Parameters:
        - n (int): Size of the chessboard.

        Returns:
        - int: Number of distinct solutions.
        """
        def backtrack(row, columns, diagonals1, diagonals2):
            # Base Case: All queens are placed successfully
            if row == n:
                return 1

            count = 0
            for col in range(n):
                diag1 = row - col  # Major diagonal
                diag2 = row + col  # Minor diagonal

                if col in columns or diag1 in diagonals1 or diag2 in diagonals2:
                    continue  # Skip unsafe positions

                # Place the queen
                columns.add(col)
                diagonals1.add(diag1)
                diagonals2.add(diag2)

                # Recur to the next row
                count += backtrack(row + 1, columns, diagonals1, diagonals2)

                # Backtrack: Remove the queen
                columns.remove(col)
                diagonals1.remove(diag1)
                diagonals2.remove(diag2)

            return count

        return backtrack(0, set(), set(), set())


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Smallest case with n = 1
    print("Test Case 1: n = 1")
    print("Expected Output: 1 | Actual Output:", solution.totalNQueens(1))

    # Test Case 2: Standard 4-Queens problem
    print("Test Case 2: n = 4")
    print("Expected Output: 2 | Actual Output:", solution.totalNQueens(4))

    # Test Case 3: 5-Queens problem
    print("Test Case 3: n = 5")
    print("Expected Output: 10 | Actual Output:", solution.totalNQueens(5))

    # Test Case 4: 6-Queens problem
    print("Test Case 4: n = 6")
    print("Expected Output: 4 | Actual Output:", solution.totalNQueens(6))

    # Test Case 5: Larger chessboard (7-Queens)
    print("Test Case 5: n = 7")
    print("Expected Output: 40 | Actual Output:", solution.totalNQueens(7))

    # Test Case 6: Edge case (9-Queens, max constraint)
    print("Test Case 6: n = 9")
    print("Expected Output: 352 | Actual Output:", solution.totalNQueens(9))

"""
Time Complexity:
- O(N!) → Worst-case scenario where each queen placement recursively tries all possibilities.

Space Complexity:
- O(N) → For recursive call stack and sets tracking queen placements.
"""
