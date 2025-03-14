class TrieNode:
    def __init__(self):
        """
        Initializes a Trie node with an empty dictionary for child nodes and a boolean flag to mark word endings.
        """
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:
    def __init__(self):
        """
        Initializes the WordDictionary with a root TrieNode.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word to the data structure.

        Parameters:
        - word (str): The word to be added to the Trie.

        Returns:
        - None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        """
        Searches for a word in the data structure, where '.' can represent any letter.

        Parameters:
        - word (str): The word to be searched (can contain '.' as wildcards).

        Returns:
        - bool: True if the word is found, otherwise False.
        """
        return self._search_in_trie(word, 0, self.root)

    def _search_in_trie(self, word: str, index: int, node: TrieNode) -> bool:
        """
        Recursively searches for the word in the Trie.

        Parameters:
        - word (str): The word being searched.
        - index (int): The current index in the word.
        - node (TrieNode): The current Trie node.

        Returns:
        - bool: True if the word is found, otherwise False.
        """
        if index == len(word):
            return node.is_end_of_word  # If we reach the end, check if it's a valid word

        char = word[index]

        if char == '.':
            for child in node.children.values():
                if self._search_in_trie(word, index + 1, child):
                    return True
        elif char in node.children:
            return self._search_in_trie(word, index + 1, node.children[char])

        return False  # Word not found


# Example Test Cases
if __name__ == "__main__":
    wordDictionary = WordDictionary()

    # Define a constant for the expected output string
    EXPECTED_OUTPUT = "Expected Output: {} | Actual Output: {}"

    # Test case 1: Adding and searching exact words
    print("Test Case 1: Basic Word Addition & Search")
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(EXPECTED_OUTPUT.format(False, wordDictionary.search("pad")))  # False
    print(EXPECTED_OUTPUT.format(True, wordDictionary.search("bad")))  # True

    # Test case 2: Searching words with single wildcard '.'
    print("Test Case 2: Single Wildcard Search")
    print(EXPECTED_OUTPUT.format(True, wordDictionary.search(".ad")))  # True

    # Test case 3: Searching words with multiple wildcards '..'
    print("Test Case 3: Multi Wildcard Search")
    print(EXPECTED_OUTPUT.format(True, wordDictionary.search("b..")))  # True

    # Test case 4: Searching for words that are not added
    print("Test Case 4: Search for Non-Existent Words")
    print(EXPECTED_OUTPUT.format(False, wordDictionary.search("xyz")))  # False

    # Test case 5: Searching a word that has a similar prefix but not an exact match
    print("Test Case 5: Search with Partial Prefix Match")
    wordDictionary.addWord("bat")
    print(EXPECTED_OUTPUT.format(False, wordDictionary.search("bats")))  # False

    # Test case 6: Searching words with no wildcard that do not exist
    print("Test Case 6: Search for Completely Different Word")
    print(EXPECTED_OUTPUT.format(False, wordDictionary.search("cat")))  # False

"""
Time Complexity:
- addWord(): O(N), where N is the length of the word.
- search(): O(26^M) in the worst case (M = length of word, max 2 wildcards), but typically much faster in practice.
- Space Complexity: O(N * 26), where N is the number of words stored in the Trie.

Trie ensures efficient storage and retrieval while supporting wildcard search.
"""
