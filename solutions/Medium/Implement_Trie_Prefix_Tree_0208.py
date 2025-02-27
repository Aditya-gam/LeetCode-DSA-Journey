class TrieNode(object):
    def __init__(self):
        """
        Each TrieNode contains:
        - children: a dictionary mapping characters to TrieNode
        - endOfWord: a boolean indicating whether a word ends at this node
        """
        self.children = {}
        self.endOfWord = False


class Trie(object):

    def __init__(self):
        """
        Initialize the trie with a root node.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the trie.

        :param word: str - the word to be inserted
        """
        current = self.root
        for char in word:
            # If the current character path doesn't exist, create it
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        # After inserting all characters, mark the end of the word
        current.endOfWord = True

    def search(self, word):
        """
        Search for a word in the trie.

        :param word: str - the word to be searched
        :return: bool - True if word is found, False otherwise
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        # Return True only if current node is marked as an end of a word
        return current.endOfWord

    def startsWith(self, prefix):
        """
        Check if there is any word in the trie that starts with the given prefix.

        :param prefix: str - the prefix to be checked
        :return: bool - True if there is a word starting with prefix, False otherwise
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

# Example test cases


def test_trie():
    # Create a Trie object
    trie = Trie()

    # Example test from the problem statement:
    trie.insert("apple")
    assert trie.search("apple") == True     # returns True
    assert trie.search("app") == False      # returns False
    assert trie.startsWith("app") == True   # returns True
    trie.insert("app")
    assert trie.search("app") == True       # returns True

    # Additional tests
    trie.insert("bat")
    trie.insert("bath")
    # Check existing words
    assert trie.search("bat") == True
    assert trie.search("bath") == True
    # Check partial prefix
    assert trie.startsWith("ba") == True
    # Check non-existing words
    assert trie.search("bad") == False
    # Check prefix that doesn't exist
    assert trie.startsWith("cat") == False

    print("All test cases passed!")


test_trie()

# Complexity Analysis
# Time complexity: O(m) for insert, search, and startsWith, where m is the length of the word or prefix.
# Space complexity: O(m) for the worst-case scenario, where m is the length of the word or prefix.
