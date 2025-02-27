class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Step 1: Sort intervals based on start times
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize merged list
        merged = [intervals[0]]  # Add the first interval

        # Step 3: Iterate through intervals
        for i in range(1, len(intervals)):
            prev = merged[-1]
            curr = intervals[i]

            # Check if overlapping
            if prev[1] >= curr[0]:
                # Merge by updating the last interval's end time
                prev[1] = max(prev[1], curr[1])
            else:
                # No overlap, add to result
                merged.append(curr)

        return merged


# Example test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6], [8, 10], [15, 18]]
    assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert solution.merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert solution.merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert solution.merge([[1, 4], [0, 1]]) == [[0, 4]]
    assert solution.merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]]
    assert solution.merge([[1, 4], [0, 0], [0, 0]]) == [[0, 0], [0, 0], [1, 4]]
    assert solution.merge([[1, 4], [0, 0], [0, 0], [0, 0]]) == [
        [0, 0], [0, 0], [0, 0], [1, 4]]
    assert solution.merge([[1, 4], [0, 0], [0, 0], [0, 0], [0, 0]]) == [
        [0, 0], [0, 0], [0, 0], [0, 0], [1, 4]]
    assert solution.merge([[1, 4], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]) == [
        [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 4]]
    assert solution.merge([[1, 4, 5], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]) == [
        [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 4, 5]]

    print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(N * log(N)), where N is the length of the intervals array. We sort the intervals array based on the start times.
# Space Complexity: O(N), where N is the length of the intervals array. We store the merged intervals in the result array.
