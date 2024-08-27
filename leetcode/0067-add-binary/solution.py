class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Takes two binary strings (a, b) and returns their sum as
        a binary string. In Python, int(x,2) converts a binary
        string to a decimal integer, and then bin(y) converts a
        decimal integer into a binary string, prefixed with '0b'.
        """
        return bin(int(a, 2) + int(b, 2))[2:]
