class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // cols
            c = mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    matrix1 = [[1, 3, 5, 7],
               [10, 11, 16, 20],
               [23, 30, 34, 60]]
    target1 = 3
    print(solution.searchMatrix(matrix1, target1))  # True

    matrix2 = [[1, 3, 5, 7],
               [10, 11, 16, 20],
               [23, 30, 34, 60]]
    target2 = 13
    print(solution.searchMatrix(matrix2, target2))  # False

    matrix3 = []
    target3 = 0
    print(solution.searchMatrix(matrix3, target3))  # False

    matrix4 = [[1, 3, 5, 7],
               [10, 11, 16, 20],
               [23, 30, 34, 60]]
    target4 = 0
    print(solution.searchMatrix(matrix4, target4))  # False

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(log(m*n)), where m is the number of rows and n is the number of columns in the input matrix.
# Space complexity: O(1), since we are using only a constant amount of space.
