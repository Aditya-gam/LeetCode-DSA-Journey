class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        result = []
        start = nums[0]  # Start of the current range

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                # Close the previous range
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(nums[i - 1]))
                # Start a new range
                start = nums[i]

        # Add the last processed range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(nums[-1]))

        return result


# Example test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]) == [
        "0", "2->4", "6", "8->9"]
    assert solution.summaryRanges([]) == []
    assert solution.summaryRanges([-1]) == ["-1"]
    assert solution.summaryRanges([0]) == ["0"]
    assert solution.summaryRanges([0, 1, 2, 3, 4, 5]) == ["0->5"]
    assert solution.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10]) == [
        "0->5", "7->10"]
    assert solution.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 12]) == [
        "0->5", "7->10", "12"]
    assert solution.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15]) == [
        "0->5", "7->10", "12->15"]
    assert solution.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 17]) == [
        "0->5", "7->10", "12->15", "17"]
    assert solution.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19, 20]) == [
        "0->5", "7->10", "12->15", "17->20"]
    assert solution.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19, 20, 22]) == [
        "0->5", "7->10", "12->15", "17->20", "22"]

    print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(N), where N is the length of the nums array. We iterate over the nums array once.
# Space Complexity: O(1), since we are using a constant amount of space.
