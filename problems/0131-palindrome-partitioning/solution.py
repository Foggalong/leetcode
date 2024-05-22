class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Given a string s, return a list of every possible partition of
        s such that every substring of the partition is a palindrome.   
        """

        n: int = len(s)
        # handle the base case of a single character
        if n == 1: return [[s]]

        partition: List[List[str]] = []

        for i in range(1, n):
            # consider each first-i-character substring of s
            substr: str = s[0:i]

            # if that substring is palindromic, then need to
            # consider all possible subpartitions of the remainder
            if self.isPalindrome(substr):
                for subpartition in self.partition(s[i:]):
                    partition.append([substr] + subpartition)

        # handle full string separately to avoid empty subpartition
        if self.isPalindrome(s): partition.append([s])

        return partition


    def isPalindrome(self, s: str) -> bool:
        """
        Helper function which, given a lowercase alphabetic string s,
        returns True if it is a palindrome or False otherwise.
        """
        return s == s[::-1]

