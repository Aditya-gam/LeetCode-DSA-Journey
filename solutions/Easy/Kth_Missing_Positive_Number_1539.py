class Solution(object):
    def findKthPositiveBinary(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int

        Uses binary search in O(log n) to find the kth missing positive integer.
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            # missing(mid) = arr[mid] - (mid+1)
            missing_count = arr[mid] - (mid + 1)

            if missing_count < k:
                left = mid + 1
            else:
                right = mid - 1

        # If all elements have missing_count < k, then left = len(arr)
        # The kth missing is beyond arr's last element
        # left is also the number of elements of arr that are strictly less than that position
        # So the answer is k + left
        # Explanation:
        #  - 'left' is how many numbers from arr are placed before we found the required missing
        #  - For every position i in arr, missing(i) = arr[i] - (i+1).
        #    When left = len(arr), it implies we used all arr elements but still want more missing
        # So the result is simply k + left

        return k + left

    def findKthPositiveLinear(self, arr, k):
        """
        O(n) approach: track missing count as we go.
        """
        missCount = 0
        current = 1
        idx = 0
        n = len(arr)

        while missCount < k and idx < n:
            if arr[idx] == current:
                idx += 1
            else:
                # current is missing from arr
                missCount += 1
                if missCount == k:
                    return current
            current += 1

        # If we used up arr but haven't found k-th missing yet
        # We continue from current onwards
        if missCount < k:
            return current + (k - missCount) - 1

        # Should not reach here logically
        return -1


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    arr1 = [2, 3, 4, 7, 11]
    k1 = 5
    print(solution.findKthPositiveBinary(arr1, k1))  # Expected: 9
    print(solution.findKthPositiveLinear(arr1, k1))  # Expected: 9

    # Example 2
    arr2 = [1, 2, 3, 4]
    k2 = 2
    print(solution.findKthPositiveBinary(arr2, k2))  # Expected: 6
    print(solution.findKthPositiveLinear(arr2, k2))  # Expected: 6

    # Example 3
    arr3 = [1, 3, 5, 7, 9]
    k3 = 2
    print(solution.findKthPositiveBinary(arr3, k3))  # Expected: 2
    print(solution.findKthPositiveLinear(arr3, k3))  # Expected: 2

    # Example 4
    arr4 = [1, 2, 3, 4]
    k4 = 2
    print(solution.findKthPositiveBinary(arr4, k4))  # Expected: 6
    print(solution.findKthPositiveLinear(arr4, k4))  # Expected: 6

    # Example 5
    arr5 = [1, 2, 4]
    k5 = 3
    print(solution.findKthPositiveBinary(arr5, k5))  # Expected: 5
    print(solution.findKthPositiveLinear(arr5, k5))  # Expected: 5

    print("All test cases passed!")

# Complexity analysis:
# Time complexity: O(log n) for binary search, O(n) for linear search.
# Space complexity: O(1) since we use only a constant amount of space.
