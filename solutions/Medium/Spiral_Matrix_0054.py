class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        res = []

        while left <= right and top <= bottom:
            # Traverse from left to right across the top row
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # Traverse downward along the right column
            if top <= bottom:
                for row in range(top, bottom + 1):
                    res.append(matrix[row][right])
                right -= 1

            # Traverse from right to left across the bottom row
            if left <= right and top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # Traverse upward along the left column
            if top <= bottom and left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Expected: [1,2,3,6,9,8,7,4,5]
    print(solution.spiralOrder(matrix1))

    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # Expected: [1,2,3,4,8,12,11,10,9,5,6,7]
    print(solution.spiralOrder(matrix2))

    # Output: [1, 2, 3, 4, 8, 7, 6, 5]
    print(solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8]]))
    # Output: [1, 2, 3, 6, 5, 4]
    print(solution.spiralOrder([[1, 2, 3], [4, 5, 6]]))
    # Output: [1, 2, 4, 6, 5, 3]
    print(solution.spiralOrder([[1, 2], [3, 4], [5, 6]]))
    print(solution.spiralOrder([[1, 2, 3]]))  # Output: [1, 2, 3]
    print(solution.spiralOrder([[1], [2], [3]]))  # Output: [1, 2, 3]
    print(solution.spiralOrder([[1]]))  # Output: [1]
    print(solution.spiralOrder([]))  # Output: []
    print(solution.spiralOrder([[]]))  # Output: []
    print(solution.spiralOrder([[1, 2, 3, 4, 5]]))  # Output: [1, 2, 3, 4, 5]
    # Output: [1, 2, 3, 4, 5]
    print(solution.spiralOrder([[1], [2], [3], [4], [5]]))
    # Output: [1, 2, 4, 6, 8, 10, 9, 7, 5, 3]
    print(solution.spiralOrder([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
    # Output: [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
    print(solution.spiralOrder([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))
    # Output: [1, 2, 4, 6, 8, 10, 12, 11, 9, 7, 5, 3]
    print(solution.spiralOrder(
        [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]))
    # Output: [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
    print(solution.spiralOrder(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))

# Complexity Analysis
# Time complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix.
# We visit each cell exactly once.
# Space complexity: O(1) since we are using a constant amount of space.
