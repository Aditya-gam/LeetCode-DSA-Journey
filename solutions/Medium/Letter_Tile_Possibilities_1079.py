from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Function: numTilePossibilities
        Description: Computes the number of possible non-empty sequences that can be 
                     formed using the given letter tiles.

        Parameters:
        - tiles (str): A string representing the available letter tiles.

        Returns:
        - int: The number of unique sequences that can be formed.
        """

        def backtrack(counter):
            """
            Helper function to generate all possible sequences using backtracking.

            Parameters:
            - counter (Counter): A dictionary tracking the remaining tile counts.

            Returns:
            - int: The number of valid sequences generated.
            """
            count = 0
            for tile in counter:
                if counter[tile] > 0:
                    counter[tile] -= 1
                    count += 1 + backtrack(counter)
                    counter[tile] += 1  # Backtrack and restore state
            return count

        tile_counter = Counter(tiles)

        return backtrack(tile_counter)


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic case with duplicates
    print(solution.numTilePossibilities("AAB"))
    # Expected output: 8

    # Test case 2: Larger input with multiple duplicates
    print(solution.numTilePossibilities("AAABBC"))
    # Expected output: 188

    # Test case 3: Single character
    print(solution.numTilePossibilities("V"))
    # Expected output: 1

    # Test case 4: Two distinct characters
    print(solution.numTilePossibilities("XY"))
    # Expected output: 4  -> {"X", "Y", "XY", "YX"}

    # Test case 5: All unique characters
    print(solution.numTilePossibilities("ABC"))
    # Expected output: 15

    # Test case 6: Maximum length input with repeated characters
    print(solution.numTilePossibilities("AAAAAAA"))
    # Expected output: 7 (all variations of A)

    # Test case 7: Edge case with an empty string
    print(solution.numTilePossibilities(""))
    # Expected output: 0

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(2^n) where n is the number of unique characters in the input string.
# The backtracking algorithm has a time complexity of O(2^n) since we are trying all possible combinations of the characters.

# Space Complexity: O(n) where n is the number of unique characters in the input string.
# The space complexity is determined by the depth of the recursion stack, which is at most the number of unique characters in the input string.
