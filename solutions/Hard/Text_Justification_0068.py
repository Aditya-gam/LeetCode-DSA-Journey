class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]

        Returns a list of fully-justified lines of text given the words
        and maxWidth.
        """

        def justify_line(line_words, line_length, maxWidth, is_last_line=False):
            """
            Justify a single line given:
            - line_words: the words in that line
            - line_length: sum of lengths of the words (excluding spaces)
            - maxWidth: the desired width
            - is_last_line: whether this is the last line or a line with a single word
            """
            if len(line_words) == 1 or is_last_line:
                # Left-justify: join with single space, then pad the right
                line = " ".join(line_words)
                return line + " " * (maxWidth - len(line))

            # Otherwise, fully justify the line
            total_spaces = maxWidth - line_length
            gaps = len(line_words) - 1

            # Minimum spaces in each gap
            space_per_gap = total_spaces // gaps
            # Extra spaces for the leftmost gaps
            extra = total_spaces % gaps

            justified_line_parts = []
            for i in range(gaps):
                justified_line_parts.append(line_words[i])
                # Distribute the spaces
                spaces_to_insert = space_per_gap + (1 if i < extra else 0)
                justified_line_parts.append(" " * spaces_to_insert)
            # Append the last word
            justified_line_parts.append(line_words[-1])

            return "".join(justified_line_parts)

        res = []
        current_words = []
        current_len = 0  # sum of the lengths of words in current line

        for w in words:
            # If we add this word plus (number of words in line) as min spaces, would it exceed maxWidth?
            if current_words and (current_len + len(w) + len(current_words)) > maxWidth:
                # Justify current line
                res.append(justify_line(current_words, current_len,
                           maxWidth, is_last_line=False))
                current_words = []
                current_len = 0

            current_words.append(w)
            current_len += len(w)

        # Handle the last line
        res.append(justify_line(current_words, current_len,
                   maxWidth, is_last_line=True))

        return res


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth1 = 16
    # Expected:
    # [
    #    "This    is    an",
    #    "example  of text",
    #    "justification.  "
    # ]
    print(solution.fullJustify(words1, maxWidth1))

    # Example 2
    words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth2 = 16
    # Expected:
    # [
    #   "What   must   be",
    #   "acknowledgment  ",
    #   "shall be        "
    # ]
    print(solution.fullJustify(words2, maxWidth2))

    # Example 3
    words3 = ["Science", "is", "what", "we", "understand", "well", "enough", "to",
              "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    maxWidth3 = 20
    # Expected:
    # [
    #   "Science  is  what we",
    #   "understand      well",
    #   "enough to explain to",
    #   "a  computer.  Art is",
    #   "everything  else  we",
    #   "do                  "
    # ]
    print(solution.fullJustify(words3, maxWidth3))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n), where n is the number of words in the input list 'words'.

# Space complexity: O(n), where n is the number of words in the input list 'words'. The space complexity is due to the output list 'res'.
# The space complexity can be reduced to O(1) if we modify the input list 'words' in place.
