class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]

        For each query [x, y], assigns ball x the color y. 
        Returns the number of distinct colors after each query.
        """
        ballToColor = {}   # Maps ball -> current color
        colorCount = {}    # Maps color -> how many balls have this color

        results = []

        for x, y in queries:
            # If ball x already had a color, remove one count from that color
            if x in ballToColor:
                oldColor = ballToColor[x]
                if oldColor in colorCount:
                    colorCount[oldColor] -= 1
                    if colorCount[oldColor] == 0:
                        del colorCount[oldColor]

            # Assign new color to ball x
            ballToColor[x] = y
            if y not in colorCount:
                colorCount[y] = 0
            colorCount[y] += 1

            # Number of distinct colors is length of colorCount dictionary
            results.append(len(colorCount))

        return results


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    limit1 = 4
    queries1 = [[1, 4], [2, 5], [1, 3], [3, 4]]
    # Explanation:
    # - After 1st query: ball 1 -> color 4, distinct colors=1
    # - After 2nd query: ball 1->4, ball 2->5, distinct colors=2
    # - After 3rd query: ball 1->3, ball 2->5, distinct colors=2
    # - After 4th query: ball 1->3, ball 2->5, ball 3->4, distinct colors=3
    print(solution.queryResults(limit1, queries1))  # Expected [1,2,2,3]

    # Example 2
    limit2 = 4
    queries2 = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
    # Explanation:
    # - Q0: ball 0->1 => distinct=1
    # - Q1: 0->1, 1->2 => distinct=2
    # - Q2: 0->1,1->2,2->2 => distinct=2
    # - Q3: 0->1,1->2,2->2,3->4 => distinct=3
    # - Q4: 0->1,1->2,2->2,3->4,4->5 => distinct=4
    print(solution.queryResults(limit2, queries2))  # Expected [1,2,2,3,4]

    # Example 3
    limit3 = 4
    queries3 = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]
    # Explanation:
    # - Q0: 0->1 => distinct=1
    # - Q1: 0->1,1->1 => distinct=1
    # - Q2: 0->1,1->1,2->1 => distinct=1
    # - Q3: 0->1,1->1,2->1,3->1 => distinct=1
    # - Q4: 0->1,1->1,2->1,3->1,4->1 => distinct=1
    print(solution.queryResults(limit3, queries3))  # Expected [1,1,1,1,1]

    # Example 4
    limit4 = 4
    queries4 = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 1]]
    # Explanation:
    # - Q0: 0->1 => distinct=1
    # - Q1: 0->1,1->2 => distinct=2
    # - Q2: 0->1,1->2,2->3 => distinct=3
    # - Q3: 0->1,1->2,2->3,3->4 => distinct=4
    # - Q4: 0->1,1->2,2->3,3->4,4->1 => distinct=4
    print(solution.queryResults(limit4, queries4))  # Expected [1,2,3,4,4]

    print("All test cases passed!")

# COMPLEXITY ANALYSIS
# Time complexity: O(n) for n queries, as we iterate through each query once.
# Space complexity: O(k) for storing the color count, where k is the number of distinct colors assigned to balls.
