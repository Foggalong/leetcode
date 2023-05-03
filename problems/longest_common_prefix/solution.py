class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Given a list of strings as input, returns the longest
        common prefix string amongst them. If there is no such
        prefix, an empty string is returned instead.
        """

        i = 0  # prefix is characters 0 to i
    
        while True:
            try:
                # s[i] won't exist if ran out of letters
                if any(s[i] != strs[0][i] for s in strs):
                    break
            except IndexError:
                break
            # move to next character
            i += 1

        # first i characters of first string are the prefix
        return strs[0][0:i]
