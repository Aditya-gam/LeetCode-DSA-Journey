class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        Find the number of days to wait for a warmer temperature.

        :param temperatures: List[int] - Array of daily temperatures
        :return: List[int] - Days to wait for warmer temperatures
        """
        stack = []  # Stack to store indices of temperatures
        answer = [0] * len(temperatures)  # Initialize result array with 0s

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index  # Calculate days to wait
            stack.append(i)  # Push current index to stack

        return answer


# Example test cases
sol = Solution()
# Output: [1, 1, 4, 2, 1, 1, 0, 0]
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(sol.dailyTemperatures([30, 40, 50, 60])
      )                 # Output: [1, 1, 1, 0]
# Output: [1, 1, 0]
print(sol.dailyTemperatures([30, 60, 90]))
print(sol.dailyTemperatures([30, 30, 30, 30])
      )                 # Output: [0, 0, 0, 0]
print(sol.dailyTemperatures([30, 30, 60, 30])
      )                 # Output: [2, 1, 0, 0]
print(sol.dailyTemperatures([30, 60, 30, 30])
      )                 # Output: [1, 1, 0, 0]

# Complexity Analysis
# Time Complexity: O(n)
# We iterate through the array once, making this a linear time solution.

# Space Complexity: O(n)
# We use a stack to store indices of temperatures, which can contain up to n elements.
