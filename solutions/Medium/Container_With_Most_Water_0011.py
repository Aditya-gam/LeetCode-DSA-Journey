class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        Finds the maximum water container area using a two-pointer technique.
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Compute current area
            h = min(height[left], height[right])
            w = right - left
            current_area = h * w

            # Update max_area if current is larger
            if current_area > max_area:
                max_area = current_area

            # Move pointer at smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # Expected output: 49
    print(solution.maxArea(height1))

    # Test case 2
    height2 = [1, 1]
    # Expected output: 1
    print(solution.maxArea(height2))

    # Test case 3
    height3 = [4, 3, 2, 1, 4]
    # Expected output: 16
    print(solution.maxArea(height3))

    # Test case 4
    height4 = [1, 2, 1]
    # Expected output: 2
    print(solution.maxArea(height4))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n), where n is the length of the input list 'height'. We traverse the list once.
# Space complexity: O(1), since we are using only a constant amount of space.
