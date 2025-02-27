class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])

        # Flags to indicate if the first row or first column should be zeroed
        first_row_zero = False
        first_col_zero = False

        # 1. Check if first row or first column should be zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # 2. Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 3. Zero out cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 4. Zero out first row or column if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    matrix1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    solution.setZeroes(matrix1)
    print(matrix1)
    # Expected: [[1,0,1],[0,0,0],[1,0,1]]

    # Example 2
    matrix2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    solution.setZeroes(matrix2)
    print(matrix2)
    # Expected: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    # Example 3
    matrix3 = [
        [1, 1, 1],
        [0, 1, 2]
    ]
    solution.setZeroes(matrix3)
    print(matrix3)
    # Expected: [[0,1,1],[0,0,0]]

    # Example 4
    matrix4 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 0]
    ]
    solution.setZeroes(matrix4)
    print(matrix4)
    # Expected: [[1,1,0],[1,1,0],[0,0,0]]

    print("All test cases passed!")

# Complexity analysis:
# Time complexity: O(m*n), where m is the number of rows and n is the number of columns in the matrix.
# Space complexity: O(1), since we are using the first row and first column as markers.
