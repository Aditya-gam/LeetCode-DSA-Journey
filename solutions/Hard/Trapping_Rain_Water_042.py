class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        Calculates how much water can be trapped between the bars
        defined by the 'height' array using a two-pointer approach.
        """
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1

        return water_trapped


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # Expected output: 6
    assert solution.trap(
        height1) == 6, f"Expected 6, got {solution.trap(height1)}"

    # Test case 2
    height2 = [4, 2, 0, 3, 2, 5]
    # Expected output: 9
    assert solution.trap(
        height2) == 9, f"Expected 9, got {solution.trap(height2)}"

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate over the height array once.
# Space complexity: O(1) - We use a constant amount of extra space.
