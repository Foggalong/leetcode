class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, return true if it is a palindrome once
        all non-alphanumeric characters are removed, or false
        otherwise. The empty string is palindromic.
        """

        # index for left-most and right-most unchecked character
        l_index = 0
        r_index = len(s)-1

        # if indexes cross, then finished checking
        while l_index < r_index:
            # is left-most unchecked character alphanumeric
            l_char = s[l_index]
            if not l_char.isalnum():
                l_index += 1
                continue
            # is right-most unchecked character alphanumeric
            r_char = s[r_index]
            if not r_char.isalnum():
                r_index -= 1
                continue
            # both alphanumeric, so can compare (ignoring case)
            if l_char.lower() != r_char.lower(): return False
            # if were equal, move inwards from left and right
            l_index += 1
            r_index -= 1
        
        return True
