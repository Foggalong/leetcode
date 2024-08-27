class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Given a string s which consists of lowercase or uppercase letters,
        return the length of the longest palindrome that can be built with
        those letters.
        """

        # first build a dictionary of character frequencies for the string
        counts: dict[str, int] = {}
        for c in s:
            try:
                counts[c] += 1
            except KeyError:
                counts[c] = 1

        # if we have a character which appears an odd number of times, we
        # can place one of those occurances at the middle of our palindrome
        have_odd: bool = False

        # when computing the length we no longer care which characters the
        # counts refer to, so only iterate over the count values
        length: int = 0
        for count in counts.values():
            length += count
            # if a character appears an odd number of times, we can't make
            # use of that last occurance in all but one case (see above)
            if count % 2:  # odd
                have_odd = True
                length -= 1

        # add the single occurance of an odd character if we have one
        return length + have_odd

        
