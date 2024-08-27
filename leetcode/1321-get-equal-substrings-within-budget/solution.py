class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        Return the maximum length of a substring of s that can be changed into the
        corresponding substring of t with a cost less than or equal to maxCost. If
        there is no substring from s that can be changed to its corresponding sub-
        string from t, return 0. The cost is defined as the sum absolute difference
        between the ASCII values of the characters in each string.
        """

        def cost(index: int) -> int:
            return abs(ord(s[index]) - ord(t[index]))

        window_cost: int = 0
        max_length: int = 0

        start: int = 0  # window start index

        # using a moving window, add an additional character to be the
        # last in the window each iteration
        for end in range(len(s)):
            # cost to transform final character in window
            window_cost += cost(end)

            # if now exceeding, remove start characters to the
            # window until cost is back below maximum
            while window_cost > maxCost:
                window_cost -= cost(start)
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
