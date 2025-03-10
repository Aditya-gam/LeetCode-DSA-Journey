class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int

        Returns the index of the gas station from which you can start to 
        complete a full circle. If impossible, returns -1.
        """
        totalDiff = 0
        partialDiff = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            totalDiff += diff
            partialDiff += diff

            if partialDiff < 0:
                # Can't reach station i+1 from the current start
                start = i + 1
                partialDiff = 0

        # If totalDiff >= 0, a solution must exist at 'start'
        return start if totalDiff >= 0 else -1


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    # Expected output: 3
    # Explanation in the prompt
    assert solution.canCompleteCircuit(gas1, cost1) == 3

    # Test case 2
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    # Expected output: -1 (no solution)
    assert solution.canCompleteCircuit(gas2, cost2) == -1

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate over the gas and cost arrays once.
# Space complexity: O(1) - We use a constant amount of extra space.
