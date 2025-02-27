class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        This function removes duplicates from a sorted array such that 
        each distinct element can appear at most twice. It returns the 
        length k of the modified array that satisfies this condition.
        """
        place = 0  # Pointer to place the next valid element

        for i in range(len(nums)):
            # If place < 2, we can add the element without checking
            if place < 2:
                nums[place] = nums[i]
                place += 1
            else:
                # Only place if this doesn't create a triplicate
                if nums[i] != nums[place - 2]:
                    nums[place] = nums[i]
                    place += 1

        return place


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = solution.removeDuplicates(nums1)
    assert k1 == 5  # Expected: 5
    # The first 5 elements of nums1 should be [1,1,2,2,3]
    assert nums1[:k1] == [1, 1, 2, 2, 3]

    # Test case 2
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k2 = solution.removeDuplicates(nums2)
    assert k2 == 7  # Expected: 7
    # The first 7 elements of nums2 should be [0,0,1,1,2,3,3]
    assert nums2[:k2] == [0, 0, 1, 1, 2, 3, 3]

    print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(n), where n is the length of nums.
# Space Complexity: O(1).
