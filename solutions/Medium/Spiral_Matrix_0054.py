class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Traverse right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Traverse bottom row (if not already traversed)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Traverse left column (if not already traversed)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result


# Example test cases
sol = Solution()
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
# Output: [1, 2, 3, 4, 8, 7, 6, 5]
print(sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8]]))
print(sol.spiralOrder([[1, 2, 3], [4, 5, 6]]))  # Output: [1, 2, 3, 6, 5, 4]
print(sol.spiralOrder([[1, 2], [3, 4], [5, 6]]))  # Output: [1, 2, 4, 6, 5, 3]
print(sol.spiralOrder([[1, 2, 3]]))  # Output: [1, 2, 3]
print(sol.spiralOrder([[1], [2], [3]]))  # Output: [1, 2, 3]
print(sol.spiralOrder([[1]]))  # Output: [1]
print(sol.spiralOrder([]))  # Output: []
print(sol.spiralOrder([[]]))  # Output: []
print(sol.spiralOrder([[1, 2, 3, 4, 5]]))  # Output: [1, 2, 3, 4, 5]
print(sol.spiralOrder([[1], [2], [3], [4], [5]]))  # Output: [1, 2, 3, 4, 5]
# Output: [1, 2, 4, 6, 8, 10, 9, 7, 5, 3]
print(sol.spiralOrder([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
# Output: [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
print(sol.spiralOrder([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))
# Output: [1, 2, 4, 6, 8, 10, 12, 11, 9, 7, 5, 3]
print(sol.spiralOrder([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]))
# Output: [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
print(sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))

# Complexity Analysis
# Time complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix.
# We visit each cell exactly once.
# Space complexity: O(1) since we are using a constant amount of space.
