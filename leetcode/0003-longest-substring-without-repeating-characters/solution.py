class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, return the length of the longest substring
        without repeating characters as an integer.
        """

        n: int = len(s)

        # handle the degenerate cases
        if n in (0, 1): return n

        # index for first and last character of substring to consider
        i: int = 0
        j: int = 1  # now guaranteed n >= 2
        length: int = 1 

        # iterate over substring in a sliding window approach
        while j < n:
            # advance substring start to the last location of s[j]
            # in the previous substring. if s[j] isn't in s[i:j],
            # this will return -1, so i will not be advanced. this
            # redundent -1+1 is better than checking inclusion and
            # finding separately
            i += s[i:j].find(s[j]) + 1
            # advance substring end point every time
            j += 1
            # check if we've made the substring longer
            length: int = max(length, j-i)

        return length
        
