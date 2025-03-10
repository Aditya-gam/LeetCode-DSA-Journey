class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool

        Checks if s1 and s2 can be made equal by performing 
        at most one swap operation on exactly one of the strings.
        """
        # If they are already equal, no swap needed
        if s1 == s2:
            return True

        # Record indices where s1 and s2 differ
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
                # Early exit if we find more than 2 differences
                if len(diff) > 2:
                    return False

        # After collecting differences:
        if len(diff) != 2:
            # If not exactly 2 differences, it's impossible
            return False

        # Let the differing indices be i, j
        i, j = diff
        # Check if swapping s1[i], s1[j] or s2[i], s2[j] makes them match
        # Essentially, we only need to check if s1[i] == s2[j] and s1[j] == s2[i].
        return s1[i] == s2[j] and s1[j] == s2[i]


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "bank"
    s2 = "kanb"
    # Explanation: We can swap the first and last characters of s2 ("k" and "b")
    # to get "bank", which equals s1.
    # Should return True
    assert solution.areAlmostEqual(s1, s2) == True

    # Test Case 2
    s1 = "attack"
    s2 = "defend"
    # No single swap in either string can make them equal
    # Should return False
    assert solution.areAlmostEqual(s1, s2) == False

    # Test Case 3
    s1 = "kelb"
    s2 = "kelb"
    # Already equal, no swaps needed
    # Should return True
    assert solution.areAlmostEqual(s1, s2) == True

    print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(N), where N is the length of the input strings s1 and s2.
# Space Complexity: O(1), since we are using a constant amount of space.
