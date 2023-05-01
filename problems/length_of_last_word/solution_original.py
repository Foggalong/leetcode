class Solution:
    def lengthOfLastWord(self, s):
        # strip right whitespace
        s_stripped = s.rstrip()

        length = 0 
        index  = len(s_stripped)-1

        while index > -1:
            # search backwards until space
            if s_stripped[index] == ' ':
                return length
            else:
                length += 1
                index  -= 1
        
        return length
