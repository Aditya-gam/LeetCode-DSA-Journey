class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str

        Uses binary search to find the smallest character in 'letters'
        which is strictly greater than 'target'. If none is found, 
        returns the first character.
        """
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            # If letters[mid] <= target, we look to the right half
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        # 'left' is now the insertion position.
        # If left == len(letters), it means all letters are <= target.
        # So we wrap around and return letters[0].
        return letters[left % len(letters)]


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    letters1 = ["c", "f", "j"]
    target1 = "a"
    # The next greatest letter after 'a' is 'c'
    assert solution.nextGreatestLetter(letters1, target1) == "c"

    # Test case 2
    letters2 = ["c", "f", "j"]
    target2 = "c"
    # The next greatest letter after 'c' is 'f'
    assert solution.nextGreatestLetter(letters2, target2) == "f"

    # Test case 3
    letters3 = ["x", "x", "y", "y"]
    target3 = "z"
    # All letters are <= 'z', so wrap around -> 'x'
    assert solution.nextGreatestLetter(letters3, target3) == "x"

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(log n) - We perform binary search on the 'letters' array.
# Space complexity: O(1) - We use a constant amount of extra space.
