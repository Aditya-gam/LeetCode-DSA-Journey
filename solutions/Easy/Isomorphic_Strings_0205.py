class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}

        for c_s, c_t in zip(s, t):
            if c_s in map_s_to_t:
                if map_s_to_t[c_s] != c_t:
                    return False
            else:
                map_s_to_t[c_s] = c_t

            if c_t in map_t_to_s:
                if map_t_to_s[c_t] != c_s:
                    return False
            else:
                map_t_to_s[c_t] = c_s

        return True


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    s1, t1 = "egg", "add"
    # Expected: True
    print(solution.isIsomorphic(s1, t1))

    s2, t2 = "foo", "bar"
    # Expected: False
    print(solution.isIsomorphic(s2, t2))

    s3, t3 = "paper", "title"
    # Expected: True
    print(solution.isIsomorphic(s3, t3))

    s4, t4 = "ab", "aa"
    # Expected: False
    print(solution.isIsomorphic(s4, t4))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n) where n is the length of the strings 's' and 't', since we iterate over each character once in both strings and perform constant time operations for each character.
# Space complexity: O(n) where n is the length of the strings 's' and 't' since we use two dictionaries to store the mappings between characters of 's' and 't'. The space complexity is O(n) since in the worst case, we may need to store a mapping for each character in 's' and 't'.
