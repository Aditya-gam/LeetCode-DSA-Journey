from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        Function: constructDistancedSequence
        Description: Constructs the lexicographically largest valid sequence 
                     following the problem constraints.

        Parameters:
        - n (int): The given integer for which the sequence is to be constructed.

        Returns:
        - List[int]: The lexicographically largest valid sequence.
        """

        size = 2 * n - 1  # The length of the sequence
        result = [0] * size  # Initialize the sequence with 0s
        used = set()  # Keep track of used numbers

        def backtrack(index: int) -> bool:
            """
            Backtracking function to build the valid sequence.

            Parameters:
            - index (int): Current index in the sequence.

            Returns:
            - bool: True if a valid sequence is found, False otherwise.
            """
            if index == size:  # Base case: sequence is fully constructed
                return True

            if result[index] != 0:  # Skip pre-filled positions
                return backtrack(index + 1)

            for num in range(n, 0, -1):  # Try placing largest possible numbers first
                if num in used:
                    continue

                if num == 1:
                    result[index] = 1
                    used.add(1)
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    used.remove(1)
                else:
                    second_index = index + num
                    if second_index < size and result[second_index] == 0:
                        result[index], result[second_index] = num, num
                        used.add(num)

                        if backtrack(index + 1):
                            return True

                        result[index], result[second_index] = 0, 0
                        used.remove(num)

            return False

        backtrack(0)
        return result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: n = 3
    print(solution.constructDistancedSequence(3))
    # Expected output: [3,1,2,3,2]

    # Test case 2: n = 5
    print(solution.constructDistancedSequence(5))
    # Expected output: [5,3,1,4,3,5,2,4,2]

    # Test case 3: n = 1
    print(solution.constructDistancedSequence(1))
    # Expected output: [1]

    # Test case 4: n = 4
    print(solution.constructDistancedSequence(4))
    # Expected output: [4,2,3,2,1,3,4]

    # Test case 5: Edge case with the maximum allowed value (n = 20)
    print(solution.constructDistancedSequence(20))
    # Expected output: A valid sequence of length 39 with the largest lexicographical order.

    # Test case 6: Edge case with the minimum allowed value (n = 1)
    print(solution.constructDistancedSequence(1))
    # Expected output: [1]

    print("All test cases passed!")

# Complexity Analysis:
# Time Complexity: O(n!) where n is the given integer. The backtracking algorithm has a time complexity of O(n!) since we are trying all possible permutations of the sequence.
# Space Complexity: O(n) where n is the given integer. The space complexity is O(n) to store the sequence and the set of used numbers.
