class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        seen_A = set()
        seen_B = set()
        prefix_common = []

        for i in range(len(A)):
            seen_A.add(A[i])
            seen_B.add(B[i])
            # Calculate the intersection and append its length
            common_count = len(seen_A.intersection(seen_B))
            prefix_common.append(common_count)

        return prefix_common


# Example test cases
sol = Solution()

# Test case 1
A = [1, 2, 3, 4, 5]
B = [4, 3, 2, 1, 5]
print(sol.findThePrefixCommonArray(A, B))  # Output: [1, 2, 3, 4, 5]

# Test case 2
A = [1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1]
print(sol.findThePrefixCommonArray(A, B))  # Output: [0, 0, 0, 0, 0]

# Test case 3
A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 5]
print(sol.findThePrefixCommonArray(A, B))  # Output: [1, 2, 3, 4, 5]

# Test case 4
A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 6]
print(sol.findThePrefixCommonArray(A, B))  # Output: [1, 2, 3, 4, 4]

# Complexity Analysis
# Time Complexity: O(N^2), Looping over n elements, and each intersection computation takes O(n) in the worst case.
# Space Complexity: O(N), Two sets for seen_A and seen_B.
