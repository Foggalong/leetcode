class Solution:
    # Give two strings, 'haystack' and 'needle', each of
    # these functions returns the index of needles first
    # occurrence in haystack, or -1 if it never appears.

    def strStr(self, haystack: str, needle: str) -> int:
        """
        Use Python's in-build `string.find(chr)`
        """
        return haystack.find(needle)

    def strStr1(self, haystack: str, needle: str) -> int:
        """
        Compare every substring of length needle.
        """
        n = len(needle)  # avoid taking it twice
        for i in range(len(haystack)-n+1):
            # compare each substring of len(needle)
            if haystack[i:i+n] == needle: return i
        return -1
    
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Remove first character of haystack until it starts
        with needle.
        """
        i = 0  # count how many characters removed
        while haystack:
            if haystack.startswith(needle):
                return i
            else:
                # remove first character of haystack
                haystack = haystack[1:]
                i += 1
        return -1


