class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        Given a string array `words`, returns an array of all characters
        that appear in all strings within `words` (including duplicates).
        """

        # guaranteed at least one word
        output: List[str] = list(words[0])

        for word in words[1:]:
            output: List[str] = self.intersect(output, word)

        return output

    def intersect(self, chars: List[str], string: str) -> List[str]:
        """
        Returns the intersection of a list of characters and a string.
        Based on the solution to '350. Intersection of Two Arrays II'.
        """

        intersection: List[str] = []
        for char in string:
            if char in chars:
                intersection.append(char)
                chars.remove(char)

        return intersection
