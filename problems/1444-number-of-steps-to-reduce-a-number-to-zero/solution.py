class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
        Given an integer num, returns the number of steps to
        reduce it to zero. In one step, if the current number
        is even, divide it by 2, otherwise, subtract 1 from it.
        """

        if num == 0:
            return 0
        elif num % 2:
            return 1 + self.numberOfSteps(num-1)
        else:
            return 1 + self.numberOfSteps(num/2)
