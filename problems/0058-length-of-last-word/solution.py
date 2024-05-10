class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        record = False
        length = 0

        for char in s[::-1]:
            if record is False:
                if char != ' ':
                    record = True
                    length += 1
                pass

            else:
                # search backwards until space
                if char is ' ':
                    return length
                else:
                    length += 1

        return length