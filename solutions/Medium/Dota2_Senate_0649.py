from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiant = deque()
        dire = deque()

        # Fill queues with indices of 'R' and 'D'
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Simulate the rounds
        n = len(senate)
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()

            # The smaller index wins and re-enters the queue with updated index
            if r_index < d_index:
                radiant.append(r_index + n)
            else:
                dire.append(d_index + n)

        # Determine the winner
        return "Radiant" if radiant else "Dire"


# Example test cases
sol = Solution()
print(sol.predictPartyVictory("RD"))  # "Radiant"
print(sol.predictPartyVictory("RDD"))  # "Dire"
print(sol.predictPartyVictory("RDDRRR"))  # "Radiant"
print(sol.predictPartyVictory("RRDD"))  # "Radiant"
print(sol.predictPartyVictory("RDDDD"))  # "Dire"
print(sol.predictPartyVictory("DDRRR"))  # "Dire"

# Complexity Analysis
# Time Complexity: O(n)
# We iterate through the input string senate once, so the time complexity is O(n).

# Space Complexity: O(n)
# We use two queues to store the indices of 'R' and 'D', respectively. The space complexity is O(n) because the total number of 'R' and 'D' characters is n.
