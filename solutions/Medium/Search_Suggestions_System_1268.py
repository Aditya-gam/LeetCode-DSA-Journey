import bisect


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        Returns a list of lists of product suggestions for each prefix of searchWord.

        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        # Step 1: Sort the products lexicographically
        products.sort()

        result = []
        prefix = ""

        for char in searchWord:
            # Add the next character to the prefix
            prefix += char

            # Step 2: Find the leftmost index to insert prefix
            # This effectively finds where 'prefix' would go in 'products'
            # so we know where potential matches could start.
            idx = bisect.bisect_left(products, prefix)

            # Step 3: Gather up to 3 matching products starting from idx
            suggestions = []
            for i in range(idx, min(idx + 3, len(products))):
                # Check if product[i] starts with the current prefix
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break

            # Step 4: Append this list of suggestions
            result.append(suggestions)

        return result

# Example test cases


def test_searchSuggestions():
    sol = Solution()

    # Test Case 1 (From the Example)
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    # Expected:
    # 1. prefix="m" -> ["mobile","moneypot","monitor"]
    # 2. prefix="mo" -> ["mobile","moneypot","monitor"]
    # 3. prefix="mou" -> ["mouse","mousepad"]
    # 4. prefix="mous" -> ["mouse","mousepad"]
    # 5. prefix="mouse" -> ["mouse","mousepad"]
    expected = [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"]
    ]
    assert sol.suggestedProducts(products, searchWord) == expected

    # Test Case 2 (From the Example)
    products = ["havana"]
    searchWord = "havana"
    # We have only one product "havana"
    # For each prefix, the only suggestion is "havana"
    expected = [
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"]
    ]
    assert sol.suggestedProducts(products, searchWord) == expected

    # Test Case 3
    products = ["bags", "baggage", "banner", "box", "cloths"]
    searchWord = "bags"
    # After sorting -> ["baggage", "bags", "banner", "box", "cloths"]
    # 1) prefix="b"   -> ["baggage", "bags", "banner"]
    # 2) prefix="ba"  -> ["baggage", "bags", "banner"]
    # 3) prefix="bag" -> ["baggage", "bags"]
    # 4) prefix="bags"-> ["baggage", "bags"]
    expected = [
        ["baggage", "bags", "banner"],
        ["baggage", "bags", "banner"],
        ["baggage", "bags"],
        ["baggage", "bags"]
    ]
    assert sol.suggestedProducts(products, searchWord) == expected

    # Test Case 4
    products = ["aaa", "aa", "aaaa", "aaaab", "aaac"]
    searchWord = "aaaa"
    # sorted -> ["aa", "aaa", "aaaab", "aaac", "aaaa"]
    # prefix="a": ["aa", "aaa", "aaaab"]
    # prefix="aa": ["aa", "aaa", "aaaab"]
    # prefix="aaa": ["aaa", "aaaab", "aaac"] (because all start with "aaa", but we only pick the first three in sorted order)
    # prefix="aaaa": ["aaaab", "aaaa"] (since we only have these matching "aaaa")
    expected = [
        ["aa", "aaa", "aaaab"],
        ["aa", "aaa", "aaaab"],
        ["aaa", "aaaab", "aaac"],
        ["aaaab", "aaaa"]
    ]
    assert sol.suggestedProducts(products, searchWord) == expected

    print("All test cases passed!")


test_searchSuggestions()

# Complexity Analysis
# Time Complexity: O(n * m * log(n)) where n is the number of products and m is the length of the searchWord.
# We iterate over the searchWord and for each prefix, we perform a binary search to find the leftmost index.
# The binary search takes O(log(n)) time and we do this for each of the m prefixes.
# Sorting the products initially takes O(n * log(n)) time.

# Space Complexity: O(n) where n is the number of products.
# We are storing the sorted products array which takes O(n) space.
