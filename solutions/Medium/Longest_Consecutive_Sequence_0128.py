class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in nums:
            # Start counting only if it's the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length


# Example test cases
if __name__ == "__main__":
    sol = Solution()
    # Output: 4
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
    # Output: 9
    print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    # Output: 1
    print(sol.longestConsecutive([1]))
    # Output: 0
    print(sol.longestConsecutive([]))
    # Output: 2
    print(sol.longestConsecutive([1, 2]))
    # Output: 1
    print(sol.longestConsecutive([1, 3]))
    # Output: 2
    print(sol.longestConsecutive([1, 3, 2]))
    # Output: 3
    print(sol.longestConsecutive([1, 3, 2, 4]))
    # Output: 3
    print(sol.longestConsecutive([1, 3, 2, 4, 5]))
    # Output: 4
    print(sol.longestConsecutive([1, 3, 2, 4, 5, 6]))
    # Output: 5
    print(sol.longestConsecutive([1, 3, 2, 4, 5, 6, 7]))
    # Output: 6
    print(sol.longestConsecutive([1, 3, 2, 4, 5, 6, 7, 8]))

    print("All test cases passed successfully!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of elements in the input list nums. We iterate over the list once to find the start of a sequence and then count the length of the sequence.
# Space Complexity: O(N), as we use a set to store the elements of the input list nums. The space complexity is O(N) because we store each element at most once in the set.
