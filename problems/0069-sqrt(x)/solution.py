class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Returns the square root of integer x (found using
        Newton's method) rounded down to the nearest integer. 
        """

        # handle edge cases, allows for better initial guess 
        if x in [0, 1]: return x 
        # take half x as the initial guess
        x0 = x/2  

        for _ in range(100):  # set iteration max
            f = x0**2 - x  # f(x0)
            fprime = 2*x0  # f'(x0)

            x1 = x0 - f/fprime  # compute Newton step

            # only need accuracy to level of integer
            if abs(x1 - x0) < 1: return int(x1)

            x0 = x1  # update x0

        return 0  # Newton did not converge
