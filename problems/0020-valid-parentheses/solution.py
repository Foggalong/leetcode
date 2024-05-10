class Solution:
    def isValid(self, s: str) -> bool:
        """
        Takes a string of just the characters '(', ')',
        '{', '}', '[' and ']', and then returns True or
        False depending whether the bracket opening and
        closings are valid.
        """

        # closing brackets are keys, openings are values
        brackets = {")":"(", "]":"[", "}":"{"}
        # saved stack of open brackets
        stack = []

        for char in s:
            # opener always valid, add it to the stack
            if char in brackets.values():
                stack.append(char)
            # catch trying to close without ever opening
            elif not stack and char in brackets.keys():
                return False
            # if valid closer, remove open from stack
            elif stack[-1] == brackets[char]:
                stack.pop(-1)
            # if invalid closer, string invalid
            else:
                return False
        
        # if some stack remains, not everything closed
        if stack: return False
        return True
