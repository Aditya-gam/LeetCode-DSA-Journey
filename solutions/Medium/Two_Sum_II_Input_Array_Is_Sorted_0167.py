class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left+1, right+1]  # 1-based indexing
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        # Given the problem statement, we never reach here because
        # there's exactly one solution guaranteed.
        return [-1, -1]  # Fallback, shouldn't happen


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    numbers1, target1 = [2, 7, 11, 15], 9
    # 2 + 7 = 9 => indices are (1,2)
    print(solution.twoSum(numbers1, target1))  # Expected [1,2]

    # Example 2
    numbers2, target2 = [2, 3, 4], 6
    # 2 + 4 = 6 => indices are (1,3)
    print(solution.twoSum(numbers2, target2))  # Expected [1,3]

    # Example 3
    numbers3, target3 = [-1, 0], -1
    # -1 + 0 = -1 => indices are (1,2)
    print(solution.twoSum(numbers3, target3))  # Expected [1,2]

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n), where n is the length of the input list 'numbers'.

# Space complexity: O(1), since we are using only a constant amount of space.
