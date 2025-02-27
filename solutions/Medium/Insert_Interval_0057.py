class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        merged = []
        i, n = 0, len(intervals)

        # Step 1: Add intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Step 2: Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        merged.append(newInterval)  # Insert merged interval

        # Step 3: Add remaining intervals
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged


# Example test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [
                           4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert solution.insert([], [5, 7]) == [[5, 7]]
    assert solution.insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert solution.insert([[1, 5]], [2, 7]) == [[1, 7]]
    assert solution.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    assert solution.insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]
    assert solution.insert([[1, 5]], [0, 1]) == [[0, 5]]
    assert solution.insert([[1, 5]], [0, 2]) == [[0, 5]]
    assert solution.insert([[1, 5]], [0, 3]) == [[0, 5]]
    assert solution.insert([[1, 5]], [0, 4]) == [[0, 5]]
    assert solution.insert([[1, 5]], [0, 5]) == [[0, 5]]
    assert solution.insert([[1, 5]], [0, 6]) == [[0, 6]]
    assert solution.insert([[1, 5]], [0, 7]) == [[0, 7]]
    assert solution.insert([[1, 5]], [0, 8]) == [[0, 8]]
    assert solution.insert([[1, 5]], [0, 9]) == [[0, 9]]
    assert solution.insert([[1, 5]], [0, 10]) == [[0, 10]]
    assert solution.insert([[1, 5]], [0, 11]) == [[0, 11]]
    assert solution.insert([[1, 5]], [0, 12]) == [[0, 12]]
    assert solution.insert([[1, 5]], [0, 13]) == [[0, 13]]

    print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of intervals in the intervals array. We iterate over the intervals array once.
# Space Complexity: O(N), where N is the number of intervals in the intervals array. We store the merged intervals in the result array.
