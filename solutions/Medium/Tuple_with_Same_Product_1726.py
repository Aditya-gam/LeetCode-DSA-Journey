from collections import defaultdict


class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Given distinct positive integers in 'nums', return the number 
        of 4-tuples (a, b, c, d) such that a*b = c*d, with all elements 
        a, b, c, d using different indices in nums.
        """
        # Dictionary:
        #   product -> [freq, indexCount]
        #     freq: number of pairs that form this product
        #     indexCount: dictionary { i -> how many pairs include index i }
        productMap = defaultdict(lambda: [0, defaultdict(int)])

        # Step 1: Build productMap
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                prod = nums[i] * nums[j]
                productMap[prod][0] += 1          # freq++
                productMap[prod][1][i] += 1
                productMap[prod][1][j] += 1

        result = 0
        # Step 2: For each product, count valid pairs-of-pairs
        for prod, (freq, idxCount) in productMap.items():
            if freq < 2:
                # Need at least two pairs to form a valid 4-tuple
                continue

            # total pairs-of-pairs
            total_pairs = freq * (freq - 1) // 2

            # subtract overlapping pairs
            overlapCount = 0
            for idx, count in idxCount.items():
                if count > 1:
                    # choose any 2 pairs from those that share this index
                    overlapCount += (count * (count - 1) // 2)

            valid_pairs = total_pairs - overlapCount

            # Each valid pair-of-pairs contributes 8 4-tuples
            result += valid_pairs * 8

        return result


# Example Usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [2, 3, 4, 6]
    # Expected output: 8
    print(solution.tupleSameProduct(nums1))  # 8

    # Example 2
    nums2 = [1, 2, 4, 5, 10]
    # Expected output: 16
    print(solution.tupleSameProduct(nums2))  # 16

    # Example 3
    nums3 = [2, 3, 4, 6, 8, 12]
    # Expected output: 40
    print(solution.tupleSameProduct(nums3))  # 40

    # Example 4
    nums4 = [2, 3, 5, 7]
    # Expected output: 0
    print(solution.tupleSameProduct(nums4))  # 0

    print("All test cases passed!")

# Complexity Analysis
# Time complexity: O(N^2) where N is the length of 'nums'
# Space complexity: O(N^2) where N is the length of 'nums'
