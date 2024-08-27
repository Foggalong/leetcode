class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        Given two strings s and t, return the minimum number of characters
        to appended to the end of s so that t becomes a subsequence of s.
        """

        s_len: int = len(s)
        t_len: int = len(t)

        # will iterate over the locations in s and t
        s_loc: int = 0
        t_loc: int = 0

        while s_loc < s_len and t_loc < t_len:
            if s[s_loc] == t[t_loc]:
                s_loc += 1
                t_loc += 1
            else:
                s_loc += 1

        # remaining characters in t must be appended to the end of s
        return t_len - t_loc
