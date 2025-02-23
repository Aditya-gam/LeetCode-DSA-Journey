class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int

        Returns the minimum number of candies needed to distribute
        such that the rating conditions are satisfied.
        """
        n = len(ratings)
        if n == 1:
            return 1

        candies = [1] * n

        # Left-to-right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right-to-left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    ratings1 = [1, 0, 2]
    # Explanation:
    #   - Child 0 has rating=1
    #   - Child 1 has rating=0
    #   - Child 2 has rating=2
    #   Assign candies -> [2,1,2] => total = 5
    assert solution.candy(ratings1) == 5  # Expected: 5

    # Test case 2
    ratings2 = [1, 2, 2]
    # Explanation:
    #   - Child 0 has rating=1
    #   - Child 1 has rating=2
    #   - Child 2 has rating=2
    #   Assign candies -> [1,2,1], total = 4
    assert solution.candy(ratings2) == 4  # Expected: 4

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate over the ratings array twice.
# Space complexity: O(n) - We use an extra array of size n to store the candies.
