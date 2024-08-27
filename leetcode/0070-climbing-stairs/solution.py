class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Given an integer number of stairs, return how many ways
        there are to reach the top if at each step you can climb
        either 1 or 2 steps.
        """

        # hardcode base-cases
        output = {1:1, 2:2, 3:3}
        if n in output.keys(): return n

        # every case is the sum of the previous two cases
        for i in range(4, n+1):
           output[i] = output[i-1] + output[i-2]
        return output[n]
