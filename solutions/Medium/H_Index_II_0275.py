class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int

        Returns the researcher's h-index in O(log n) time.
        citations is sorted in ascending order.
        """
        n = len(citations)
        left, right = 0, n

        while left < right:
            mid = (left + right + 1) // 2  # upper mid
            # we want to check if there are mid papers with >= mid citations
            # that means citations[n-mid] >= mid
            if citations[n - mid] >= mid:
                left = mid  # mid is feasible, try bigger
            else:
                right = mid - 1

        return left


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    citations1 = [0, 1, 3, 5, 6]
    # Expected: 3
    print(solution.hIndex(citations1))

    citations2 = [1, 2, 3, 4, 5]
    # Expected: 3
    print(solution.hIndex(citations2))

    citations3 = [0, 0, 0, 0, 0]
    # Expected: 0
    print(solution.hIndex(citations3))

    citations4 = [1, 1, 1, 1, 1]
    # Expected: 1
    print(solution.hIndex(citations4))

    citations5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Expected: 5
    print(solution.hIndex(citations5))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(log n) where n is the length of the list 'citations'. The binary search algorithm takes O(log n) time to find the h-index.
# Space complexity: O(1) since we use only a constant amount of extra space.
