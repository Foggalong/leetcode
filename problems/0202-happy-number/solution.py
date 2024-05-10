class Solution:
    def sumSquaredDigits(self, m: int) -> int:
        """
        Takes an integer m as input and then returns
        an integer which is the sum of the squares of
        the digits of m.
        """

        total = 0
        # hardcode squares to avoid calculating them
        squares = (0,1,4,9,16,25,36,49,64,81)
        # iterate over m's digits w/o converting to list
        while m:
            # add square of last digit to running total
            total += squares[m % 10]
            # remove last digit from m
            m //= 10
        return total


    def isHappy(self, n: int) -> bool:
        """
        Takes an integer n as input and then returns a
        boolean indicating whether n is a happy number.
        """

        # track what we've seen, check if we've looped
        seen = []
        while n not in seen:
            seen.append(n)
            # replace n with sum of squared digits 
            n = self.sumSquaredDigits(n)
            # if reached 1, we're happy!
            if n == 1: return True
        # if n in seen, we're not happy
        return False

