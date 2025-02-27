class Solution(object):
    def findMinArrowShots(self, points):
        """
        Returns the minimum number of arrows required to burst all balloons.

        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        # Sort balloons by their end position
        points.sort(key=lambda x: x[1])

        arrows = 1  # At least one arrow is needed
        last_shot = points[0][1]  # Shoot at the end of the first balloon

        for start, end in points:
            if start > last_shot:  # New balloon that does not overlap
                arrows += 1
                last_shot = end  # Update new shooting position

        return arrows


# Example test cases
if __name__ == "__main__":
    solution = Solution()
    # Test on the example in the problem statement
    assert solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    # Additional test cases
    assert solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert solution.findMinArrowShots([[1, 2], [1, 2], [1, 2], [1, 5]]) == 1
    assert solution.findMinArrowShots([[1, 2], [1, 2], [1, 2], [1, 6]]) == 1
    assert solution.findMinArrowShots([[1, 2], [1, 2], [1, 2], [1, 16]]) == 1

    print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(N * log(N)), where N is the number of balloons. We sort the balloons based on their end positions.
# Space Complexity: O(1), since we are using a constant amount of space.
