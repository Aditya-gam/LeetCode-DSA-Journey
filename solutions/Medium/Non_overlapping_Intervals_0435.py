class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        Returns the minimum number of intervals to remove so that
        no two intervals overlap.

        :param intervals: List[List[int]]
        :rtype: int
        """
        # Edge case: if there's 0 or 1 interval, no need to remove anything
        if len(intervals) <= 1:
            return 0

        # 1. Sort by end time
        intervals.sort(key=lambda x: x[1])

        # 2. Iterate and count how many intervals we can keep without overlapping
        count_non_overlap = 0
        end = float('-inf')

        for interval in intervals:
            start, finish = interval
            # If the current interval doesn't overlap with the chosen intervals
            if start >= end:
                count_non_overlap += 1
                end = finish  # Update the end to the current interval's end

        # 3. Minimum to remove = total intervals - number of intervals we can keep
        return len(intervals) - count_non_overlap

# Example test cases


def test_eraseOverlapIntervals():
    sol = Solution()

    # Test case 1 (from the example)
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    # Remove [1,3], keep the rest
    # Overlapping pairs if [1,3] not removed:
    #   [1,3] and [1,2], [1,3] and [2,3], [1,3] and [3,4] (3 overlaps)
    # By removing [1,3], no overlaps remain.
    # Expected: 1
    assert sol.eraseOverlapIntervals(intervals) == 1

    # Test case 2 (from the example)
    intervals = [[1, 2], [1, 2], [1, 2]]
    # Three intervals all the same => we can only keep one
    # Need to remove 2
    # Expected: 2
    assert sol.eraseOverlapIntervals(intervals) == 2

    # Test case 3 (from the example)
    intervals = [[1, 2], [2, 3]]
    # [1,2] and [2,3] do not overlap as per problem statement (touching boundary is allowed)
    # Expected: 0
    assert sol.eraseOverlapIntervals(intervals) == 0

    # Additional test: intervals that are already non-overlapping
    intervals = [[0, 1], [1, 2], [2, 3], [3, 4]]
    # All intervals are non-overlapping
    # Expected: 0
    assert sol.eraseOverlapIntervals(intervals) == 0

    # Additional test: intervals all overlap heavily
    intervals = [[1, 5], [2, 5], [3, 5], [4, 5]]
    # Sort by end time -> [[1,5],[2,5],[3,5],[4,5]]
    # We can keep only one interval (e.g., [1,5])
    # So we remove 3
    # Expected: 3
    assert sol.eraseOverlapIntervals(intervals) == 3

    # Additional test: random
    intervals = [[-1, 2], [2, 5], [0, 2], [2, 3]]
    # Sort by end -> [[0,2], [-1,2], [2,3], [2,5]]
    # Keep [0,2] -> end = 2
    # Next [-1,2] overlaps (start=-1 < end=2), skip
    # Next [2,3] doesn't overlap (start=2 >= end=2) -> keep -> end=3
    # Next [2,5] overlaps (start=2 < end=3), skip
    # Kept 2 intervals => remove 2 out of 4
    # Expected: 2
    assert sol.eraseOverlapIntervals(intervals) == 2

    print("All test cases passed!")


test_eraseOverlapIntervals()

# Complexity Analysis
# Time Complexity: O(nlogn) where n is the number of intervals.
# We sort the intervals by end time, which takes O(nlogn) time.
# Then, we iterate through the intervals once, which takes O(n) time.

# Space Complexity: O(1) since we use only a constant amount of space.
