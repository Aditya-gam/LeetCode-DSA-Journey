import heapq


class Solution:
    def totalCost(self, costs, k, candidates):
        """
        Calculate the total cost to hire k workers.

        Parameters:
        costs (List[int]): The cost of hiring each worker.
        k (int): The number of workers to hire.
        candidates (int): The number of candidates to consider from both ends.

        Returns:
        int: The total cost to hire k workers.
        """
        n = len(costs)
        total_cost = 0

        # Two priority queues: one for the left and one for the right
        left_heap, right_heap = [], []
        left, right = 0, n - 1

        # Fill the initial heaps with candidates from both sides
        for _ in range(min(candidates, n)):
            heapq.heappush(left_heap, (costs[left], left))
            left += 1

        for _ in range(min(candidates, n - left)):
            heapq.heappush(right_heap, (costs[right], right))
            right -= 1

        # Hire k workers
        for _ in range(k):
            if not left_heap:
                cost, idx = heapq.heappop(right_heap)
            elif not right_heap:
                cost, idx = heapq.heappop(left_heap)
            else:
                # Compare the two heaps
                if left_heap[0][0] <= right_heap[0][0]:
                    cost, idx = heapq.heappop(left_heap)
                else:
                    cost, idx = heapq.heappop(right_heap)

            total_cost += cost

            # Replenish the heap if possible
            if idx < left and left <= right:
                heapq.heappush(left_heap, (costs[left], left))
                left += 1
            elif idx > right and left <= right:
                heapq.heappush(right_heap, (costs[right], right))
                right -= 1

        return total_cost


# Example test cases
solution = Solution()

# Test case 1
costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
k = 3
candidates = 4
assert solution.totalCost(costs, k, candidates) == 11  # Expected: 11

# Test case 2
costs = [1, 2, 4, 1]
k = 3
candidates = 3
assert solution.totalCost(costs, k, candidates) == 4  # Expected: 4

# Test case 3
costs = [1, 2, 3, 4, 5]
k = 2
candidates = 2
assert solution.totalCost(costs, k, candidates) == 3  # Expected: 3

# Test case 4
costs = [5, 5, 5, 5]
k = 2
candidates = 2
assert solution.totalCost(costs, k, candidates) == 10  # Expected: 10

assert Solution().totalCost(
    [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58], 11, 2) == 423
assert Solution().totalCost([5, 5, 5, 5], 2, 2) == 10
assert Solution().totalCost([10], 1, 1) == 10

# Complexity Analysis
# Time Complexity: O((candidates+k)⋅log(candidates))
# Adding workers to the heap initially: O(candidates⋅log(candidates)).
# Popping and pushing in the heap k times: O(k⋅log(candidates)).

# Space Complexity: O(candidates)
# Heap size is O(candidates).
