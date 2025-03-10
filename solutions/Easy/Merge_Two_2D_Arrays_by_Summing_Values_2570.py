from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        Function: mergeArrays
        Description: Merges two sorted 2D arrays by summing values of matching IDs.

        Parameters:
        - nums1 (List[List[int]]): First sorted 2D array with unique IDs.
        - nums2 (List[List[int]]): Second sorted 2D array with unique IDs.

        Returns:
        - List[List[int]]: The merged and sorted 2D array.
        """

        merged = {}

        # Step 1: Add values from nums1
        for key, val in nums1:
            merged[key] = val

        # Step 2: Add values from nums2, summing if key already exists
        for key, val in nums2:
            if key in merged:
                merged[key] += val
            else:
                merged[key] = val

        # Step 3: Convert dictionary back to sorted list
        result = sorted([[key, val] for key, val in merged.items()])

        return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Some common IDs
    nums1 = [[1, 2], [2, 3], [4, 5]]
    nums2 = [[1, 4], [3, 2], [4, 1]]
    print("Test Case 1:", solution.mergeArrays(nums1, nums2))
    # Expected Output: [[1,6],[2,3],[3,2],[4,6]]

    # Test Case 2: No common IDs
    nums1 = [[2, 4], [3, 6], [5, 5]]
    nums2 = [[1, 3], [4, 3]]
    print("Test Case 2:", solution.mergeArrays(nums1, nums2))
    # Expected Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]

    # Test Case 3: One empty array
    nums1 = [[1, 2], [2, 3]]
    nums2 = []
    print("Test Case 3:", solution.mergeArrays(nums1, nums2))
    # Expected Output: [[1,2],[2,3]]

    # Test Case 4: Identical arrays
    nums1 = [[1, 5], [2, 10], [3, 15]]
    nums2 = [[1, 5], [2, 10], [3, 15]]
    print("Test Case 4:", solution.mergeArrays(nums1, nums2))
    # Expected Output: [[1,10],[2,20],[3,30]]

    # Test Case 5: Large numbers
    nums1 = [[1, 1000], [2, 500]]
    nums2 = [[2, 500], [3, 1000]]
    print("Test Case 5:", solution.mergeArrays(nums1, nums2))
    # Expected Output: [[1,1000],[2,1000],[3,1000]]

    # Test Case 6: IDs in reverse order
    nums1 = [[5, 50], [10, 100]]
    nums2 = [[1, 10], [5, 50]]
    print("Test Case 6:", solution.mergeArrays(nums1, nums2))
    # Expected Output: [[1,10],[5,100],[10,100]]

"""
Time Complexity:
- O(n + m) for inserting elements into the dictionary.
- O(n log n) for sorting (but since we're sorting by keys, it's usually very fast).
- Total: O(n + m) in practical cases.

Space Complexity:
- O(n + m) for storing results in a dictionary.
- Total: O(n + m).
"""
