class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int

        Computes the researcher's H-Index.
        """
        # Step 1: Sort in descending order
        citations.sort(reverse=True)

        # Step 2: Find the maximum h
        h_index = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h_index = i + 1
            else:
                break

        return h_index


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    citations1 = [3, 0, 6, 1, 5]
    # Sorted: [6, 5, 3, 1, 0]
    # i=0 => 6 >= 1 => h=1
    # i=1 => 5 >= 2 => h=2
    # i=2 => 3 >= 3 => h=3
    # i=3 => 1 >= 4 => no
    # Result: 3
    assert solution.hIndex(citations1) == 3  # Expected: 3

    # Test case 2
    citations2 = [1, 3, 1]
    # Sorted: [3, 1, 1]
    # i=0 => 3 >= 1 => h=1
    # i=1 => 1 >= 2 => no
    # Result: 1
    assert solution.hIndex(citations2) == 1  # Expected: 1

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(nlogn) - We sort the citations list
# Space complexity: O(1) - We use a constant amount of extra space
