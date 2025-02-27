class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        n = len(nums)
        # Total pairs (i, j) with i < j
        total_pairs = n*(n-1)//2

        freq = defaultdict(int)  # maps (i - nums[i]) -> count
        for i, val in enumerate(nums):
            key = i - val
            freq[key] += 1

        # Count how many good pairs exist
        good_pairs = 0
        for k, count in freq.items():
            if count > 1:
                good_pairs += count*(count - 1)//2

        # Bad pairs = total_pairs - good_pairs
        return total_pairs - good_pairs


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    nums1 = [4, 1, 3, 3]
    # Expected output: 5
    print(solution.countBadPairs(nums1))  # 5

    nums2 = [1, 2, 3, 4, 5]
    # Expected output: 0 (no bad pairs)
    print(solution.countBadPairs(nums2))  # 0

    nums3 = [1, 1, 1, 1]
    # Expected output: 6
    print(solution.countBadPairs(nums3))  # 6

    nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Expected output: 0 (no bad pairs)
    print(solution.countBadPairs(nums4))  # 0

    nums5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Expected output: 20
    print(solution.countBadPairs(nums5))  # 20


# Complexity analysis
# Time complexity: O(n), where n is the length of the input list 'nums'.
# Space complexity: O(n), for the frequency dictionary 'freq'.
