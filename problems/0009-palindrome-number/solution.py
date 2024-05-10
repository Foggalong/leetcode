from math import ceil, log10

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        returns True if integer x is a palindrome (i.e. it
        reads the same left-to-right as right-to-left) and
        False otherwise. Does this without converting x to
        a string, list, or other object.
        """

        # negative numbers cannot be palindromes
        if x < 0: return False

        # handle specifically to avoid log issues
        if x == 0: return True 

        # work out the number of digits
        digits = int(log10(x)) + 1

        for i in range(1, ceil(digits/2)+1):
            # computes the ith digit
            frnt_digit = (x // (10**(digits-i))) % 10
            # computes the (digits-i)th digit
            back_digit = (x%(10**i)) // (10**(i-1))
            # if two aren't equal, done
            if frnt_digit != back_digit:
                return False

        return True
