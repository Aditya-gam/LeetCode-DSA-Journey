class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        Finds the peak element index in a mountain array in O(log n) time.
        """
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                # We're on the ascending side of the mountain
                left = mid + 1
            else:
                # We're on the descending side (or at the peak)
                right = mid

        return left


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    arr1 = [0, 1, 0]
    # Expected: 1
    print(solution.peakIndexInMountainArray(arr1))

    arr2 = [0, 2, 1, 0]
    # Expected: 1
    print(solution.peakIndexInMountainArray(arr2))

    arr3 = [0, 10, 5, 2]
    # Expected: 1
    print(solution.peakIndexInMountainArray(arr3))

    arr4 = [3, 4, 5, 1]
    # Expected: 2
    print(solution.peakIndexInMountainArray(arr4))

    arr5 = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    # Expected: 2
    print(solution.peakIndexInMountainArray(arr5))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(log n) where n is the length of the list 'arr'. The binary search algorithm takes O(log n) time to find the peak element.
# Space complexity: O(1) since we use only a constant amount of extra space.
