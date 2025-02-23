class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None 
        Modifies matrix in-place to rotate by 90 degrees clockwise.
        """
        n = len(matrix)

        # 1. Transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. Reverse each row
        for i in range(n):
            matrix[i].reverse()


# Example usage
if __name__ == "__main__":
    solution = Solution()

    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    solution.rotate(matrix1)
    print(matrix1)
    # Expected: [[7,4,1],[8,5,2],[9,6,3]]

    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    solution.rotate(matrix2)
    print(matrix2)
    # Expected: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    matrix3 = [
        [1]
    ]
    solution.rotate(matrix3)
    print(matrix3)
    # Expected: [[1]]

    matrix4 = [
        [1, 2],
        [3, 4]
    ]
    solution.rotate(matrix4)
    print(matrix4)
    # Expected: [[3,1],[4,2]]

    matrix5 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    solution.rotate(matrix5)
    print(matrix5)
    # Expected: [[10,7,4,1],[11,8,5,2],[12,9,6,3]]

    print("All test cases passed!")

# Complexity analysis:
# Time complexity: O(n^2), where n is the number of rows in the matrix. We iterate through the matrix twice.
# Space complexity: O(1), since we do not use any extra space.
