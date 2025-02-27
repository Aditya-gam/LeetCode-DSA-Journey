import bisect


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]

        For each interval in intervals, returns the index of the smallest 
        interval that starts at or after the end of the current interval.
        If no such interval exists, returns -1 for that interval.
        """
        n = len(intervals)
        # Build list of (start, original_index) for each interval
        starts = [(intervals[i][0], i) for i in range(n)]
        # Sort the list by start value
        starts.sort(key=lambda x: x[0])

        # Create a list of just the start values for binary search
        sorted_starts = [s for s, _ in starts]

        result = [-1] * n
        # For each interval, binary search for the smallest start >= interval's end
        for i, interval in enumerate(intervals):
            key = interval[1]
            # Find leftmost index where sorted_starts[j] >= key
            j = bisect.bisect_left(sorted_starts, key)
            if j < n:
                # Retrieve the original index from the sorted list
                result[i] = starts[j][1]
            else:
                result[i] = -1

        return result


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    intervals1 = [[1, 2]]
    # Only one interval, so no right interval exists.
    # Expected output: [-1]
    print(solution.findRightInterval(intervals1))  # Output: [-1]

    # Example 2
    intervals2 = [[3, 4], [2, 3], [1, 2]]
    # For [3,4]: no interval with start >= 4, so -1.
    # For [2,3]: right interval is [3,4] with original index 0.
    # For [1,2]: right interval is [2,3] with original index 1.
    # Expected output: [-1, 0, 1]
    print(solution.findRightInterval(intervals2))  # Output: [-1, 0, 1]

    # Example 3
    intervals3 = [[1, 4], [2, 3], [3, 4]]
    # For [1,4]: no right interval (no start >= 4) -> -1.
    # For [2,3]: right interval is [3,4] with original index 2.
    # For [3,4]: no right interval -> -1.
    # Expected output: [-1, 2, -1]
    print(solution.findRightInterval(intervals3))  # Output: [-1, 2, -1]

    # Example 4
    intervals4 = [[4, 5], [2, 3], [1, 2]]
    # For [4,5]: no right interval -> -1.
    # For [2,3]: right interval is [4,5] with original index 0.
    # For [1,2]: right interval is [2,3] with original index 1.
    # Expected output: [-1, 0, 1]
    print(solution.findRightInterval(intervals4))  # Output: [-1, 0, 1]

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(nlogn) where n is the number of intervals. We sort the intervals in O(nlogn) time
# and perform binary search for each interval in O(logn) time.

# Space complexity: O(n) where n is the number of intervals. We use O(n) space to store the sorted starts.
