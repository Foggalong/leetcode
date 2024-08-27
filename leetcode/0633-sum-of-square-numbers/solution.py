from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Given a non-negative integer c, return True if there're
        two integers a and b such that a^2 + b^2 = c
        """

        # iterate over b which keep sqrt(c-b^2) real
        for b in range(int(sqrt(c))+1):
            # known b and c means a is uniquely determined
            a: float = sqrt(c - b*b)
            # uses Python's dynamic typing to check if a's an integer
            if a == int(a): return True
        
        return False
    

    def judgeSquareSumSlow(self, c: int) -> bool:
        """
        Naive approach by exhaustion, only making use of a + b <= c
        as a constraint. This version hit TLE for c = 10000000.
        """

        # handle edge cases 0^2 + 0^2 = 0, 1^2 + 0^2 = 1 
        if c in [0, 1]: return True

        half: int = int(c/2) + 1

        for a in range(half):
            for b in range(half):
                if a*a + b*b == c:
                    return True
        
        return False

