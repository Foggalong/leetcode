class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        Returns the score of a string, defined as the sum of the absolute
        difference between the ASCII values of adjacent characters.
        """
        return sum(abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1))
