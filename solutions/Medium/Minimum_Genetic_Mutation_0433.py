from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        Function: minMutation
        Description: Finds the minimum number of mutations required to mutate from startGene to endGene.

        Parameters:
        - startGene (str): The starting gene sequence.
        - endGene (str): The target gene sequence.
        - bank (List[str]): A list of valid gene mutations.

        Returns:
        - int: The minimum number of mutations required, or -1 if not possible.
        """

        # Step 1: Convert bank to a set for quick lookup
        valid_genes = set(bank)
        if endGene not in valid_genes:
            return -1  # If endGene is not in the bank, mutation is impossible

        # Step 2: Define mutation options and BFS queue
        mutation_options = ['A', 'C', 'G', 'T']
        queue = deque([(startGene, 0)])  # (current_gene, mutation_count)
        visited = set([startGene])  # Prevent reprocessing

        # Step 3: BFS to find the shortest mutation path
        while queue:
            current_gene, mutations = queue.popleft()

            if current_gene == endGene:
                return mutations  # Found the shortest path to endGene

            # Step 4: Try mutating each character
            for i in range(len(current_gene)):
                for mutation in mutation_options:
                    # Change one character at a time
                    if mutation != current_gene[i]:
                        new_gene = current_gene[:i] + \
                            mutation + current_gene[i+1:]

                        # If the new mutation is valid and not visited
                        if new_gene in valid_genes and new_gene not in visited:
                            visited.add(new_gene)
                            queue.append((new_gene, mutations + 1))

        return -1  # No mutation path found


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Single mutation needed
    print("Test Case 1: One mutation needed")
    startGene1 = "AACCGGTT"
    endGene1 = "AACCGGTA"
    bank1 = ["AACCGGTA"]
    print("Expected Output: 1 | Actual Output:",
          solution.minMutation(startGene1, endGene1, bank1))

    # Test case 2: Two mutations required
    print("Test Case 2: Two mutations required")
    startGene2 = "AACCGGTT"
    endGene2 = "AAACGGTA"
    bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print("Expected Output: 2 | Actual Output:",
          solution.minMutation(startGene2, endGene2, bank2))

    # Test case 3: No valid mutation path
    print("Test Case 3: No valid mutation path")
    startGene3 = "AACCGGTT"
    endGene3 = "AACCGGTA"
    bank3 = []
    print("Expected Output: -1 | Actual Output:",
          solution.minMutation(startGene3, endGene3, bank3))

    # Test case 4: Longest possible path with backtracking
    print("Test Case 4: Longest valid mutation path")
    startGene4 = "AACCGGTT"
    endGene4 = "CCCCGGTT"
    bank4 = ["AACCGGTA", "CACCGGTA", "CCCCGGTA", "CCCCGGTT"]
    print("Expected Output: 3 | Actual Output:",
          solution.minMutation(startGene4, endGene4, bank4))

    # Test case 5: Direct mutation but missing in bank
    print("Test Case 5: Direct mutation possible but missing in bank")
    startGene5 = "AACCGGTT"
    endGene5 = "AACCGGTA"
    bank5 = ["AACCGGTC", "AACCGGTC"]
    print("Expected Output: -1 | Actual Output:",
          solution.minMutation(startGene5, endGene5, bank5))

    # Test case 6: Large mutation tree with dead ends
    print("Test Case 6: Large mutation tree with dead ends")
    startGene6 = "AACCGGTT"
    endGene6 = "CCACGGTT"
    bank6 = ["AACCGGTA", "CACCGGTA", "CCACGGTA",
             "CCACGGTT", "AACCGCTA", "AACCGTTA"]
    print("Expected Output: 4 | Actual Output:",
          solution.minMutation(startGene6, endGene6, bank6))

"""
Time Complexity:
- The worst-case scenario is trying all 8 positions with 3 other character mutations.
- Each mutation is checked in O(1) using a set.
- BFS ensures each valid mutation is visited once.
- Time Complexity: O(N * M), where N is the number of genes in the bank and M=8 (fixed).
- Space Complexity: O(N) for storing visited genes and the queue.
"""
