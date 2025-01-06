class Solution(object):
    def minOperations(self, boxes):
        """
        Calculate minimum operations to move all balls to each box.

        :param boxes: str - Binary string representing boxes with balls
        :return: List[int] - Minimum number of operations for each box
        """
        n = len(boxes)
        answer = [0] * n

        # Left to right pass
        count = 0  # Number of balls seen so far
        operations = 0  # Total operations for current pass
        for i in range(n):
            answer[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count

        # Right to left pass
        count = 0
        operations = 0
        for i in range(n - 1, -1, -1):
            answer[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count

        return answer


# Example test cases
sol = Solution()
print(sol.minOperations("110"))      # Output: [1, 1, 3]
print(sol.minOperations("001011"))   # Output: [11, 8, 5, 4, 3, 4]
