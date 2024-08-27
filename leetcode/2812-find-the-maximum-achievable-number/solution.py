class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        """
        We are interested in the *maximum* possible achievable
        number `x`, which is equivalent to maximising the `num`
        once `t` operations have been applied. It is trivial to
        see that this is `num` incremeneted by one `t` times.
        Per the operation, the achievable `x` this relates to
        will also have been decremented `t` times, hence to
        find this `x` we increase add `2t` to `num`.
        """
        return num + 2*t
