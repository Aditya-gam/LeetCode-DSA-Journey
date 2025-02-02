class Solution(object):
    def findMinArrowShots(self, points):
        """
        Returns the minimum number of arrows required to burst all balloons.

        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        # 1. Sort balloons by their x_end
        points.sort(key=lambda x: x[1])

        arrows = 0
        current_end = float('-inf')

        for balloon in points:
            start, end = balloon
            # 2. If this balloon is not covered by the last arrow
            if start > current_end:
                # Place a new arrow at balloon's end
                arrows += 1
                current_end = end

        return arrows

# Example test cases


def test_findMinArrowShots():
    sol = Solution()

    # Test case 1
    # Balloons: [[10,16],[2,8],[1,6],[7,12]]
    # Arrows needed: 2
    # Explanation:
    # 1. Arrow at x=8: Bursts [2,8], [1,6]
    # 2. Arrow at x=16: Bursts [10,16], [7,12]
    assert sol.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2

    # Test case 2
    # Balloons: [[1,2],[3,4],[5,6],[7,8]]
    # Arrows needed: 4
    # Explanation:
    # Each balloon is separate, so need 1 arrow per balloon
    assert sol.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4

    # Test case 3
    # Balloons: [[1,2],[2,3],[3,4],[4,5]]
    # Arrows needed: 2
    # Explanation:
    # 1. Arrow at x=2: Bursts [1,2], [2,3]
    # 2. Arrow at x=4: Bursts [3,4], [4,5]
    assert sol.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2

    # Test case 4
    # Balloons: [[1,2]]
    # Arrows needed: 1
    # Explanation:
    # Only one balloon, need 1 arrow
    assert sol.findMinArrowShots([[1, 2]]) == 1

    # Test case 5
    # Balloons: []
    # Arrows needed: 0
    # Explanation:
    # No balloons to burst
    assert sol.findMinArrowShots([]) == 0

    print("All test cases pass")


test_findMinArrowShots()

# Complexity Analysis
# Time Complexity: O(nlogn) where n is the number of balloons.
# We sort the balloons by their end points.

# Space Complexity: O(1) since we use a constant amount of space.
