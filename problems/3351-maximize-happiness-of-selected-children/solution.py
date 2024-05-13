class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        """
        Given a queue of n children where the ith child has happiness value
        happiness[i], select k children to maximise happiness. Every time a
        child is selected the happiness of all other children decreases by
        one. Return the maximum possible happiness.
        """

        happiness_sum = 0
        l = 0
        for h in nlargest(k, happiness):
            # all future children will contribute no happiness
            if h-l < 0: break
            # add next biggest happiness, minus one per round
            happiness_sum += h-l
            l += 1

        return happiness_sum
